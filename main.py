from database import movimentacoes, estoque, login_funcionario
from datetime import datetime


def mostrar_estoque_total(estoque):
    print("\n")
    print("------- ESTOQUE -------")
    print("\n")

    for elemento, itens in estoque.items():
        print(f"Código = {elemento} ")

        for chave, valor in itens.items():
            if isinstance(valor, str):
                valor = valor.capitalize()
            print(f"{chave.replace('_', " ").capitalize()} : {valor}")

        print("\n")

    return


def mostrar_movimentacoes(movimentacoes):
    print("\n")
    print("------- MOVIMENTAÇÕES -------")
    print("\n")

    for elemento, itens in movimentacoes.items():
        print(f"Código = {elemento} ")

        for chave, valor in itens.items():
            if isinstance(valor, str):
                valor = valor.upper()
            print(f"{chave.replace('_', " ").capitalize()} : {valor}")

        print("\n")

    return


def registrar_movimentacoes(
    movimentacoes, codigo_produto, produto, quantidade, valor, user, entrada, saida
):
    num_movimentacao = len(movimentacoes) + 1
    cod_movimentacao = f"MOV{num_movimentacao}"

    movimentacoes[cod_movimentacao] = {
        "codigo_produto": codigo_produto,
        "produto": produto,
        "quantidade": quantidade,
        "preco": valor["preco"],
        "total": None,
        "entrada": entrada,
        "saida": saida,
        "funcionario": user,
    }

    return


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
                saida = str(datetime.now().strftime("%Y-%m-%d"))
                entrada = None

                registrar_movimentacoes(
                    movimentacoes, codigo_produto, produto, quantidade, valor, user, entrada, saida
                )
            break

    return


def registrar_entrada(estoque, movimentacoes, user, setor):
    produto = input("CÓDIGO/PRODUTO: ").strip()
    quantidade = int(input("Quantidade: "))

    for item, valor in estoque.items():
        if item == produto or valor["produto"] == produto:
            codigo_produto = item

            if item == produto:
                produto = valor["produto"]

            valor["quantidade_estoque"] += quantidade
            saida = None
            entrada = str(datetime.now().strftime("%Y-%m-%d"))
            registrar_movimentacoes(
                movimentacoes, codigo_produto, produto, quantidade, valor, user, entrada, saida
            )

            break
        else:
            print("PRODUTO não existe no estoque!")
            if setor == "1" or setor == "2" or setor == "9":
                adicionar = input(
                    "Deseja adicionar um novo produto ao estoque? (S/N)"
                ).lower()

                if adicionar == "s" or adicionar == "sim":
                    produto_adicionar = input("Nome do Produto: ").lower()
                    quantidade = int(input("Quantidade: "))
                    preco = float(input("Preço: "))
                    tamanho = input("Tamaho (Ex:20cm): ")
                    num_codigo_produto = len(estoque) + 1
                    codigo_produto = f"{produto[0:3].upper()}{num_codigo_produto}"
                    saida = None
                    entrada = str(datetime.now().strftime("%Y-%m-%d"))

                    estoque[codigo_produto] = {
                        "produto": produto_adicionar,
                        "quantidade_estoque": quantidade,
                        "preco": preco,
                        "tamanho": tamanho,
                        "classificacao": None,
                    }
                    registrar_movimentacoes(
                        movimentacoes, codigo_produto, produto, quantidade, valor, user, entrada, saida
                    )

    return


def menu(estoque, movimentacoes, user, setor):
    acao = input(
        "1 - Registrar saída\n"
        "2 - Registrar entrada de produto\n"
        "3 - Verificar preço de um produto\n"
        "4 - Sair\n"
        "Digite a opção desejada: "
    )

    if acao == "1":
        registrar_saida(estoque, movimentacoes, user, setor)
        mostrar_estoque_total(estoque)
        mostrar_movimentacoes(movimentacoes)

    if acao == "2":
        registrar_entrada(estoque, movimentacoes, user, setor)
        mostrar_estoque_total(estoque)
        mostrar_movimentacoes(movimentacoes)


def main():
    user = str(input("USER do Funcinário: ")).lower()

    for users in login_funcionario.values():
        if users["user"] == user:

            senha = str(input("SENHA do Funcinário: ")).lower()
            if users["senha"] == senha:
                setor = str(
                    input(
                        "Selecione o setor do funcionário:\n"
                        "1 - Estoque / Almoxarifado\n"
                        "2 - Compras / Suprimentos\n"
                        "3 - Vendas / Comercial\n"
                        "4 - Logística / Expedição\n"
                        "5 - Cadastro de Produtos\n"
                        "6 - Financeiro\n"
                        "7 - TI / Sistemas\n"
                        "8 - Controle de Qualidade\n"
                        "9 - Administração / Gerência\n"
                        "Digite o número do seu setor: "
                    )
                )
                if users["setor"] == setor:
                    menu(estoque, movimentacoes, user, setor)

                else:
                    print("O user não pertence a esse setor!")
            else:
                print("SENHA INCORRETA")
        else:
            print(f"User : {user} indisponível no momento!")


main()
