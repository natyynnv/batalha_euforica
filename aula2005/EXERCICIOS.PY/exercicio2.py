vetor = []

# Leitura dos números reais
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    vetor.append(numero)

# Exibição na ordem inversa
print("\nNúmeros na ordem inversa:")
for numero in reversed(vetor):
    print(numero)