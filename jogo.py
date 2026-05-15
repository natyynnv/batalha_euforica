import random

# ================= INTRO =================
print("===================================")
print("        BATALHA EUFÓRICA          ")
print("===================================\n")

print("BEM-VINDO AO JOGO!")
print("Aqui você vai descontar toda sua raiva 😈\n")

# ================= PERSONAGENS =================
personagens = {
    1: {
        "nome": "Rue",
        "vida": 100
    },

    2: {
        "nome": "Maddy",
        "vida": 100
    }
}

# ================= INIMIGO =================
inimigo = {
    "nome": "Cassie",
    "vida": 100,
    "dano_persistente": []
}

# ================= MOSTRAR PERSONAGENS =================
print("PERSONAGENS:")

for chave, personagem in personagens.items():
    print(f"{chave} - {personagem['nome']} ({personagem['vida']} HP)")

print("\nINIMIGO:")
print(f"{inimigo['nome']} ({inimigo['vida']} HP)\n")

# ================= ESCOLHA =================
while True:

    escolha = input("Escolha seu personagem (1 ou 2): ")

    if escolha.isdigit():

        escolha = int(escolha)

        if escolha in personagens:

            jogador = personagens[escolha]

            print(f"\nVocê escolheu {jogador['nome'].upper()}! Boa sorte!\n")

            break

# ================= LOOP DO JOGO =================
while jogador["vida"] > 0 and inimigo["vida"] > 0:

    print("\n===================================")
    print(f"Vida de {jogador['nome']}: {jogador['vida']}")
    print(f"Vida da {inimigo['nome']}: {inimigo['vida']}")
    print("===================================\n")

    # ================= MENU =================
    print("SUA VEZ")
    print("1 - SEQUÊNCIA DE TAPAS")
    print("2 - PUXÃO DE CABELO")

    while True:

        ataque = input("Escolha seu ataque: ")

        if ataque.isdigit():

            ataque = int(ataque)

            if ataque == 1 or ataque == 2:
                break

    # ================= ATAQUE 1 =================
    if ataque == 1:

        print(f"\n{jogador['nome']} iniciou uma SEQUÊNCIA DE TAPAS!")

        total_dano = 0

        for i in range(4):

            tapa = random.randint(2, 7)

            inimigo["vida"] -= tapa

            total_dano += tapa

            print(f"Hit {i+1}: {tapa} de dano")

        print(f"Dano total do combo: {total_dano}")

    # ================= ATAQUE 2 =================
    elif ataque == 2:

        dano = random.randint(2, 7)

        inimigo["vida"] -= dano

        novo_dano = random.randint(3, 8)

        inimigo["dano_persistente"].append(novo_dano)

        print(f"\n{jogador['nome']} causou {dano} de dano")

        print(
            f"Cassie está com {inimigo['dano_persistente']} dor na cabeça"
        )

    # ================= DANO PERSISTENTE =================
    if len(inimigo["dano_persistente"]) > 0:

        dano_total = sum(inimigo["dano_persistente"])

        inimigo["vida"] -= dano_total

        print(f"Cassie sofreu {dano_total} de dor na cabeça")

    # impedir vida negativa
    inimigo["vida"] = max(0, inimigo["vida"])

    # ================= VITÓRIA =================
    if inimigo["vida"] <= 0:

        print(f"\n{inimigo['nome']} foi derrotada!")
        print("VOCÊ VENCEU 😈")

        break

    # ================= TURNO DA CASSIE =================
    print("\nVEZ DA CASSIE")

    ataque_inimigo = random.randint(10, 40)

    jogador["vida"] -= ataque_inimigo

    jogador["vida"] = max(0, jogador["vida"])

    print(
        f"{inimigo['nome']} causou {ataque_inimigo} de dano em {jogador['nome']}"
    )

    # ================= DERROTA =================
    if jogador["vida"] <= 0:

        print(f"\n{jogador['nome']} foi derrotado!")
        print("CASSIE VENCEU 😈")

        break

# ================= FIM =================
print("\n===================================")
print("FIM DE JOGO")
print("===================================")