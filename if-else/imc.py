peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")


if peso / (altura * altura) < 18.5:
    print("Você abaixo do peso")
elif peso / (altura * altura) < 25:
    print("Você está no peso ideal")
else:
    print("Você está acima do peso.")