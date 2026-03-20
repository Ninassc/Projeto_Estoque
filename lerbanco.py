import json

path = "database.json"

def ler_banco():
    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

# def salvar_banco(dados):
#     with open(path, "w", encoding="utf-8") as arquivo:
#         json.dump(dados, arquivo, indent=4, ensure_ascii=False)
