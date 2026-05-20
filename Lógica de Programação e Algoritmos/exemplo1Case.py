print ("----- Menu de opção -----") 
print ("1 - Circulo")
print ("2 - Triângulo")
print ("3 - Quadrado")
opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        print("🔵")
    case 2:
        print("🔺")
    case 3:
        print("⏹️")
    case _:
        print("✖️")