from database import movimentacoes, estoque

def mostrar_estoque_total():
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

def main():
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

    if setor == "1":
        mostrar_estoque_total()

main()