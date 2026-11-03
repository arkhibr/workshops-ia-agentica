import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const DADOS = ["publico", "interno", "pessoal", "sensivel"];
const AUTONOMIAS = ["sugere", "prepara", "executa"];
const FAIXAS = ["baixa", "moderada", "alta"];
const TIPOS = ["permissao", "hook", "validacao", "politica-api", "revisao-humana", "instrucao"];
const TEXTOS = ["dono", "finalidade", "alternativaSemIA", "fatorDecisivo"];
const vazio = (v) => typeof v !== "string" || v.trim() === "";
const lista = (v) => Array.isArray(v) && v.length > 0 && v.every((i) => typeof i === "string" && i.trim() !== "");

export function verificarFicha(ficha) {
  if (ficha === null || typeof ficha !== "object" || Array.isArray(ficha)) return ["ficha: esperado um objeto"];
  const erros = [];
  for (const campo of TEXTOS) if (vazio(ficha[campo])) erros.push(`${campo}: campo obrigatório vazio`);
  for (const campo of ["dados", "ferramentas", "premissas"]) {
    if (!Array.isArray(ficha[campo])) erros.push(`${campo}: esperado uma lista`);
    else if (!lista(ficha[campo])) erros.push(`${campo}: campo obrigatório vazio`);
  }
  if (Array.isArray(ficha.dados) && ficha.dados.some((d) => !DADOS.includes(d)))
    erros.push(`dados: valores aceitos são ${DADOS.join(", ")}`);
  if (!AUTONOMIAS.includes(ficha.autonomia)) erros.push(`autonomia: valores aceitos são ${AUTONOMIAS.join(", ")}`);
  if (!FAIXAS.includes(ficha.faixa)) erros.push(`faixa: valores aceitos são ${FAIXAS.join(", ")}`);
  if (Array.isArray(ficha.dados) && ficha.dados.includes("sensivel") && ficha.faixa !== "alta")
    erros.push("faixa: dado sensível leva à faixa alta");
  if (ficha.autonomia === "executa" && ficha.faixa !== "alta")
    erros.push("faixa: autonomia executa leva à faixa alta");
  if (ficha.faixa === "alta" && (vazio(ficha.gate?.aprovador) || vazio(ficha.gate?.aprovadoEm)))
    erros.push("gate: faixa alta exige aprovador e data de aprovação");
  if (!Array.isArray(ficha.riscos) || ficha.riscos.length === 0) erros.push("riscos: esperado uma lista com ao menos um risco");
  else
    ficha.riscos.forEach((risco, i) => {
      const id = `riscos[${i}]`;
      for (const campo of ["evento", "consequencia", "detectivo", "evidencia"])
        if (vazio(risco?.[campo])) erros.push(`${id}.${campo}: campo obrigatório vazio`);
      if (vazio(risco?.preventivo?.descricao)) erros.push(`${id}.preventivo: campo obrigatório vazio`);
      else if (!TIPOS.includes(risco.preventivo.tipo))
        erros.push(`${id}.preventivo.tipo: valores aceitos são ${TIPOS.join(", ")}`);
      else if (risco.preventivo.tipo === "instrucao")
        erros.push(`${id}: controle preventivo depende só de instrução ao modelo`);
    });
  if (!lista(ficha.revisao?.gatilhos)) erros.push("revisao.gatilhos: esperado uma lista");
  if (vazio(ficha.revisao?.retirada)) erros.push("revisao.retirada: campo obrigatório vazio");
  return erros;
}

// Editores do Windows podem gravar o BOM no início do arquivo, e o JSON.parse o recusa.
const lerJson = (arquivo) => JSON.parse(fs.readFileSync(arquivo, "utf8").replace(/^\uFEFF/, ""));

function lerCatalogo(pasta) {
  const arquivo = path.join(pasta, ".claude-plugin", "marketplace.json");
  if (!fs.existsSync(arquivo)) throw new Error(`marketplace.json: arquivo ausente em ${arquivo}`);
  let catalogo;
  try {
    catalogo = lerJson(arquivo);
  } catch (e) {
    throw new Error(`marketplace.json: JSON inválido (${e.message})`);
  }
  if (!Array.isArray(catalogo?.plugins)) throw new Error("marketplace.json: plugins: esperado uma lista");
  return catalogo;
}

export function verificarMarketplace(pasta) {
  return lerCatalogo(pasta).plugins.map((entrada, i) => {
    if (entrada === null || typeof entrada !== "object")
      return { plugin: `plugins[${i}]`, erros: ["entrada: esperado um objeto com name e source"] };
    if (vazio(entrada.name)) return { plugin: `plugins[${i}]`, erros: ["entrada sem name"] };
    if (typeof entrada.source !== "string")
      return { plugin: entrada.name, erros: [], aviso: "fonte remota: ficha não verificada localmente" };
    const arquivo = path.join(pasta, entrada.source, "governanca.json");
    if (!fs.existsSync(arquivo)) return { plugin: entrada.name, erros: ["governanca.json: arquivo ausente"] };
    try {
      return { plugin: entrada.name, erros: verificarFicha(lerJson(arquivo)) };
    } catch (e) {
      return { plugin: entrada.name, erros: [`governanca.json: JSON inválido (${e.message})`] };
    }
  });
}

// No Windows o shell encontra o claude instalado como .cmd, e as aspas mantêm inteiro um caminho com espaço.
// O resolve tira a barra final, que antes da aspa de fechamento formaria \" e quebraria o argumento.
export function argumentosDoValidate(pasta, plataforma = process.platform) {
  if (plataforma === "win32")
    return [`claude plugin validate "${path.win32.resolve(pasta)}"`, [], { stdio: "inherit", shell: true }];
  return ["claude", ["plugin", "validate", pasta], { stdio: "inherit", shell: false }];
}

const VERSAO_MINIMA = "2.1.317";

// O realpath dos dois lados reconhece a execução direta também por link simbólico ou caminho relativo.
function execucaoDireta() {
  try {
    return fs.realpathSync(process.argv[1]) === fs.realpathSync(fileURLToPath(import.meta.url));
  } catch {
    return false;
  }
}

if (execucaoDireta()) {
  const [pasta, ...opcoes] = process.argv.slice(2);
  if (!pasta) {
    console.error("uso: node portao.mjs <pasta-do-marketplace> [--sem-claude]");
    process.exit(2);
  }
  let resultado;
  try {
    resultado = verificarMarketplace(pasta);
  } catch (e) {
    console.error(`portão: ${e.message}`);
    process.exit(2);
  }
  for (const { plugin, erros, aviso } of resultado) {
    console.log(`${plugin}: ${erros.length ? "reprovado" : "aprovado"}`);
    for (const erro of erros) console.log(`  - ${erro}`);
    if (aviso) console.log(`  aviso: ${aviso}`);
  }
  if (resultado.some((r) => r.erros.length)) process.exit(1);
  if (!opcoes.includes("--sem-claude")) {
    const r = spawnSync(...argumentosDoValidate(pasta));
    // Sem o claude, o spawnSync devolve error no macOS e no Linux, e o cmd.exe do Windows sai com 9009.
    if (r.error || (process.platform === "win32" && r.status === 9009)) {
      console.error(`portão: o comando claude não foi encontrado. Instale o Claude Code ${VERSAO_MINIMA} ou superior, ou rode com --sem-claude.`);
      process.exit(2);
    }
    process.exit(r.status ?? 1);
  }
}
