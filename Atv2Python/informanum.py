numnota = int(input("Digite a quantidade de notas: "))
media = 0
notas = []

for i in range(numnota):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / numnota

if media >= 7:
    print(f"Aprovado, a média é: {media:.2f}")
else:
    print(f"Reprovado, a média é: {media:.2f}")
