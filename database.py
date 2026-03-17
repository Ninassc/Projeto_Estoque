from funcoes_database import classificar, calcular_preco_total

#user, senha, setor
login_funcionario = {
    "FUN1" : {
        "user" : "lucassilva",
        "senha" : "lk123",
        "setor" : "9"
    },
    "FUN2" : {
        "user" : "mariaclara",
        "senha" : "mc456",
        "setor" : "2"
    },
    "FUN3" : {
        "user" : "joaosouza",
        "senha" : "js789",
        "setor" : "5"
    },
    "FUN4" : {
        "user" : "fernandocosta",
        "senha" : "fc123",
        "setor" : "1"
    },
    "FUN5" : {
        "user" : "camilalima",
        "senha" : "cl456",
        "setor" : "3"
    },
    "FUN6" : {
        "user" : "rafaelalves",
        "senha" : "ra789",
        "setor" : "7"
    },
    "FUN7" : {
        "user" : "patriciasilva",
        "senha" : "ps321",
        "setor" : "4"
    }
}

estoque = {
    "MTR1": {
        "produto": "motor",
        "quantidade_estoque": 10,
        "preco": 2000.00,
        "tamanho": "60cm",
        "classificacao" : None
    },
    "RAD2": {
        "produto": "radiador",
        "quantidade_estoque": 5,
        "preco": 350.00,
        "tamanho": "50cm",
        "classificacao" : None
    },
    "ALT3": {
        "produto": "alternador",
        "quantidade_estoque": 50,
        "preco": 500.00,
        "tamanho": "25cm",
        "classificacao" : None
    },
    "BAT4": {
        "produto": "bateria",
        "quantidade_estoque": 3,
        "preco": 450.00,
        "tamanho": "30cm",
        "classificacao" : None
    },
    "EMB5": {
        "produto": "embreagem",
        "quantidade_estoque": 20,
        "preco": 700.00,
        "tamanho": "28cm",
        "classificacao" : None
    },
    "AMT6": {
        "produto": "amortecedor",
        "quantidade_estoque": 67,
        "preco": 300.00,
        "tamanho": "45cm",
        "classificacao" : None
    },
    "VEL7": {
        "produto": "velas de ignicao",
        "quantidade_estoque": 2,
        "preco": 120.00,
        "tamanho": "7cm",
        "classificacao" : None
    },
    "FIL8": {
        "produto": "filtro de ar",
        "quantidade_estoque": 34,
        "preco": 80.00,
        "tamanho": "20cm",
        "classificacao" : None
    },
    "PAS9": {
        "produto": "pastilha de freio",
        "quantidade_estoque": 0,
        "preco": 150.00,
        "tamanho": "15cm",
        "classificacao" : None
    },
    "COR10": {
        "produto": "correia dentada",
        "quantidade_estoque": 1,
        "preco": 220.00,
        "tamanho": "90cm",
        "classificacao" : None
    },
    "PNE11": {
        "produto": "pneu",
        "quantidade_estoque": 40,
        "preco": 350.00,
        "tamanho": "38cm",
        "classificacao" : None
    },
    "BOM12": {
        "produto": "bomba d'agua",
        "quantidade_estoque": 15,
        "preco": 250.00,
        "tamanho": "15cm",
        "classificacao" : None
    },
    "DIS13": {
        "produto": "disco de freio",
        "quantidade_estoque": 20,
        "preco": 180.00,
        "tamanho": "25cm",
        "classificacao" : None
    },
    "OLE14": {
        "produto": "oleo de motor",
        "quantidade_estoque": 50,
        "preco": 45.00,
        "tamanho": "20cm",
        "classificacao" : None
    },
    "FAR15": {
        "produto": "farol",
        "quantidade_estoque": 12,
        "preco": 300.00,
        "tamanho": "40cm",
        "classificacao" : None
    },
}

# Cod --> nome_produto, quantidade, preco, total, entrada, saida
movimentacoes = {
        "MOV1": {
            "codigo_produto" : "ALT003",
            "produto": "alternador",
            "quantidade": 2,
            "preco": 500.00,
            "total": None,
            "entrada": "2025-01-16",
            "saida": "",
            "funcionario" :""
        },
    
        "MOV2": {
            "codigo_produto" : "COR010",
            "produto": "correia dentada",
            "quantidade": 1,
            "preco": 220.00,
            "total": None,
            "entrada": "2025-01-16",
            "saida": "",
            "funcionario" :""
        }
}

classificar(estoque)
calcular_preco_total(movimentacoes)

# print(movimentacoes)
print(login_funcionario.values())


