

despensa = ["arroz", "feijão", "sal"]

item = input("Digite o item que deseja verificar na despensa: ").lower().strip()

if item in despensa:
    print(f"O item {item} está na despensa.")
else:
    print(f"O item {item} precisa ser comprado.")