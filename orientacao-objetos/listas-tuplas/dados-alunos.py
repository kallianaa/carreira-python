entrada = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(",")


for i in range(0, len(entrada), 3):
    nome = entrada[i].strip()
    idade = int(entrada[i+1].strip())
    nota = float(entrada[i+2].strip())

    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}")

    print()