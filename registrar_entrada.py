from datetime import datetime
from lerbanco import salvar
from registrar_movimentacoes import registrar_movimentacoes
from cadastrar_estoque import cadastrar_estoque

def registrar_entrada(estoque, movimentacoes, user, setor):
    produto = input("CÓDIGO/PRODUTO: ").strip()
    quantidade = int(input("Quantidade: "))

    for item, valor in estoque.items():
        if item == produto or valor["produto"] == produto:
            codigo_produto = item

            if item == produto:
                produto = valor["produto"]

            valor["quantidade_estoque"] += quantidade
            preco = valor["preco"]
            saida = None
            entrada = str(datetime.now().strftime("%Y-%m-%d"))
            registrar_movimentacoes(
                movimentacoes,
                codigo_produto,
                produto,
                quantidade,
                preco,
                user,
                entrada,
                saida,
            )
            salvar()
            break
    else:
        print("PRODUTO não existe no estoque!")
        cadastrar_estoque(estoque, movimentacoes, setor, user)

    return
