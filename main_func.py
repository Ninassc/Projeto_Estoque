from menu import menu

from funcoes_database import calcular_preco_total, classificar
from lerbanco import ler_banco

dados_banco = ler_banco()
estoque = dados_banco.get("estoque", {})
movimentacoes = dados_banco.get("movimentacoes", {})
login_funcionario = dados_banco.get("login_funcionario", {})

classificar(estoque)
calcular_preco_total(movimentacoes)

def main():
    user = str(input("USER do Funcinário: ")).lower()

    for users in login_funcionario.values():
        if users["user"] == user:

            senha = str(input("SENHA do Funcinário: ")).lower()
            if users["senha"] == senha:
                setor = str(
                    input(
                        "\n"
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
            break
    else:
        print(f"User : {user} indisponível no momento!")
