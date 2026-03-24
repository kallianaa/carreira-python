epis = ["capacete", "luva", "bota"]

print(type(epis))
print(len(epis))
print(epis[1])

epis[2] = "óculos"
epis.append("protetor auricular")
epis.remove("capacete")

print("bota" in epis)

epis.insert(1, "cinto de segurança")

epis.clear()
print(epis)

def registrar(epi="capacete"):
    print(f"EPI registrado: {epi}")


registrar("luva")
registrar()

equipe_a = ["luva", "bota"]
equipe_b = equipe_a
equipe_b.append("óculos")
print(f"Equipe A tem: {equipe_a}")

estoque = ["capacete", "luva", "cinto", "bota"]
filtro = [item for item in estoque if "c" in item]
print(f"Filtro com a letra C: {filtro}")