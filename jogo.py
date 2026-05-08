print("BATALHA EUFORICA")
print("BEM VINDO AO JOGO")
print("o jogo se passa na sala de estar da casa da Cassie ")

print("personagem 1: Rue")
print("personagem 2: Maddy")
print("inimigo Cassie")
import random



print("escolha seu personagem: 1 para Rue, 2 para Maddy para essa batalha com Cassie")
personagem = int(input())
if personagem == 1:  print("Rue")
elif personagem == 2:  print("Maddy")
else:  print("personagem invalido")


for i in range(1,3):
    print(f"essa é a sua {i} rodada")
    if personagem == 1:
        print("escolha seu ataque: 1 para xingamentos, 2 para tapas")
        ataque = int(input())
        if ataque == 1:  print("Rue chama Cassie de #@!&*#$%! ! causa 15 de dano")
        elif ataque == 2:  print("Rue da um tapa no rosto da Cassie. causa 25 de dano")
        else: print("ataque invalido")

    if personagem == 2:
        print("escolha seu ataque: 1 para tapa, 2 para puxão de cabelo")
        ataque = int(input())
        if ataque == 1: print("Maddy chega perto de Cassie e da tapas no rosto dela. causa 25 de dano")
        elif ataque == 2: print("Maddy chega perto da Cassie e puxa o cabelo dela. causa 15 de dano")
        else: print("ataque invalido")

        print("Vez da Cassie")

        ataque_inimigo = random.randint(1,2)
        if ataque_inimigo == 1: print("Cassie começa a chorar, causa 0 dano")
        elif ataque_inimigo == 2: print("Cassie começa a xingar, causa 10 de dano")

        print("vida do jogador")
        if personagem == 1 and ataque_inimigo == 1:  print("Rue não se atingiu. tem 100 de vida restante")
        if personagem == 1 and ataque_inimigo == 2: print("Rue se ofendeu. tem 90 de vida restante")
        if personagem == 2 and ataque_inimigo == 1: print("Maddy não se atingiu. tem 100 de vida restante")
        if personagem == 2 and ataque_inimigo == 2: print("Maddy se ofendeu. tem 90 de vida restante")

        print("vida da Cassie")
        if personagem == 1 and ataque == 1: print("Cassie se ofendeu e comecou a chorar. tem 85 de vida restante")
        if personagem == 1 and ataque == 2: print("Cassie se machucou. tem 75 de vida restante")
        if personagem == 2 and ataque == 1: print("Cassie cai no chão com os tapas. tem 75 de vida restante")
        if personagem == 2 and ataque == 2: print("Cassie tropeça e se machuca. tem 85 de vida restante")


