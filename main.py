from modulos.talhoes import cadastrar_talhao, listar_talhoes, remover_talhao
from modulos.colheitas import registrar_colheita, listar_colheitas, colheitas_por_talhao
from modulos.relatorios import relatorio_perdas_geral, relatorio_por_metodo, relatorio_prejuizo
from modulos.persistencia import salvar_dados, carregar_dados, registrar_log
from modulos.banco import inicializar_banco, salvar_talhao, salvar_colheita, listar_talhoes_bd, listar_colheitas_bd

estado = {
    "talhoes": {},
    "colheitas": [],
    "historico": []
}


def menu_talhoes():
    while True:
        print("\n--- GESTÃO DE TALHÕES ---")
        print("[1] Cadastrar talhão")
        print("[2] Listar talhões")
        print("[3] Remover talhão")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            talhao = cadastrar_talhao(estado["talhoes"])
            if talhao:
                salvar_talhao(talhao)
                salvar_dados(estado)
                registrar_log(estado["historico"], f"Talhão '{talhao['nome']}' cadastrado.")

        elif opcao == "2":
            listar_talhoes(estado["talhoes"])

        elif opcao == "3":
            remover_talhao(estado["talhoes"])
            salvar_dados(estado)
            registrar_log(estado["historico"], "Talhão removido.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_colheitas():
    while True:
        print("\n--- REGISTRO DE COLHEITAS ---")
        print("[1] Registrar colheita")
        print("[2] Listar todas as colheitas")
        print("[3] Colheitas por talhão")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            registrar_colheita(estado["talhoes"], estado["colheitas"])
            if estado["colheitas"]:
                salvar_colheita(estado["colheitas"][-1])
            salvar_dados(estado)
            registrar_log(estado["historico"], "Colheita registrada.")

        elif opcao == "2":
            listar_colheitas(estado["colheitas"])

        elif opcao == "3":
            colheitas_por_talhao(estado["talhoes"], estado["colheitas"])

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_relatorios():
    while True:
        print("\n--- RELATÓRIOS ---")
        print("[1] Relatório geral de perdas")
        print("[2] Comparativo manual vs mecânico")
        print("[3] Top 5 maiores prejuízos")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            relatorio_perdas_geral(estado["colheitas"])

        elif opcao == "2":
            relatorio_por_metodo(estado["colheitas"])

        elif opcao == "3":
            relatorio_prejuizo(estado["colheitas"])

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_banco():
    while True:
        print("\n--- BANCO DE DADOS ORACLE ---")
        print("[1] Consultar talhões")
        print("[2] Consultar colheitas")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            listar_talhoes_bd()

        elif opcao == "2":
            listar_colheitas_bd()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("\n=== FarmTech Cana ===")
        print("[1] Gestão de Talhões")
        print("[2] Registro de Colheitas")
        print("[3] Relatórios")
        print("[4] Banco de Dados Oracle")
        print("[5] Histórico de operações")
        print("[0] Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            menu_talhoes()

        elif opcao == "2":
            menu_colheitas()

        elif opcao == "3":
            menu_relatorios()

        elif opcao == "4":
            menu_banco()

        elif opcao == "5":
            if not estado["historico"]:
                print("Nenhuma operação registrada.")
            else:
                print("\n--- HISTÓRICO ---")
                for entrada in estado["historico"]:
                    print(f"{entrada['timestamp']}  {entrada['mensagem']}")

        elif opcao == "0":
            salvar_dados(estado)
            print("Dados salvos. Até logo!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    inicializar_banco()

    dados_salvos = carregar_dados()
    if dados_salvos:
        estado["talhoes"]   = dados_salvos.get("talhoes", {})
        estado["colheitas"] = dados_salvos.get("colheitas", [])
        estado["historico"] = dados_salvos.get("historico", [])

    menu_principal()