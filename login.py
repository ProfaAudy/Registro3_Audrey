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
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado. Verifique o nome de usuário.")

# Chama a função para realizar o login
realizar_login()
