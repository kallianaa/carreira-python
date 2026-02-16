
kms = float(input("Digite distância percorrida em KM: "))

if kms <= 100:
    print("Valor do pedágio: R$ 10,00")
elif  100 <= kms < 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 30,00")

