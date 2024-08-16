# Simulando um banco de dados de produtos com seus preços
produtos = {
    "camiseta": 49.90,
    "calça": 89.90,
    "tênis": 149.90,
    "mochila": 99.90
}

def exibir_produtos():
    print("Produtos disponíveis:")
    for produto, preco in produtos.items():
        print(f"{produto.title()}: R$ {preco:.2f}")

def aplicar_desconto(preco, desconto):
    return preco - (preco * desconto / 100)

def realizar_pagamento():
    exibir_produtos()
    
    # Solicita ao usuário escolher um produto
    produto_escolhido = input("Escolha um produto: ").lower()
    
    if produto_escolhido in produtos:
        preco = produtos[produto_escolhido]
        print(f"Você escolheu {produto_escolhido.title()} que custa R$ {preco:.2f}.")
        
        # Solicita ao usuário o valor do pagamento
        valor_pago = float(input("Insira o valor do pagamento: R$ "))
        
        # Verifica se o valor é suficiente
        if valor_pago >= preco:
            desconto = float(input("Digite o percentual de desconto (0 se não houver): "))
            preco_com_desconto = aplicar_desconto(preco, desconto)
            troco = valor_pago - preco_com_desconto
            print(f"Pagamento bem-sucedido! O valor com desconto é R$ {preco_com_desconto:.2f}. Seu troco é R$ {troco:.2f}.")
        else:
            print("Valor insuficiente. Tente novamente.")
    else:
        print("Produto não encontrado. Verifique a escolha.")

def realizar_pagamento_multiplo():
    total = 0
    while True:
        exibir_produtos()
        produto_escolhido = input("Escolha um produto ou digite 'fim' para finalizar: ").lower()
        
        if produto_escolhido == 'fim':
            break
        elif produto_escolhido in produtos:
            preco = produtos[produto_escolhido]
            total += preco
        else:
            print("Produto não encontrado. Tente novamente.")
    
    print(f"Total a pagar: R$ {total:.2f}")
    valor_pago = float(input("Insira o valor do pagamento: R$ "))
    
    if valor_pago >= total:
        troco = valor_pago - total
        print(f"Pagamento bem-sucedido! Seu troco é R$ {troco:.2f}.")
    else:
        print("Valor insuficiente. Tente novamente.")

# Chama a função para realizar o pagamento
#realizar_pagamento() # Para pagamento único
realizar_pagamento_multiplo() # Para pagamento múltiplo
