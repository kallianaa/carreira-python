texto = input("Digite seu texto aqui: ").split()

palavras_longas = []

for palavra in texto:
    if len(palavra) > 10:
        palavras_longas.append(palavra)

if len(palavras_longas) > 0:
    print(f"Palavras longas encontradas: {', '.join(palavras_longas)}")
else:
    print("Nenhuma palavra longa encontrada.")


