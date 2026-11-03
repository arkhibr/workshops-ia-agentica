import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { argumentosDoValidate, verificarFicha, verificarMarketplace } from "../portao.mjs";

const aqui = path.dirname(fileURLToPath(import.meta.url));
const exemplo = path.join(aqui, "..", "marketplace-acme");
const portao = path.join(aqui, "..", "portao.mjs");

const fichaModerada = () => ({
  dono: "Coordenação de Projetos",
  finalidade: "Extrair tarefas e riscos de transcrições",
  alternativaSemIA: "Leitura manual da transcrição",
  dados: ["interno"],
  ferramentas: ["Read"],
  autonomia: "sugere",
  faixa: "moderada",
  fatorDecisivo: "Os dados são internos e o resultado passa por revisão humana",
  premissas: ["A transcrição não contém dado sensível"],
  riscos: [
    {
      evento: "Texto da transcrição é lido como instrução",
      consequencia: "Tarefa falsa entra no relatório",
      preventivo: { tipo: "validacao", descricao: "Script confere o formato do relatório" },
      detectivo: "Revisão do relatório por uma pessoa",
      evidencia: "Registro da revisão",
    },
  ],
  gate: { aprovador: "", aprovadoEm: "" },
  revisao: { gatilhos: ["Troca de modelo"], retirada: "Remover o plugin do marketplace" },
});

function marketplaceTemporario(plugins) {
  const pasta = fs.mkdtempSync(path.join(os.tmpdir(), "portao-"));
  fs.mkdirSync(path.join(pasta, ".claude-plugin"));
  const entradas = plugins.map(({ name, source }) => ({ name, source: source ?? `./plugins/${name}` }));
  fs.writeFileSync(
    path.join(pasta, ".claude-plugin", "marketplace.json"),
    JSON.stringify({ name: "temporario", owner: { name: "ACME" }, plugins: entradas }),
  );
  return pasta;
}

function criarPlugin(pasta, nome, conteudo) {
  const dir = path.join(pasta, "plugins", nome);
  fs.mkdirSync(dir, { recursive: true });
  if (conteudo !== undefined) fs.writeFileSync(path.join(dir, "governanca.json"), conteudo);
}

test("ficha completa de faixa moderada passa", () => {
  assert.deepEqual(verificarFicha(fichaModerada()), []);
});

test("campo obrigatório vazio reprova", () => {
  const ficha = { ...fichaModerada(), dono: "" };
  assert.ok(verificarFicha(ficha).includes("dono: campo obrigatório vazio"));
});

test("dados em texto reprova sem quebrar", () => {
  const ficha = { ...fichaModerada(), dados: "interno" };
  assert.ok(verificarFicha(ficha).includes("dados: esperado uma lista"));
});

test("dado sensível exige faixa alta", () => {
  const ficha = { ...fichaModerada(), dados: ["sensivel"] };
  assert.ok(verificarFicha(ficha).includes("faixa: dado sensível leva à faixa alta"));
});

test("autonomia executa exige faixa alta", () => {
  const ficha = { ...fichaModerada(), autonomia: "executa" };
  assert.ok(verificarFicha(ficha).includes("faixa: autonomia executa leva à faixa alta"));
});

test("faixa alta sem aprovação registrada reprova", () => {
  const ficha = { ...fichaModerada(), faixa: "alta" };
  assert.ok(verificarFicha(ficha).includes("gate: faixa alta exige aprovador e data de aprovação"));
});

test("risco só com instrução ao modelo reprova", () => {
  const ficha = fichaModerada();
  ficha.riscos[0].preventivo = { tipo: "instrucao", descricao: "Pedir ao modelo que tenha cuidado" };
  assert.ok(
    verificarFicha(ficha).includes("riscos[0]: controle preventivo depende só de instrução ao modelo"),
  );
});

test("marketplace de exemplo: revisando-pull-requests reprova e identificando-tarefas-e-riscos passa", () => {
  const resultado = verificarMarketplace(exemplo);
  const por = Object.fromEntries(resultado.map((r) => [r.plugin, r]));
  assert.deepEqual(por["identificando-tarefas-e-riscos"].erros, []);
  assert.ok(por["revisando-pull-requests"].erros.length > 0);
});

test("governanca.json ausente vira erro do plugin e os demais seguem", () => {
  const pasta = marketplaceTemporario([{ name: "sem-ficha" }, { name: "com-ficha" }]);
  criarPlugin(pasta, "sem-ficha");
  criarPlugin(pasta, "com-ficha", JSON.stringify(fichaModerada()));
  const [primeiro, segundo] = verificarMarketplace(pasta);
  assert.deepEqual(primeiro.erros, ["governanca.json: arquivo ausente"]);
  assert.deepEqual(segundo.erros, []);
});

test("JSON malformado vira erro do plugin", () => {
  const pasta = marketplaceTemporario([{ name: "quebrado" }]);
  criarPlugin(pasta, "quebrado", "{ dono: ");
  const [resultado] = verificarMarketplace(pasta);
  assert.equal(resultado.erros.length, 1);
  assert.match(resultado.erros[0], /^governanca\.json: JSON inválido/);
});

test("fonte remota gera aviso e nenhum erro", () => {
  const pasta = marketplaceTemporario([
    { name: "remoto", source: { source: "github", repo: "acme/remoto" } },
  ]);
  const [resultado] = verificarMarketplace(pasta);
  assert.deepEqual(resultado.erros, []);
  assert.equal(resultado.aviso, "fonte remota: ficha não verificada localmente");
});

function catalogoTemporario(conteudo) {
  const pasta = fs.mkdtempSync(path.join(os.tmpdir(), "portao-"));
  if (conteudo !== undefined) {
    fs.mkdirSync(path.join(pasta, ".claude-plugin"));
    fs.writeFileSync(path.join(pasta, ".claude-plugin", "marketplace.json"), conteudo);
  }
  return pasta;
}

const rodarPortao = (args, env = process.env) =>
  spawnSync(process.execPath, [portao, ...args], { encoding: "utf8", env });

test("marketplace.json ausente vira erro em português", () => {
  assert.throws(() => verificarMarketplace(catalogoTemporario()), {
    message: /^marketplace\.json: arquivo ausente em /,
  });
});

test("marketplace.json malformado vira erro em português", () => {
  assert.throws(() => verificarMarketplace(catalogoTemporario("{ name: ")), {
    message: /^marketplace\.json: JSON inválido/,
  });
});

test("plugins fora de lista vira erro em português", () => {
  const pasta = catalogoTemporario(JSON.stringify({ name: "x", owner: { name: "ACME" }, plugins: {} }));
  assert.throws(() => verificarMarketplace(pasta), { message: "marketplace.json: plugins: esperado uma lista" });
});

test("entrada nula vira erro da entrada e as demais seguem", () => {
  const pasta = marketplaceTemporario([{ name: "com-ficha" }]);
  const arquivo = path.join(pasta, ".claude-plugin", "marketplace.json");
  const catalogo = JSON.parse(fs.readFileSync(arquivo, "utf8"));
  catalogo.plugins.unshift(null);
  fs.writeFileSync(arquivo, JSON.stringify(catalogo));
  criarPlugin(pasta, "com-ficha", JSON.stringify(fichaModerada()));
  const [primeiro, segundo] = verificarMarketplace(pasta);
  assert.deepEqual(primeiro, { plugin: "plugins[0]", erros: ["entrada: esperado um objeto com name e source"] });
  assert.deepEqual(segundo.erros, []);
});

test("ficha salva com BOM, comum em editores do Windows, é lida", () => {
  const pasta = marketplaceTemporario([{ name: "com-bom" }]);
  criarPlugin(pasta, "com-bom", "\uFEFF" + JSON.stringify(fichaModerada()));
  const [resultado] = verificarMarketplace(pasta);
  assert.deepEqual(resultado.erros, []);
});

test("linha de comando com catálogo ilegível sai com código 2 e sem rastreamento de pilha", () => {
  const r = rodarPortao([catalogoTemporario("{ name: "), "--sem-claude"]);
  assert.equal(r.status, 2);
  assert.match(r.stderr, /^portão: marketplace\.json: JSON inválido/);
  assert.doesNotMatch(r.stderr, /\n\s+at /);
});

test("no Windows o caminho vai entre aspas para o shell aceitar pasta com espaço", () => {
  assert.deepEqual(argumentosDoValidate("C:\\Users\\Maria Silva\\marketplace-acme", "win32"), [
    'claude plugin validate "C:\\Users\\Maria Silva\\marketplace-acme"',
    [],
    { stdio: "inherit", shell: true },
  ]);
});

test("no Windows a barra final some, para que \\\" não escape a aspa de fechamento", () => {
  assert.deepEqual(argumentosDoValidate("C:\\x y\\m\\", "win32"), [
    'claude plugin validate "C:\\x y\\m"',
    [],
    { stdio: "inherit", shell: true },
  ]);
  assert.deepEqual(argumentosDoValidate("C:\\x\\m\\", "win32")[0], 'claude plugin validate "C:\\x\\m"');
});

test("fora do Windows o caminho segue como argumento, sem aspas e sem shell", () => {
  assert.deepEqual(argumentosDoValidate("/home/maria silva/marketplace-acme", "linux"), [
    "claude",
    ["plugin", "validate", "/home/maria silva/marketplace-acme"],
    { stdio: "inherit", shell: false },
  ]);
});

test("claude ausente gera mensagem com a versão mínima e código 2", { skip: process.platform === "win32" }, () => {
  const pasta = marketplaceTemporario([{ name: "com-ficha" }]);
  criarPlugin(pasta, "com-ficha", JSON.stringify(fichaModerada()));
  const r = rodarPortao([pasta], { ...process.env, PATH: "" });
  assert.equal(r.status, 2);
  assert.match(r.stderr, /portão: o comando claude não foi encontrado/);
  assert.match(r.stderr, /2\.1\.317/);
});

for (const [rotulo, tipo] of [["acentuado", "instrução"], ["com maiúscula", "Instrucao"], ["ausente", undefined]]) {
  test(`tipo do controle preventivo ${rotulo} reprova com a lista de valores aceitos`, () => {
    const ficha = fichaModerada();
    ficha.riscos[0].preventivo = { tipo, descricao: "Pedir ao modelo que tenha cuidado" };
    assert.ok(
      verificarFicha(ficha).includes(
        "riscos[0].preventivo.tipo: valores aceitos são permissao, hook, validacao, politica-api, revisao-humana, instrucao",
      ),
    );
  });
}

test("entrada sem name vira erro da entrada, identificada pela posição", () => {
  const pasta = marketplaceTemporario([{ name: "com-ficha" }]);
  const arquivo = path.join(pasta, ".claude-plugin", "marketplace.json");
  const catalogo = JSON.parse(fs.readFileSync(arquivo, "utf8"));
  catalogo.plugins.push({ source: "./plugins/com-ficha" });
  fs.writeFileSync(arquivo, JSON.stringify(catalogo));
  criarPlugin(pasta, "com-ficha", JSON.stringify(fichaModerada()));
  const [primeiro, segundo] = verificarMarketplace(pasta);
  assert.deepEqual(primeiro.erros, []);
  assert.deepEqual(segundo, { plugin: "plugins[1]", erros: ["entrada sem name"] });
});

test("portão chamado por link simbólico roda e imprime o resultado", { skip: process.platform === "win32" }, () => {
  const link = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "portao-link-")), "portao.mjs");
  fs.symlinkSync(portao, link);
  const r = spawnSync(process.execPath, [link, exemplo, "--sem-claude"], { encoding: "utf8" });
  assert.equal(r.status, 1);
  assert.match(r.stdout, /^identificando-tarefas-e-riscos: aprovado$/m);
  assert.match(r.stdout, /^revisando-pull-requests: reprovado$/m);
});
