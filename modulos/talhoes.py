import uuid # Biblioteca para gerar identificadores únicos

VARIEDADES_CANA = (
    "RB867515", "RB92579", "SP81-3250",
    "RB966928", "CTC4", "CTC9001", "Outra"
)


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
            print("Digite um número válido. Exemplo: 12.5")


def _validar_inteiro(mensagem, opcoes=None, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if opcoes and valor not in opcoes:
                print("Opção inválida. Tente novamente.")
                continue
            if minimo is not None and valor < minimo:
                print(f"Valor mínimo permitido: {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor máximo permitido: {maximo}")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")

def cadastrar_talhao(talhoes):
    print("(Digite 0 para cancelar)\n")

    nome = input("Nome do talhão: ").strip()
    if nome == "0":
        return None
    if not nome:
        print("O nome não pode ser vazio.")
        return None

    for t in talhoes.values():
        if t["nome"].lower() == nome.lower():
            print("Já existe um talhão com este nome.")
            return None

    area = _validar_float("Área (hectares): ", minimo=0.1, maximo=10000.0)

    print("\nVariedades disponíveis:")
    for i, v in enumerate(VARIEDADES_CANA, 1):
        print(f"  [{i}] {v}")
    idx = _validar_inteiro("Escolha a variedade: ", opcoes=range(1, len(VARIEDADES_CANA) + 1))
    variedade = VARIEDADES_CANA[idx - 1]

    municipio = input("Município/Estado: ").strip()
    if not municipio:
        municipio = "Não informado"

    ano_plantio = _validar_inteiro("Ano de plantio: ", minimo=1990, maximo=2100)

    talhao_id = str(uuid.uuid4())[:8].upper()

    talhao = {
        "id": talhao_id,
        "nome": nome,
        "area_ha": area,
        "variedade": variedade,
        "municipio": municipio,
        "ano_plantio": ano_plantio
    }

    talhoes[talhao_id] = talhao
    return talhao


def listar_talhoes(talhoes):
    if not talhoes:
        print("Nenhum talhão cadastrado.")
        return

    print(f"\n{'ID':<10} {'Nome':<20} {'Área (ha)':<12} {'Variedade':<12} {'Município':<20} {'Plantio'}")
    print("-" * 80)
    for t in talhoes.values():
        print(f"{t['id']:<10} {t['nome']:<20} {t['area_ha']:<12} {t['variedade']:<12} {t['municipio']:<20} {t['ano_plantio']}")


def buscar_talhao_por_id(talhoes, talhao_id):
    return talhoes.get(talhao_id.upper())


def remover_talhao(talhoes):
    if not talhoes:
        print("Nenhum talhão cadastrado.")
        return

    listar_talhoes(talhoes)
    talhao_id = input("\nDigite o ID do talhão a remover: ").strip().upper()
    talhao = buscar_talhao_por_id(talhoes, talhao_id)

    if not talhao:
        print("Talhão não encontrado.")
        return

    confirmacao = input(f"Confirmar remoção de '{talhao['nome']}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        del talhoes[talhao_id]
        print("Talhão removido com sucesso.")
    else:
        print("Operação cancelada.")