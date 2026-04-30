
#funções da calculadora
def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

#Calculadora
def calculadora():
    while True:
        try:
            num1 = float(input("Digite um numero: "))
            num2 = float(input("Digite outro numero: "))
            operacao  = input("Digite a operação desejada (somar (+), subtrair (-), multiplicar (*), dividir (/)): ")
            if operacao == "+":
              resultado = somar(num1, num2)
            elif operacao == "-":
                resultado = subtrair(num1, num2)
            elif operacao == "*":
              resultado = multiplicar(num1, num2)
            elif operacao == "/":
                resultado = dividir(num1, num2)
            else:
              print("Operação inválida!")
              continue

            print(f"Resultado: {resultado}")
            break
    #tratamento de erros
        except ValueError:
            print("Digite apenas números!")
        except ZeroDivisionError:
            print("Não é possível dividir por zero!")

calculadora()