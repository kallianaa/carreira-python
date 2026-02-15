horarioAcesso = int(input("Digite a hora atual (formato 24 horas): "))

if 8 <= horarioAcesso <= 18:
    print("Acesso permitido")
else:
    print("Acesso negado")