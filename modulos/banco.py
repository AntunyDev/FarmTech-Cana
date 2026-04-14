import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DSN      = os.getenv("DB_DSN")


def conectar():
    try:
        conexao = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
        return conexao
    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar no banco: {e}")
        return None


def inicializar_banco():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE talhoes (
                        id           VARCHAR2(8)   PRIMARY KEY,
                        nome         VARCHAR2(100) NOT NULL,
                        area_ha      NUMBER(10,2)  NOT NULL,
                        variedade    VARCHAR2(50),
                        municipio    VARCHAR2(100),
                        ano_plantio  NUMBER(4)
                    )';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN RAISE; END IF;
            END;
        """
        )

        cursor.execute(
            """
            BEGIN
                EXECUTE IMMEDIATE '
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
                    )';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN RAISE; END IF;
            END;
        """
        )

        conexao.commit()
        print("Banco inicializado com sucesso.")

    except oracledb.DatabaseError as e:
        print(f"Erro ao inicializar banco: {e}")
    finally:
        conexao.close()


def salvar_talhao(talhao):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            MERGE INTO talhoes t
            USING (SELECT :id AS id FROM dual) src
            ON (t.id = src.id)
            WHEN MATCHED THEN
                UPDATE SET nome = :nome, area_ha = :area_ha,
                           variedade = :variedade, municipio = :municipio,
                           ano_plantio = :ano_plantio
            WHEN NOT MATCHED THEN
                INSERT (id, nome, area_ha, variedade, municipio, ano_plantio)
                VALUES (:id, :nome, :area_ha, :variedade, :municipio, :ano_plantio)
        """,
            {
                "id": talhao["id"],
                "nome": talhao["nome"],
                "area_ha": talhao["area_ha"],
                "variedade": talhao["variedade"],
                "municipio": talhao["municipio"],
                "ano_plantio": talhao["ano_plantio"],
            },
        )
        conexao.commit()
        print("Talhão salvo no banco.")

    except oracledb.DatabaseError as e:
        print(f"Erro ao salvar talhão: {e}")
    finally:
        conexao.close()


def salvar_colheita(colheita):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            MERGE INTO colheitas c
            USING (SELECT :id AS id FROM dual) src
            ON (c.id = src.id)
            WHEN MATCHED THEN
                UPDATE SET perda_percentual = :perda_percentual,
                           perda_toneladas  = :perda_toneladas,
                           prejuizo         = :prejuizo
            WHEN NOT MATCHED THEN
                INSERT (id, talhao_id, talhao_nome, ano_safra, metodo,
                        producao_esperada, perda_percentual, perda_toneladas,
                        producao_real, preco_tonelada, prejuizo, data_registro)
                VALUES (:id, :talhao_id, :talhao_nome, :ano_safra, :metodo,
                        :producao_esperada, :perda_percentual, :perda_toneladas,
                        :producao_real, :preco_tonelada, :prejuizo, :data_registro)
        """,
            {
                "id": colheita["id"],
                "talhao_id": colheita["talhao_id"],
                "talhao_nome": colheita["talhao_nome"],
                "ano_safra": colheita["ano_safra"],
                "metodo": colheita["metodo"],
                "producao_esperada": colheita["producao_esperada"],
                "perda_percentual": colheita["perda_percentual"],
                "perda_toneladas": colheita["perda_toneladas"],
                "producao_real": colheita["producao_real"],
                "preco_tonelada": colheita["preco_tonelada"],
                "prejuizo": colheita["prejuizo"],
                "data_registro": colheita["data_registro"],
            },
        )
        conexao.commit()
        print("Colheita salva no banco.")

    except oracledb.DatabaseError as e:
        print(f"Erro ao salvar colheita: {e}")
    finally:
        conexao.close()


def listar_talhoes_bd():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome, area_ha, variedade, municipio, ano_plantio FROM talhoes ORDER BY nome"
        )
        linhas = cursor.fetchall()

        if not linhas:
            print("Nenhum talhão no banco de dados.")
            return

        print(
            f"\n{'ID':<10} {'Nome':<20} {'Área':<10} {'Variedade':<12} {'Município':<20} {'Plantio'}"
        )
        print("-" * 80)
        for linha in linhas:
            print(
                f"{linha[0]:<10} {linha[1]:<20} {linha[2]:<10} {linha[3]:<12} {linha[4]:<20} {linha[5]}"
            )

    except oracledb.DatabaseError as e:
        print(f"Erro ao consultar talhões: {e}")
    finally:
        conexao.close()


def listar_colheitas_bd():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            SELECT id, talhao_nome, ano_safra, metodo,
                   producao_esperada, perda_percentual, prejuizo
            FROM colheitas
            ORDER BY ano_safra DESC
        """
        )
        linhas = cursor.fetchall()

        if not linhas:
            print("Nenhuma colheita no banco de dados.")
            return

        print(
            f"\n{'ID':<16} {'Talhão':<20} {'Safra':<6} {'Método':<10} {'Prod.Esp.':<12} {'Perda%':<8} {'Prejuízo'}"
        )
        print("-" * 85)
        for linha in linhas:
            print(
                f"{linha[0]:<16} {linha[1]:<20} {linha[2]:<6} {linha[3]:<10} {linha[4]:<12} {linha[5]:<8} R$ {linha[6]:.2f}"
            )

    except oracledb.DatabaseError as e:
        print(f"Erro ao consultar colheitas: {e}")
    finally:
        conexao.close()
