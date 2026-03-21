def calcular_preco_total(movimentacoes):
    for itens in movimentacoes.values():
        itens["total"] = itens["quantidade"] * itens["preco"]

def classificar(estoque):
    for itens in estoque.values():
        tamanho = float(itens["tamanho"].replace("cm", ""))
        if tamanho <= 15:
            itens["classificacao"] = "P"
        elif tamanho > 15 and tamanho < 40:
            itens["classificacao"] = "M"
        elif tamanho >= 40.0:
            itens["classificacao"] = "G"
        
