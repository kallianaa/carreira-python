
while True:
    try:
        valor = int(input("Digite um número inteiro: "))
        if valor % 2 != 0:
            print("ERRO: O valor deve ser múltiplo de 2.")
            continue
        else:
            print("Valor válido! Vamos calcular as notas")
            break
    except ValueError:
        print("ERRO: Digite apenas números inteiros.")