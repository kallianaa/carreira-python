class veiculo(object):
    def motor(self):
        print("motor do veículo")


class carro(veiculo):
    def __init__(self, cor, potencia, modelo, marca):
        self.cor = cor
        self.potencia = potencia
        self.modelo = modelo
        self.marca = marca


    def acelerar(self):
      print("Vrummm")


    def freiar(self):
      print("parando")

