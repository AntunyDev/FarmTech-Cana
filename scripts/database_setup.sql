-- FARMTECH CANA - Scripts de Inicialização do Banco de Dados Oracle

-- 1. Criação da Tabela de Talhões
CREATE TABLE talhoes (
    id           VARCHAR2(8)   PRIMARY KEY,
    nome         VARCHAR2(100) NOT NULL,
    area_ha      NUMBER(10,2)  NOT NULL,
    variedade    VARCHAR2(50),
    municipio    VARCHAR2(100),
    ano_plantio  NUMBER(4)
);

-- 2. Criação da Tabela de Colheitas
CREATE TABLE colheitas (
    id                  VARCHAR2(20)  PRIMARY KEY,
    talhao_id           VARCHAR2(8)   REFERENCES talhoes(id),
    talhao_nome         VARCHAR2(100),
    ano_safra           NUMBER(4),
    metodo              VARCHAR2(20),
    producao_esperada   NUMBER(12,2),
    perda_percentual    NUMBER(5,2),
    perda_toneladas     NUMBER(12,2),
    producao_real       NUMBER(12,2),
    preco_tonelada      NUMBER(10,2),
    prejuizo            NUMBER(14,2),
    data_registro       VARCHAR2(20)
);

-- Notas:
-- O sistema Python executa automaticamente estes scripts (MERGE) para garantir a integridade.
