import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

computador = random.choice(opcoes)

print(f"Jogador: {jogador}")
print(f"Computador: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra"):
    print("Jogador venceu!")
else:
    print("Você perdeu!")