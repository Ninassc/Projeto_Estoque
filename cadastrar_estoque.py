from datetime import datetime
from funcoes_database import classificar
from lerbanco import salvar
from registrar_movimentacoes import registrar_movimentacoes

def cadastrar_estoque(estoque, movimentacoes, setor, user):
    if setor == "1" or setor == "2" or setor == "9":
        adicionar = input("Deseja adicionar um novo produto ao estoque? (S/N)\n").lower()

        if adicionar == "s" or adicionar == "sim":
            produto_adicionar = input("Nome do Produto: ").lower()
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            tamanho = input("Tamaho (Ex:20cm): ")
            tipo = input("Tipo: ")
            parte = input("Parte: ")
            veiculos = input("Veiculos: ")
            veiculos = veiculos.split(",")
            fabricante = input("Fabricante: ")
            data_fabricacao = input("Data de Fabricacao: ")
            num_codigo_produto = len(estoque) + 1
            codigo_produto = f"{produto_adicionar[0:3].upper()}{num_codigo_produto}"
            saida = None
            entrada = str(datetime.now().strftime("%Y-%m-%d"))

            estoque[codigo_produto] = {
                "produto": produto_adicionar,
                "quantidade_estoque": quantidade,
                "preco": preco,
                "tamanho": tamanho,
                "classificacao": None,
                "tipo": tipo,
                "parte": parte,
                "veiculos": veiculos,
                "fabricante": fabricante,
                "data_fabricacao": data_fabricacao,
            }
            registrar_movimentacoes(
                movimentacoes,
                codigo_produto,
                produto_adicionar,
                quantidade,
                preco,
                user,
                entrada,
                saida,
            )

            classificar(estoque)
            salvar()
