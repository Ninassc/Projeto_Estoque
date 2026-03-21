def mostrar_movimentacoes(movimentacoes):
    print("\n")
    print("------- MOVIMENTAÇÕES -------")
    print("\n")

    for elemento, itens in movimentacoes.items():
        print(f"Código = {elemento} ")

        for chave, valor in itens.items():
            if isinstance(valor, str):
                valor = valor.upper()
            print(f"{chave.replace('_', ' ').capitalize()} : {valor}")

        print("\n")

    return
