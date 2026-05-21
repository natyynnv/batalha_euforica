notas = []

# Leitura das 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

# Cálculo da média
media = sum(notas) / 4

# Exibição das notas e da média
print("\nNotas digitadas:")
for nota in notas:
    print(nota)

print(f"\nMédia: {media:.2f}")