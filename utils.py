#Comentário Teste
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def conversor_de_temperatura():
    print("Conversor de Temperatura")
    print("1: Celsius para Fahrenheit")
    print("2: Fahrenheit para Celsius")
    print("3: Converter lista de temperaturas")
    print("4: Calcular média das temperaturas convertidas")
    
    opcao = input("Escolha a opção desejada (1, 2, 3 ou 4): ")
    
    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius:.2f}°C é equivalente a {fahrenheit:.2f}°F")
    
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F é equivalente a {celsius:.2f}°C")
    
    elif opcao == "3":
        lista_temperaturas = input("Digite as temperaturas separadas por vírgula (ex.: 20,30,40): ")
        temperaturas = [float(temp) for temp in lista_temperaturas.split(',')]
        tipo_conversao = input("Converter para (1) Fahrenheit ou (2) Celsius? ")
        
        if tipo_conversao == "1":
            convertido = [celsius_para_fahrenheit(temp) for temp in temperaturas]
            print("Temperaturas em Fahrenheit:", convertido)
        elif tipo_conversao == "2":
            convertido = [fahrenheit_para_celsius(temp) for temp in temperaturas]
            print("Temperaturas em Celsius:", convertido)
        else:
            print("Opção inválida.")
    
    elif opcao == "4":
        lista_temperaturas = input("Digite as temperaturas separadas por vírgula (ex.: 20,30,40): ")
        temperaturas = [float(temp) for temp in lista_temperaturas.split(',')]
        tipo_conversao = input("Converter para (1) Fahrenheit ou (2) Celsius? ")
        
        if tipo_conversao == "1":
            convertido = [celsius_para_fahrenheit(temp) for temp in temperaturas]
        elif tipo_conversao == "2":
            convertido = [fahrenheit_para_celsius(temp) for temp in temperaturas]
        else:
            print("Opção inválida.")
            return
        
        media = sum(convertido) / len(convertido)
        print(f"Média das temperaturas convertidas: {media:.2f}")
    
    else:
        print("Opção inválida. Tente novamente.")

# Chama a função principal
conversor_de_temperatura()
