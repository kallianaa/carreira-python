#1 - Para verificar se um número é impar ou par:
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

print("********************************************************")

#2 - Para fazer as condicionais que informará a idade em categorias:
idade = int(input("Digite sua idade: "))
if 0 < idade <= 12:
    print("Criança")
elif 12 < idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else:
    print("Valor inválido!")

print("********************************************************")

#3 - Para fazer uma condicional que poderá verificar os valores de usuário e senha
usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")


print("********************************************************")

#4 - Para verificar onde o ponto está localizado no plano cartesiano, você pode utilizar a seguinte estrutura:
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")