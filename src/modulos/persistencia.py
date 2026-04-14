import json
import os
from datetime import datetime

ARQUIVO_JSON = "dados.json"
ARQUIVO_LOG  = "log.txt"


from rich import print as rprint

def salvar_dados(estado):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(estado, f, ensure_ascii=False, indent=4)
    rprint("[bold yellow]Dados salvos com sucesso.[/bold yellow]")


def carregar_dados():
    if not os.path.exists(ARQUIVO_JSON):
        return None

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def registrar_log(historico, mensagem):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    entrada = {"timestamp": timestamp, "mensagem": mensagem}

    historico.append(entrada)

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {mensagem}\n")