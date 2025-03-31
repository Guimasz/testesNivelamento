
CREATE DATABASE ans_dados
    WITH 
    ENCODING = 'UTF8';

\connect ans_dados
   

-- Criação da tabela de operadoras

CREATE TABLE IF NOT EXISTS operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20) NOT NULL,
    razao_social VARCHAR(255) ,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(50) NOT NULL,
    logradouro VARCHAR(255) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    complemento VARCHAR(255),
    bairro VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    ddd VARCHAR(5) ,
    telefone VARCHAR(20) ,
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255) ,
    representante VARCHAR(255) NOT NULL,
    cargo_representante VARCHAR(255) ,
    regiao_de_comercializacao VARCHAR(2) ,
    data_registro_ans DATE NOT NULL
);

-- Criação da tabela definitiva de demonstrações contábeis

CREATE TABLE IF NOT EXISTS demo_contabeis (
    data DATE NOT NULL,
    reg_ans VARCHAR(20) NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial DECIMAL(15, 2) NOT NULL,
    vl_saldo_final DECIMAL(15, 2) NOT NULL,
    PRIMARY KEY (data, reg_ans, cd_conta_contabil),
    CONSTRAINT fk_operadora FOREIGN KEY (reg_ans)
        REFERENCES operadoras(registro_ans)
);

-- Criação da tabela de staging para as demonstrações contábeis

CREATE TABLE IF NOT EXISTS demo_contabeis_stg(
    data DATE NOT NULL,
    reg_ans VARCHAR(20) NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial DECIMAL(15, 2) NOT NULL,
    vl_saldo_final DECIMAL(15, 2) NOT NULL,
    PRIMARY KEY (data, reg_ans, cd_conta_contabil)
);

-- copiando dados para a tabela de staging
\copy operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans) FROM 'downloads/link2/Health_Plan_Operators_Report.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2023/1T2023.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2023/2T2023.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2023/3T2023.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2023/4T2023.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2024/1T2024.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2024/2T2024.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2024/3T2024.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demo_contabeis_stg(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'downloads/link1/2024/4T2024.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

--inserindo apenas dados que tem correspondência na tabela de operadoras na tabela definitiva

INSERT INTO demo_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SELECT s.data, s.reg_ans, s.cd_conta_contabil, s.descricao, s.vl_saldo_inicial, s.vl_saldo_final
FROM demo_contabeis_stg as s
WHERE s.reg_ans IN (SELECT registro_ans FROM operadoras);

DROP TABLE IF EXISTS demo_contabeis_stg;



