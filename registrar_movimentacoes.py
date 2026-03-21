from funcoes_database import calcular_preco_total

def registrar_movimentacoes(
    movimentacoes, codigo_produto, produto, quantidade, preco, user, entrada, saida
):
    num_movimentacao = len(movimentacoes) + 1
    cod_movimentacao = f"MOV{num_movimentacao}"

    movimentacoes[cod_movimentacao] = {
        "codigo_produto": codigo_produto,
        "produto": produto,
        "quantidade": quantidade,
        "preco": preco,
        "total": None,
        "entrada": entrada,
        "saida": saida,
        "funcionario": user,
    }

    calcular_preco_total(movimentacoes)

    return
