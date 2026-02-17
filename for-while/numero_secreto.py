import random

numero_secreto = random.randint(1, 10)
tentativas = 0
acertou = False

while not acertou:
    tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1

    if tentativa == numero_secreto:
        acertou = True
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
    elif tentativa < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")