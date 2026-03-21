from registrar_saida import registrar_saida
from registrar_entrada import registrar_entrada
from mostrar_estoque_total import mostrar_estoque_total
from mostrar_movimentacoes import mostrar_movimentacoes
from verificar_preco import verificar_preco

def menu(estoque, movimentacoes, user, setor):
    
    while True: 
        acao = input(
            "\n"
            "Escolha a Ação:\n"
            "1 - Registrar saída\n"
            "2 - Registrar entrada de produto\n"
            "3 - Verificar preço de um produto\n"
            "4 - Sair\n"
            "Digite a opção desejada: "
        )
        
        if acao == "1":
            registrar_saida(estoque, movimentacoes, user, setor)
            mostrar_estoque_total(estoque)
            mostrar_movimentacoes(movimentacoes)

        if acao == "2":
            registrar_entrada(estoque, movimentacoes, user, setor)
            mostrar_estoque_total(estoque)
            mostrar_movimentacoes(movimentacoes)
        
        if acao == "3":
            verificar_preco(estoque)
        
        if acao == "4":
            break
