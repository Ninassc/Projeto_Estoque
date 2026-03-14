from funcoes_database import classificar, calcular_preco_total

estoque = {
    "MTR008": {
        "produto": "motor",
        "quantidade_estoque": 10,
        "preco": 2000.00,
        "tamanho": "60cm",
        "classificacao" : None
    },
    "RAD002": {
        "produto": "radiador",
        "quantidade_estoque": 5,
        "preco": 350.00,
        "tamanho": "50cm",
        "classificacao" : None
    },
    "ALT003": {
        "produto": "alternador",
        "quantidade_estoque": 50,
        "preco": 500.00,
        "tamanho": "25cm",
        "classificacao" : None
    },
    "BAT004": {
        "produto": "bateria",
        "quantidade_estoque": 3,
        "preco": 450.00,
        "tamanho": "30cm",
        "classificacao" : None
    },
    "EMB005": {
        "produto": "embreagem",
        "quantidade_estoque": 20,
        "preco": 700.00,
        "tamanho": "28cm",
        "classificacao" : None
    },
    "AMT006": {
        "produto": "amortecedor",
        "quantidade_estoque": 67,
        "preco": 300.00,
        "tamanho": "45cm",
        "classificacao" : None
    },
    "VEL007": {
        "produto": "velas de ignicao",
        "quantidade_estoque": 2,
        "preco": 120.00,
        "tamanho": "7cm",
        "classificacao" : None
    },
    "FIL008": {
        "produto": "filtro de ar",
        "quantidade_estoque": 34,
        "preco": 80.00,
        "tamanho": "20cm",
        "classificacao" : None
    },
    "PAS009": {
        "produto": "pastilha de freio",
        "quantidade_estoque": 0,
        "preco": 150.00,
        "tamanho": "15cm",
        "classificacao" : None
    },
    "COR010": {
        "produto": "correia dentada",
        "quantidade_estoque": 1,
        "preco": 220.00,
        "tamanho": "90cm",
        "classificacao" : None
    },
}

# Cod --> nome_produto, quantidade, total, entrada, saida
movimentacoes = {
        "ALT003": {
            "produto": "alternador",
            "quantidade": 2,
            "preco": 500.00,
            "total": None,
            "entrada": "2025-01-16",
            "saida": "",
        },
    
        "COR010": {
            "produto": "correia dentada",
            "quantidade": 1,
            "preco": 220.00,
            "total": None,
            "entrada": "2025-01-16",
            "saida": "",
        }
}

classificar(estoque)
calcular_preco_total(movimentacoes)

print(movimentacoes)


