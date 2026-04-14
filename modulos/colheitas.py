from modulos.talhoes import buscar_talhao_por_id
from datetime import datetime

METODOS_COLHEITA = ("Manual", "Mecânico")

PERDA_REFERENCIA = {
    "Manual": 5.0,
    "Mecânico": 15.0
}


def _validar_float(mensagem, minimo=0.0, maximo=None):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < minimo:
                print(f"Valor mínimo permitido: {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor máximo permitido: {maximo}")
                continue
            return valor
        except ValueError:
            print("Digite um número válido. Exemplo: 150.5")


def _validar_inteiro(mensagem, opcoes=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if opcoes and valor not in opcoes:
                print("Opção inválida. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def calcular_perda(producao_esperada, perda_percentual):
    perda_toneladas = producao_esperada * (perda_percentual / 100)
    producao_real = producao_esperada - perda_toneladas
    return round(perda_toneladas, 2), round(producao_real, 2)


def registrar_colheita(talhoes, colheitas):
    print("(Digite 0 para cancelar)\n")

    talhao_id = input("ID do talhão: ").strip().upper()
    if talhao_id == "0":
        return

    talhao = buscar_talhao_por_id(talhoes, talhao_id)
    if not talhao:
        print("Talhão não encontrado.")
        return

    print(f"Talhão encontrado: {talhao['nome']} ({talhao['area_ha']} ha)\n")

    print("Métodos de colheita:")
    for i, m in enumerate(METODOS_COLHEITA, 1):
        print(f"  [{i}] {m}")
    idx = _validar_inteiro("Escolha o método: ", opcoes=range(1, len(METODOS_COLHEITA) + 1))
    metodo = METODOS_COLHEITA[idx - 1]

    ano_safra = _validar_inteiro("Ano da safra: ", opcoes=range(2000, 2101))
    producao_esperada = _validar_float("Produção esperada (toneladas): ", minimo=0.1)
    
    referencia = PERDA_REFERENCIA[metodo]
    print(f"Referência de perda para colheita {metodo.lower()}: {referencia}%")
    perda_percentual = _validar_float("Percentual de perda observado (%): ", minimo=0.0, maximo=100.0)

    preco_tonelada = _validar_float("Preço por tonelada (R$): ", minimo=0.1)

    perda_toneladas, producao_real = calcular_perda(producao_esperada, perda_percentual)
    prejuizo = round(perda_toneladas * preco_tonelada, 2)

    if perda_percentual > referencia:
        print(f"\nAVISO: Perda acima da referência para colheita {metodo.lower()} ({referencia}%)!")

    print(f"\nResumo:")
    print(f"  Produção esperada : {producao_esperada} t")
    print(f"  Perda             : {perda_toneladas} t ({perda_percentual}%)")
    print(f"  Produção real     : {producao_real} t")
    print(f"  Prejuízo estimado : R$ {prejuizo}")

    confirmacao = input("\nConfirmar registro? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Registro cancelado.")
        return

    colheita = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "talhao_id": talhao_id,
        "talhao_nome": talhao["nome"],
        "ano_safra": ano_safra,
        "metodo": metodo,
        "producao_esperada": producao_esperada,
        "perda_percentual": perda_percentual,
        "perda_toneladas": perda_toneladas,
        "producao_real": producao_real,
        "preco_tonelada": preco_tonelada,
        "prejuizo": prejuizo,
        "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    colheitas.append(colheita)
    print("Colheita registrada com sucesso!")


def listar_colheitas(colheitas):
    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    print(f"\n{'ID':<16} {'Talhão':<20} {'Safra':<6} {'Método':<10} {'Prod.Esp.':<12} {'Perda%':<8} {'Prejuízo'}")
    print("-" * 85)
    for c in colheitas:
        print(f"{c['id']:<16} {c['talhao_nome']:<20} {c['ano_safra']:<6} {c['metodo']:<10} {c['producao_esperada']:<12} {c['perda_percentual']:<8} R$ {c['prejuizo']}")


def colheitas_por_talhao(talhoes, colheitas):
    if not talhoes:
        print("Nenhum talhão cadastrado.")
        return

    listar_colheitas(colheitas)
    talhao_id = input("\nDigite o ID do talhão: ").strip().upper()

    filtradas = [c for c in colheitas if c["talhao_id"] == talhao_id]

    if not filtradas:
        print("Nenhuma colheita encontrada para este talhão.")
        return

    listar_colheitas(filtradas)