voluntarios = []

while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ").lower().strip()
    if nome.lower() == 'sair':
        break
    else:
        voluntarios.append(nome)

print("\nVoluntários registrados:", voluntarios)