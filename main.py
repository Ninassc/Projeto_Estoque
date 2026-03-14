from database import movimentacoes, estoque, login_funcionario


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

def entrar():
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
                       return setor
                    else: 
                        print("O user não pertence a esse setor!")
            else:
                print("SENHA INCORRETA")
        else:
            print(f"User : {user} indisponível no momento!")
    return


def main():
    setor = entrar()
    
    if setor != None:
        mostrar_estoque_total()

main()
