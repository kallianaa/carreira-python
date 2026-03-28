
class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self.titular} tem {self.saldo} reais'

    def ativar_conta(self):
        self._ativo = True


    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

class ClienteBanco:
    def __init__(self, nome, idade, cpf, email, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.conta = None

    def exibir_cliente(self):
        print(self.nome)

    def __str__(self):
        return f'O Cliente {self.nome} tem {self.idade} anos, possui o email: {self.email} e tem o telefone de contato: {self.telefone}'

    def adicionar_conta(self, conta_nova):
        self.conta = conta_nova

conta1 = ContaBancaria("Nala", 897)
cliente1 = ClienteBanco("Nala", 18, 12345678900, "emailnala@email.com", 51998877445)
cliente1.adicionar_conta(conta1)
print(cliente1.conta)
cliente2 = ClienteBanco("Maria", 25, 48765412399, "emailmaria@email.com", 51998452588)
print(cliente2)
cliente3 = ClienteBanco("katy", 18, 65478912300, "emailkaty@email.com", 51996785462)
print(cliente3)


conta2 = ContaBancaria("Pablo", 1545)
print(conta2)
conta3 = ContaBancaria("Thainá", 123)
conta3.ativar_conta()
print(conta3.ativo)