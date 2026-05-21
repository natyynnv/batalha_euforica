alunos = ["davi","daniel","wanchise","igor","nicoli","ian","natasha","fabio"]
print("formacao original")
print(alunos)

alunos.append("antoni")
print("adicionamos o antoni")

alunos.remove("nicoli")
print("removemos a nicoli")
print()
print(f"ha {len(alunos)} alunos presentes hoje!")

print()

for aluno in alunos:
    print(f"boa noite {aluno}")