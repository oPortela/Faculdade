CREATE TABLE clientefisico (
    clientes_codcliente NUMBER(18) NOT NULL,
    cpf                 VARCHAR2(11 CHAR) NOT NULL
);

CREATE UNIQUE INDEX clientefisico__idx ON
    clientefisico (
        clientes_codcliente
    ASC );

ALTER TABLE clientefisico ADD CONSTRAINT clientefisico_pk PRIMARY KEY ( cpf,
                                                                        clientes_codcliente );

CREATE TABLE clientejuridico (
    clientes_codcliente NUMBER(18) NOT NULL,
    cnpj                VARCHAR2(14 CHAR) NOT NULL,
    incricaoestadual    VARCHAR2(20 CHAR) NOT NULL
);

CREATE UNIQUE INDEX clientejuridico__idx ON
    clientejuridico (
        clientes_codcliente
    ASC );

ALTER TABLE clientejuridico ADD CONSTRAINT clientejuridico_pk PRIMARY KEY ( cnpj,
                                                                            clientes_codcliente );

CREATE TABLE clientes (
    codcliente           NUMBER(18) NOT NULL,
    cliente              VARCHAR2(400 CHAR) NOT NULL,
    fantasia             VARCHAR2(400) NOT NULL,
    datacadastro         DATE NOT NULL,
    email                VARCHAR2(100 CHAR) NOT NULL,
    tipopessoa           CHAR(1 CHAR) CHECK (tipoPessoa IN ('F', 'J')) NOT NULL,
    telefone_codtelefone NUMBER(18) NOT NULL,
    endereco_codendereco NUMBER(18) NOT NULL
);

CREATE UNIQUE INDEX clientes__idx ON
    clientes (
        endereco_codendereco
    ASC );

CREATE UNIQUE INDEX clientes__idxv1 ON
    clientes (
        telefone_codtelefone
    ASC );

ALTER TABLE clientes ADD CONSTRAINT clientes_pk PRIMARY KEY ( codcliente );

CREATE TABLE empregados (
    codempr      NUMBER(18) NOT NULL,
    nome         VARCHAR2(200 CHAR) NOT NULL,
    cpf          VARCHAR2(11 CHAR) NOT NULL,
    dtinicio     DATE NOT NULL,
    dtfim        DATE,
    dtnascimento DATE NOT NULL,
    codtelefone  NUMBER(18) NOT NULL,
    email        VARCHAR2(100),
    codendereco  NUMBER(18) NOT NULL,
    obs          VARCHAR2(300 CHAR)
);

ALTER TABLE empregados ADD CONSTRAINT empregados_pk PRIMARY KEY ( codempr );

CREATE TABLE endereco (
    codendereco NUMBER(18) NOT NULL,
    logradouro  VARCHAR2(400 CHAR) NOT NULL,
    numero      VARCHAR2(10 BYTE),
    cep         VARCHAR2(9 BYTE) NOT NULL,
    bairro      VARCHAR2(100 BYTE) NOT NULL,
    cidade      VARCHAR2(50 BYTE) NOT NULL,
    estado      VARCHAR2(2 BYTE) NOT NULL,
    pais        VARCHAR2(2 BYTE) NOT NULL
);

ALTER TABLE endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( codendereco );

CREATE TABLE fornecedor (
    codfornec          NUMBER(18) NOT NULL,
    fornecedor         VARCHAR2(200 CHAR) NOT NULL,
    fantasia           VARCHAR2(200 CHAR) NOT NULL,
    dtcadastro         DATE NOT NULL,
    codtelefone        NUMBER(18) NOT NULL,
    email              VARCHAR2(100 CHAR) NOT NULL,
    codendereco        NUMBER(18) NOT NULL,
    nomerepresentante  VARCHAR2(200 CHAR) NOT NULL,
    emailrepresentante VARCHAR2(100 CHAR) NOT NULL,
    telrepresentante   VARCHAR2(20) NOT NULL
);

ALTER TABLE fornecedor ADD CONSTRAINT fornecedor_pk PRIMARY KEY ( codfornec );

CREATE TABLE pedidoc (
    numped              NUMBER(18) NOT NULL,
    data                DATE NOT NULL,
    clientes_codcliente NUMBER(18) NOT NULL,
    empregados_codempr  NUMBER(18) NOT NULL,
    mediadesc           NUMBER NOT NULL,
    vltotal             NUMBER(18, 4) NOT NULL
);

ALTER TABLE pedidoc ADD CONSTRAINT pedidoc_pk PRIMARY KEY ( numped );

CREATE TABLE pedidoi (
    numped         NUMBER(18) NOT NULL,
    data           DATE,
    codcliente     NUMBER(18) NOT NULL,
    codproduto     NUMBER(18) NOT NULL,
    quantidade     NUMBER(18) NOT NULL,
    desconto       NUMBER(18, 4) NOT NULL,
    vlunit         NUMBER(18, 4) NOT NULL,
    vltotal        NUMBER(18, 4) NOT NULL,
    pedidoc_numped NUMBER(18) NOT NULL
);

ALTER TABLE pedidoi ADD CONSTRAINT pedidoi_pk PRIMARY KEY ( numped );

CREATE TABLE produtos (
    codproduto NUMBER(18) NOT NULL,
    descricao  VARCHAR2(400 CHAR) NOT NULL,
    vlunit     NUMBER(18, 4) NOT NULL,
    embalagem  VARCHAR2(40 CHAR) NOT NULL,
    gtin       VARCHAR2(2 CHAR) NOT NULL,
    ean        VARCHAR2(20 CHAR) NOT NULL,
    codfornec  NUMBER(18) NOT NULL
);

ALTER TABLE produtos ADD CONSTRAINT produtos_pk PRIMARY KEY ( codproduto );

CREATE TABLE telefone (
    codtelefone NUMBER(18) NOT NULL,
    telefone    VARCHAR2(15 CHAR),
    celular     VARCHAR2(15 CHAR),
    fax         VARCHAR2(15)
);

ALTER TABLE telefone ADD CONSTRAINT telefone_pk PRIMARY KEY ( codtelefone );

ALTER TABLE clientefisico
    ADD CONSTRAINT clientefisico_clientes_fk FOREIGN KEY ( clientes_codcliente )
        REFERENCES clientes ( codcliente );

ALTER TABLE clientejuridico
    ADD CONSTRAINT clientejuridico_clientes_fk FOREIGN KEY ( clientes_codcliente )
        REFERENCES clientes ( codcliente );

ALTER TABLE clientes
    ADD CONSTRAINT clientes_endereco_fk FOREIGN KEY ( endereco_codendereco )
        REFERENCES endereco ( codendereco );

ALTER TABLE clientes
    ADD CONSTRAINT clientes_telefone_fk FOREIGN KEY ( telefone_codtelefone )
        REFERENCES telefone ( codtelefone );

ALTER TABLE empregados
    ADD CONSTRAINT empregados_endereco_fk FOREIGN KEY ( codendereco )
        REFERENCES endereco ( codendereco );

ALTER TABLE empregados
    ADD CONSTRAINT empregados_telefone_fk FOREIGN KEY ( codtelefone )
        REFERENCES telefone ( codtelefone );

ALTER TABLE fornecedor
    ADD CONSTRAINT fornecedor_endereco_fk FOREIGN KEY ( codendereco )
        REFERENCES endereco ( codendereco );

ALTER TABLE fornecedor
    ADD CONSTRAINT fornecedor_telefone_fk FOREIGN KEY ( codtelefone )
        REFERENCES telefone ( codtelefone );

ALTER TABLE pedidoc
    ADD CONSTRAINT pedidoc_clientes_fk FOREIGN KEY ( clientes_codcliente )
        REFERENCES clientes ( codcliente );

ALTER TABLE pedidoc
    ADD CONSTRAINT pedidoc_empregados_fk FOREIGN KEY ( empregados_codempr )
        REFERENCES empregados ( codempr );

ALTER TABLE pedidoi
    ADD CONSTRAINT pedidoi_clientes_fk FOREIGN KEY ( codcliente )
        REFERENCES clientes ( codcliente );

ALTER TABLE pedidoi
    ADD CONSTRAINT pedidoi_pedidoc_fk FOREIGN KEY ( pedidoc_numped )
        REFERENCES pedidoc ( numped );

ALTER TABLE pedidoi
    ADD CONSTRAINT pedidoi_produtos_fk FOREIGN KEY ( codproduto )
        REFERENCES produtos ( codproduto );

ALTER TABLE produtos
    ADD CONSTRAINT produtos_fornecedor_fk FOREIGN KEY ( codfornec )
        REFERENCES fornecedor ( codfornec );

CREATE OR REPLACE TRIGGER fknto_pedidoc BEFORE
    UPDATE OF empregados_codempr ON pedidoc
    FOR EACH ROW
BEGIN
    IF :old.empregados_codempr IS NOT NULL THEN
        raise_application_error(-20225, 'Non Transferable FK constraint Pedidoc_empregados_FK on table Pedidoc is violated');
    END IF;
END;
/