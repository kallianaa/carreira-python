# for i in range(0, 5):
#     print(i)
#
# for i in range(0, 10, 2):
#     print(i)

x: int
soma: int

n = int(input("Quantos numeros serão digitados? "))
soma = 0
for i in range(0, n):
    x = int(input("Digite um numero: "))
    soma = soma + x

print("Soma = ", soma)