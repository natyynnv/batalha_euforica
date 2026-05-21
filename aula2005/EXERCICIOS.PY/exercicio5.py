vetor = []
par = []
impar = []

# Leitura dos 20 números inteiros
for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)

    # Separação em pares e ímpares
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

# Exibição dos vetores
print("\nVetor completo:")
print(vetor)

print("\nVetor PAR:")
print(par)

print("\nVetor IMPAR:")
print(impar)