-- conectando ao banco de dados
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

-- Criação da tabela de demonstrações contábeis

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




