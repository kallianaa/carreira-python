hora_atual = int(input("Digite a hora atual: "))

def saudacao(hora_atual):
    if hora_atual < 12:
        return "Bom dia!"
    elif hora_atual < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

print(saudacao(hora_atual))