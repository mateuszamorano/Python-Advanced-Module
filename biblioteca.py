class Pessoa: #não concluído
    def __init__(self, nome, peso, idade, dormindo = False, comendo = True, falando = True):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = falando
        self.dormindo = dormindo
        self.comendo = comendo
        if self.idade <= 2:
            print(f"{self.nome} ainda é um bebê, ou seja, não fala!")
        else:
            print(f"{self.nome} tem {self.idade} anos.")
        if self.dormindo == "Sim" or "sim" and self.comendo == "Não" or "não" and self.falando == "Não" and "não":
            print(f"O bebê está dormindo!")
        elif self.dormindo == "Não" or "não" and self.comendo == "Sim" or "sim" and self.falando == "Não" and "não":
            print("A pessoa está comendo!")
        elif self.dormindo == "Não" or "não" and self.comendo == "Não" or "não" and self.falando == "Sim" and "sim" and self.idade >= 2:
            print("A pessoa está falando!")
            
    def dormir(self):
        pass

    def comer(self):
        pass

    def falar(self):
        pass
