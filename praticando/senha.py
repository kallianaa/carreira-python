import random

maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
especiais = "!@#$%&*"

todas_opcoes = maiusculas + minusculas + numeros + especiais
senha = []

#Gera os 4 primeiros caracteres
senha.append(random.choice(maiusculas))
senha.append(random.choice(minusculas))
senha.append(random.choice(numeros))
senha.append(random.choice(especiais))

#Gera os caracteres restantes
for i in range(16):
    senha.append(random.choice(todas_opcoes))

#Embaralha a senha
random.shuffle(senha)
print(f"Senha gerada: {''.join(senha)}")