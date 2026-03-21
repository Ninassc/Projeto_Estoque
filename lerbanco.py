import json

path = "database.json"

def ler_banco():
    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

# def salvar():
#     from main_func import login_funcionario, estoque, movimentacoes
#     dados_atualizados = {
#         "login_funcionario": login_funcionario,
#         "estoque": estoque,
#         "movimentacoes": movimentacoes
#     }
#     with open(path, "w", encoding="utf-8") as arquivo:
#         json.dump(dados_atualizados, arquivo, indent=4, ensure_ascii=False)
