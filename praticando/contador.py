
while True:
    frase = input("Digite uma frase: ").lower().strip()
    frase = (frase.replace(",", "").replace(".", "").replace(":", "").replace("()", "")
         .replace("!", "").replace("?", "").replace(";", "").replace("[]", "")
         .replace("{}", "").replace("<>", "").replace("/", "").replace("\\", "")
         .replace("|", "")).replace("'", "")
    if frase == "":
        print("Texto em branco. Por favor, digite palavras reais.")

        continue
    else:
        break

lista_palavras = frase.split()

print(lista_palavras)

contagem = {}

for palavra in lista_palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)