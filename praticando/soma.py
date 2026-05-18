
while True:
    try:
        numero1 = float(input("Digite um numero: "))
        numero2 = float(input("Digite mais um numero: "))
        soma = (numero1) + (numero2)
        print("A soma entre os numeros digitados é: ", soma)
        break
    except ValueError:
        print("Erro. Você digitou letras ou deixou em branco. Digite apenas números reais.")