idade: int
salario: float
altura: float
genero: str
nome: str

idade = 30
salario = 5800.50
altura = 1.80
genero = "F"
nome = "Kalliana"

print(f"IDADE = {idade}")
print(f"SALARIO = {salario:.2f}")
print(f"ALTURA = {altura:.2f}")
print(f"GENERO = {genero}")
print(f"NOME = {nome}")
print(f"A funcionaria {nome}, genero {genero}, tem {idade} anos e ganha R${salario:.2f}")
print("A funcionaria {:s}, genero {:s}, tem {:d} anos e ganha R${:.2f}".format(nome, genero, idade, salario))

print("********************************************************")

x = 5
y = 2

z = 5 % 2 #resto divisão
print(z)

z = 5 ** 2 #elevado a
print(z)

z = 5 * 2 #multiplicaçao
print(z)

z = 5 + 2 #soma
print(z)

z = 5 - 2 #subtracao
print(z)

z = 5 / 2 #divisao real
print(z)

z = 5 // 2 #divisao inteira
print(z)

print("********************************************************")

print("Bom dia", end="")
print("Boa noite")

print("********************************************************")

a = "Maria"
b = 19

print("%s tem %d anos." % (a, b))

print("********************************************************")

e: int
d: int

e = 10
d = 20

print(e)
print(d)

print("********************************************************")
b1: float
b2: float
h: float
area: float

b1 = 6.0
b2 = 8.0
h = 5.0

area = (b1 + b2) / 2.0 * h
print(f"a area do trapezio é: " + str(area))
print("********************************************************")
f = int(input("Digite um número: "))
if(f < 10):
    print("o valor de F é menor que 10")
elif(f == 10):
    print("O valor de F é igual a 10")
else:
    print("O valor de F é maior que 10")
print("********************************************************")
v = 0
while(v < 10):
    print(v)
    v += 1
else:
    v = 0
print("********************************************************")

q = 0
while(True):
    if(q < 10):
        print(q)
        q += 1
    else:
        q = 0
        break
print("********************************************************")
t = [1, 2, 3, 4]
for i in t:
    print(i)
print("********************************************************")
g: int
soma: int

soma = 0
g = int(input("Digite o primiero numero: "))

while(g != 0):
    soma = soma + g
    g = int(input("Digite o proximo numero: ou digite 0 para parar: "))

print("SOMA = ", soma)
