from Livros import Livro

livro_biblioteca = Livro("Sobre O Amor", "Bukowski", 2015)


livro_biblioteca.emprestar()

print(livro_biblioteca.disponivel)

livro_biblioteca2 = Livro("Fique comigo", "Harlan Coben", 2014)
print(livro_biblioteca2.disponivel)


lista_ano = Livro.verificar_disponibilidade(2014)

for livro in lista_ano:
    print(livro)