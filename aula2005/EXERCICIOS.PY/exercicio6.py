medias = []
aprovados = 0

# Leitura das notas dos 10 alunos
for i in range(10):
    print(f"\nAluno {i + 1}")

    soma = 0
    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota: "))
        soma += nota

    media = soma / 4
    medias.append(media)

    # Verifica se a média é maior ou igual a 7
    if media >= 7.0:
        aprovados += 1

# Exibição das médias
print("\nMédias dos alunos:")
for i in range(10):
    print(f"Aluno {i + 1}: {medias[i]:.2f}")

# Exibição da quantidade de aprovados
print(f"\nNúmero de alunos com média maior ou igual a 7.0: {aprovados}")