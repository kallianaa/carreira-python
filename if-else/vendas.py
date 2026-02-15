vendasMaca = int(input("Digite o numero de vendas das MAÇAS: "))
vendasBananas = int(input("Digite o numero de vendas das BANANAS: "))

if vendasMaca > vendasBananas:
    print("As maças tiveram mais vendas")
elif vendasMaca < vendasBananas:
    print("As bananas tiveram mais vendas")
else:
    print("As vendas foram iguais")