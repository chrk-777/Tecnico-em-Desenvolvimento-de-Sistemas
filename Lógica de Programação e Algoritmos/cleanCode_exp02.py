notas = []

for i in range(4):
    # Tenta solicitar as notas
    try:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if(nota < 0 or nota > 10):
            print("Nota inválida. Insira um valor entre 0 e 10!")
            exit()
        else:
            notas.append(nota)
    # Se tiver algum erro (excessão) de valor, retorna uma mensagem
    except ValueError:
        print("Erro: Insira um número valido!")

#Se a pessoa apenas digitou texto
if not notas:
    print("Erro: Nenhuma nota foi inserida!")
else:
    media = sum(notas)/len(notas)

    if(media >= 7):
        print(f"Media = {media} - Aprovado!")
    elif(media >= 5):
        print(f"Media = {media} - Recuperação!")
    else:
        print(f"Media = {media} - Reprovado!")

