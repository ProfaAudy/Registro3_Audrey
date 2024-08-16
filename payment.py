# Simulando um banco de dados de produtos com seus preços
produtos = {
    "camiseta": 49.90,
    "calça": 89.90,
    "tênis": 149.90,
    "mochila": 99.90
}

# Função para exibir os produtos disponíveis
def exibir_produtos():
    print("Produtos disponíveis:")
    for produto, preco in produtos.items():
        print(f"{produto.title()}: R$ {preco:.2f}")

# Função para simular o pagamento
def realizar_pagamento():
    exibir_produtos()
    
    # Solicita ao usuário escolher um produto
    produto_escolhido = input("Escolha um produto: ").lower()
    
    # Verifica se o produto está disponível
    if produto_escolhido in produtos:
        preco = produtos[produto_escolhido]
        print(f"Você escolheu {produto_escolhido.title()} que custa R$ {preco:.2f}.")
        
        # Solicita ao usuário inserir o valor do pagamento
        valor_pago = float(input("Insira o valor do pagamento: R$ "))
        
        # Verifica se o valor é suficiente
        if valor_pago >= preco:
            troco = valor_pago - preco
            print(f"Pagamento bem-sucedido! Seu troco é R$ {troco:.2f}.")
        else:
            print("Valor insuficiente. Tente novamente.")
    else:
        print("Produto não encontrado. Verifique a escolha.")

# Chama a função para realizar o pagamento
realizar_pagamento()
