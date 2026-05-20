notas = []

for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª nota:")))

media = sum(notas)/len(notas)

print("Sua média é:",media)