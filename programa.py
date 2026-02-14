tituloLivro = "Dom Casmurro"
anoPublicacao = 1899
preco = 45.90
estaDisponivel = True
ano_atual = int(input("Qual é o ano atual? "))
idade_do_livro = ano_atual - anoPublicacao


print(f"Título: {tituloLivro} e o ano de lançamento {anoPublicacao}")
print(f"O livro tem {idade_do_livro} anos")

if estaDisponivel :
    print(f"O livro {tituloLivro} está disponivel")
else:
    print(f"O livro {tituloLivro} não está disponivel")


# if idade_do_livro >= 100:
#     print("Este livro é um clássico centenário!")
# else:
#     print("Este livro ainda não é centenário.")

if preco <= 30:
    print("Livro barato")
elif preco < 100:
    print("Preço razoável")
else:
    print("Livro caro")