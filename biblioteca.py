class Pessoa:
    def __init__(self, nome, peso, idade, falando, dormindo, comendo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = falando
        self.dormindo = dormindo
        self.comendo = comendo
    def falar(self):
        if self.comendo and self.dormindo == True:
            print(f"{self.nome} não está falando!")

    def comer(self):
        print(f"{self.nome} está comendo!")

    def dormir(self):
        #acordar
        print(f"{self.nome} está dormindo!")