vetor = []

# Leitura dos números
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)

# Exibição dos números
print("\nNúmeros digitados:")
for numero in vetor:
    print(numero)