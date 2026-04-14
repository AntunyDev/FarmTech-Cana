def relatorio_perdas_geral(colheitas):
    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    total_esperado = sum(c["producao_esperada"] for c in colheitas)
    total_perda    = sum(c["perda_toneladas"]   for c in colheitas)
    total_real     = sum(c["producao_real"]      for c in colheitas)
    total_prejuizo = sum(c["prejuizo"]           for c in colheitas)
    media_perda    = (total_perda / total_esperado) * 100

    print("\n--- RELATÓRIO GERAL DE PERDAS ---")
    print(f"Produção esperada total : {total_esperado:.2f} t")
    print(f"Produção real total     : {total_real:.2f} t")
    print(f"Perda total             : {total_perda:.2f} t")
    print(f"Média de perda          : {media_perda:.2f}%")
    print(f"Prejuízo total          : R$ {total_prejuizo:.2f}")


def relatorio_por_metodo(colheitas):
    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    grupos = {}
    for c in colheitas:
        metodo = c["metodo"]
        if metodo not in grupos:
            grupos[metodo] = {
                "quantidade": 0,
                "total_esperado": 0.0,
                "total_perda": 0.0,
                "total_prejuizo": 0.0
            }
        grupos[metodo]["quantidade"]      += 1
        grupos[metodo]["total_esperado"]  += c["producao_esperada"]
        grupos[metodo]["total_perda"]     += c["perda_toneladas"]
        grupos[metodo]["total_prejuizo"]  += c["prejuizo"]

    print("\n--- COMPARATIVO: MANUAL vs MECÂNICO ---")
    for metodo, dados in grupos.items():
        media = (dados["total_perda"] / dados["total_esperado"]) * 100
        print(f"\nMétodo: {metodo}")
        print(f"  Colheitas registradas : {dados['quantidade']}")
        print(f"  Produção esperada     : {dados['total_esperado']:.2f} t")
        print(f"  Perda total           : {dados['total_perda']:.2f} t")
        print(f"  Média de perda        : {media:.2f}%")
        print(f"  Prejuízo total        : R$ {dados['total_prejuizo']:.2f}")


def relatorio_prejuizo(colheitas):
    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    top5 = sorted(colheitas, key=lambda c: c["prejuizo"], reverse=True)[:5]

    print("\n--- TOP 5 MAIORES PREJUÍZOS ---")
    print(f"\n{'Talhão':<20} {'Safra':<6} {'Método':<10} {'Perda%':<8} {'Prejuízo'}")
    print("-" * 60)
    for c in top5:
        print(f"{c['talhao_nome']:<20} {c['ano_safra']:<6} {c['metodo']:<10} {c['perda_percentual']:<8} R$ {c['prejuizo']:.2f}")