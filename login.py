# Simulando um banco de dados de usuários com senhas
usuarios = {
    "usuario1": "senha123",
    "usuario2": "minhasenha",
    "usuario3": "abc123"
}

def realizar_login():
    print("Bem-vindo! Faça o login:")
    
    # Solicita o nome de usuário e senha
    username = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    # Verifica se o nome de usuário está registrado
    if username in usuarios:
        # Verifica se a senha está correta
        if usuarios[username] == senha:
            print(f"Login bem-sucedido! Bem-vindo, {username}!")
            menu_opcoes(username)
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado. Verifique o nome de usuário.")

def alterar_senha(username):
    nova_senha = input("Digite a nova senha: ")
    usuarios[username] = nova_senha
    print("Senha alterada com sucesso!")

def registrar_usuario():
    novo_usuario = input("Digite o nome de usuário: ")
    if novo_usuario in usuarios:
        print("Usuário já existe. Escolha outro nome.")
    else:
        nova_senha = input("Digite a senha: ")
        usuarios[novo_usuario] = nova_senha
        print("Usuário registrado com sucesso!")

def menu_opcoes(username):
    print("\nEscolha uma opção:")
    print("1: Alterar senha")
    print("2: Registrar novo usuário")
    print("3: Sair")
    
    opcao = input("Digite sua escolha (1, 2 ou 3): ")
    
    if opcao == "1":
        alterar_senha(username)
    elif opcao == "2":
        registrar_usuario()
    elif opcao == "3":
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")

# Chama a função para realizar o login
realizar_login()
