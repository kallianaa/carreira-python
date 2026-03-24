class Epi:
    def __init__(self, nome, ca, ano_validade):
        self.nome = nome
        self.ca = ca
        self.ano_validade = ano_validade

    def exibir_dados(self):
        print("O EPI é: ", self.nome, "/ O número do CA é: ", self.ca, "/ O ano de validade é: ", self.ano_validade)

    def verificar_validade(self, ano_atual):
        if ano_atual > self.ano_validade:
            print("Atenção: Este EPI está vencido!")
        else:
            print("O EPI está dentro da validade.")


epi1 = Epi("Capacete", 12345, 2025)
epi1.verificar_validade(2026)
epi1.exibir_dados()

epi2 = Epi("Luva",67890, 2027)
epi2.exibir_dados()
epi2.verificar_validade(2026)
