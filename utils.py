# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função principal que solicita ao usuário a conversão desejada
def conversor_de_temperatura():
    print("Conversor de Temperatura")
    print("1: Celsius para Fahrenheit")
    print("2: Fahrenheit para Celsius")
    
    # Solicita ao usuário escolher a opção
    opcao = input("Escolha a conversão desejada (1 ou 2): ")
    
    # Verifica a escolha do usuário e realiza a conversão correspondente
    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius:.2f}°C é equivalente a {fahrenheit:.2f}°F")
    
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F é equivalente a {celsius:.2f}°C")
    
    else:
        print("Opção inválida. Tente novamente.")

# Chama a função principal
conversor_de_temperatura()
