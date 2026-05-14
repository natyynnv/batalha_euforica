import random

# ================= INTRO =================
print("===================================")
print("        BATALHA EUFÓRICA          ")
print("===================================\n")

print("BEM-VINDO AO JOGO!")
print("Aqui você vai descontar toda sua raiva 😈\n")

print("PERSONAGENS:")
print("1 - Rue (100 HP) → estratégica")
print("2 - Maddy (100 HP) → agressiva\n")

print("INIMIGO:")
print("Cassie (100 HP) → imprevisível\n")

# ================= ESCOLHA =================
while True:
    personagem = input("Escolha seu personagem (1 ou 2): ")

    if personagem.isdigit():
        personagem = int(personagem)

        if personagem == 1:
            nome = "Rue"
            print("\nVocê escolheu RUE. Boa sorte!\n")
            break

        elif personagem == 2:
            nome = "Maddy"
            print("\nVocê escolheu MADDY. Boa sorte!\n")
            break

# ================= VIDA =================
vida = 100
vidainimigo = 100
dano_persistente = 0

# ================= LOOP DO JOGO =================
while vida > 0 and vidainimigo > 0:

    print("\n===================================")
    print(f"Sua vida: {vida}")
    print(f"Vida da Cassie: {vidainimigo}")
    print("===================================\n")

    # ================= TURNO DO JOGADOR =================
    print("SUA VEZ")
    print("1 - MULTI-DANO (combo)")
    print("2 - DANO PERSISTENTE")

    while True:
        ataque = input("Escolha seu ataque: ")

        if ataque.isdigit():
            ataque = int(ataque)
            if ataque == 1 or ataque == 2:
                break

    # ================= MULTI-DANO REAL =================
    if ataque == 1:
        print(f"\n{nome} iniciou um MULTI-DANO!")

        total_dano = 0

        for i in range(4):  # 4 hits
            hit = random.randint(5, 12)
            vidainimigo -= hit
            total_dano += hit
            print(f"Hit {i+1}: {hit} de dano")

        print(f"Dano total do combo: {total_dano}")

    # ================= DANO PERSISTENTE =================
    elif ataque == 2:
        dano = random.randint(5, 10)
        vidainimigo -= dano
        dano_persistente = random.randint(3, 7)

        print(f"{nome} causou {dano} de dano")
        print(f"Ativou dano persistente de {dano_persistente}")

    # ================= EFEITO PERSISTENTE =================
    if dano_persistente > 0:
        vidainimigo -= dano_persistente
        print(f"Dano persistente causa {dano_persistente} na Cassie")

    # vitória
    if vidainimigo <= 0:
        print("\nCassie foi derrotada! Você venceu!")
        break

    # ================= VEZ DA CASSIE =================
    print("\nVEZ DA CASSIE")

    ataque_inimigo = random.randint(10, 25)
    vida -= ataque_inimigo

    print(f"Cassie causou {ataque_inimigo} de dano em {nome}")

    # derrota
    if vida <= 0:
        print("\nVocê foi derrotado pela Cassie!")
        break

# ================= FIM =================
print("\n===================================")
print("FIM DE JOGO")
print("===================================")