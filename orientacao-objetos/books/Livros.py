class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)


    def __str__(self):
        return f'O livro: {self.titulo}, foi escrito por {self.autor} e foi publicado em {self.ano_publicacao}'

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_encontrados = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro.disponivel:
                livros_encontrados.append(livro)
        return livros_encontrados