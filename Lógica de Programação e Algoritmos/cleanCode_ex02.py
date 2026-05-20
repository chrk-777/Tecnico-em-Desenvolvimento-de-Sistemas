idade = int(input("Digite sua idade: "))
if (idade >= 18):
    print("Você é de maior!")
elif(idade >= 0 and idade < 18):
    print("Você é de menor!")
else:
    print("Idade invalida")