
ano_nasicmento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))


def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

idade = calcular_idade(ano_nasicmento, ano_atual)
print(f"A idade é {idade} anos.") 
