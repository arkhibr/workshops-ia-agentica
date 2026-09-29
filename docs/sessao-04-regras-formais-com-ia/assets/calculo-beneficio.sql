-- Artefato didático, sem especificação externa. Os limites 759.00 e 900.00 foram fixados para a aula.
SELECT
    p.pessoa_id,
    COALESCE(c.renda_per_capita, 0) AS renda_considerada,
    CASE
        WHEN p.cpf_regular = 0 THEN 'BLOQUEADO'
        WHEN c.cadastro_ativo = 1 AND COALESCE(c.renda_per_capita, 0) <= 759.00 THEN
            CASE
                WHEN f.categoria IN ('ENERGIA', 'AGUA', 'ESGOTO', 'GAS_CANALIZADO', 'TELECOM')
                    THEN 'DEVOLUCAO_INCISO_I'
                WHEN f.categoria = 'GLP' AND f.peso_kg <= 13
                    THEN 'DEVOLUCAO_INCISO_I'
                WHEN f.imposto_seletivo = 1 THEN 'SEM_DEVOLUCAO'
                ELSE 'DEVOLUCAO_DEMAIS_CASOS'
            END
        WHEN c.cadastro_ativo = 1 AND COALESCE(c.renda_per_capita, 0) <= 900.00
            THEN 'ANALISE_MANUAL'
        ELSE 'SEM_DEVOLUCAO'
    END AS situacao,
    CASE
        WHEN f.categoria IN ('ENERGIA', 'AGUA', 'ESGOTO', 'GAS_CANALIZADO', 'TELECOM')
             OR (f.categoria = 'GLP' AND f.peso_kg <= 13)
            THEN f.valor_cbs
        ELSE f.valor_cbs * 0.20
    END AS devolucao_cbs,
    f.valor_ibs * 0.20 AS devolucao_ibs
FROM pessoa p
INNER JOIN cadastro_familiar c ON c.responsavel_id = p.pessoa_id
LEFT JOIN documento_fiscal f ON f.cpf = p.cpf
WHERE p.residente_brasil = 1
  AND f.consumo_domiciliar = 1
  AND COALESCE(f.cancelado, 0) = 0;
