

-- Query para as 10 operadoras com maiores despesas na categoria no último ano (últimos 3 meses)
SELECT 
    o.razao_social,
    o.nome_fantasia,
    o.registro_ans,
    SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS total_despesa
FROM demo_contabeis dc
JOIN operadoras o 
    ON dc.reg_ans = o.registro_ans
WHERE dc.descricao ILIKE 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
  AND EXTRACT(YEAR FROM dc.data)::INTEGER = (SELECT MAX(EXTRACT(YEAR FROM data))::INTEGER FROM demo_contabeis)
  AND EXTRACT(MONTH FROM dc.data)::INTEGER BETWEEN 10 AND 12
GROUP BY o.nome_fantasia, o.registro_ans, o.razao_social
ORDER BY total_despesa DESC
LIMIT 10;

-- Query para as 10 operadoras com maiores despesas na categoria no último ano

SELECT 
    o.nome_fantasia,
    o.registro_ans,
    SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS total_despesa
FROM demo_contabeis dc
JOIN operadoras o 
    ON dc.reg_ans = o.registro_ans
WHERE dc.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
  AND EXTRACT(YEAR FROM dc.data)::INTEGER = (SELECT MAX(EXTRACT(YEAR FROM data))::INTEGER FROM demo_contabeis)
GROUP BY o.nome_fantasia, o.registro_ans
ORDER BY total_despesa DESC
LIMIT 10;
