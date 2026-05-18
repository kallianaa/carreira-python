texto = input("Digite a sua frase aqui: ").lower()

def contar_vogais(texto):
    contador = 0
    vogais = "aeiouáéíóúâêîôûãõ"

    for letra in texto:
        if letra in vogais:
            contador += 1

print(f"O texto contém {contador} vogais.")