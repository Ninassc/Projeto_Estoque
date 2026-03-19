import json

path = "bd.json"

def ler_banco():
    
    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

print(ler_banco())
