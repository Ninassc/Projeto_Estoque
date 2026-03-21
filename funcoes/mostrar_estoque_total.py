def mostrar_estoque_total(estoque):
    print("\n")
    print("------- ESTOQUE -------")
    print("\n")

    contador = 0
    itens_por_pagina = 5
    total_estoque = len(estoque)

    for elemento, itens in estoque.items():
        print(f"Código = {elemento} ")

        for chave, valor in itens.items():
            if isinstance(valor, str):
                valor = valor.capitalize()
        
            print(f"{chave.replace('_', ' ').capitalize()} : {valor}")

        print("\n")

        contador += 1
        if contador % itens_por_pagina == 0 and contador < total_estoque:
            opcao = input(f"Mostrando {contador} de {total_estoque}. Pressione [Enter] para continuar ou digite 'S' para sair: ")
            if opcao.upper() == 'S':
                print("Saindo da visualização do estoque...\n")
                break

    return
