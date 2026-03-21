from datetime import datetime
from lerbanco import salvar
from registrar_movimentacoes import registrar_movimentacoes

def registrar_saida(estoque, movimentacoes, user, setor):
    produto = input("CÓDIGO/PRODUTO: ")
    quantidade = int(input("Quantidade: "))

    for item, valor in estoque.items():
        if item == produto or valor["produto"] == produto:
            codigo_produto = item

            if item == produto:
                produto = estoque[item]["produto"]

            if valor["quantidade_estoque"] - quantidade >= 0:

                valor["quantidade_estoque"] -= quantidade
                preco = valor["preco"]
                saida = str(datetime.now().strftime("%Y-%m-%d"))
                entrada = None

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

    return
