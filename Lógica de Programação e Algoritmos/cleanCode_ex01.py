numeros = []

for i in range(6):
    numeros.append(int(input(f"Digite o {i+1}° número:")))

soma = sum(numeros)
print("Soma total é: ",soma)