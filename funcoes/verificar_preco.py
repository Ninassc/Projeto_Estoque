def verificar_preco(estoque):
    produto = input("CÓDIGO/PRODUTO: ").strip()
    for item, valor in estoque.items():
        if item == produto or valor["produto"] == produto:
            print(f"Preço do produto {valor['produto']}: {valor['preco']} \nQuantidade em estoque: {valor['quantidade_estoque']}")
            break
    else:
        print("PRODUTO não existe no estoque!")
