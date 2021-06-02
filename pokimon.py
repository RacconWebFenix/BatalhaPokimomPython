import random

class Pokimon:
    def __init__(self, nome, hp, ataque, defesa):
        self.__nome = nome
        self.__hp = hp
        self.__ataque = ataque
        self.__defesa = defesa

    def getNome(self):
        return self.__nome

    def getHp(self):
        return self.__hp

    def getAtaque(self):
        return self.__ataque

    def getDefesa(self):
        return self.__defesa

    def setNome(self, nome):
        self.__nome = nome

    def setHp(self, hp):
        self.__hp = hp

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa
    
    def atacar(self, pokimon):
        dano = self.getAtaque() - random.randint(1, pokimon.getDefesa())
        return dano
   
    def receberDano(self, pokimon, dano):
        resultado = pokimon.getHp() - dano
        return pokimon.setHp(resultado)

pikachu = Pokimon('PIKACHU', 50, 15, 5)
charmander = Pokimon('CHARMANDER', 50, 15, 5)
bulbasaur = Pokimon('BULBASAUR', 50, 15, 5)
staryu = Pokimon('STARYU', 50, 15, 5)
gyarados = Pokimon('GYARADOS', 50, 15, 5)
lapras = Pokimon('LAPRAS', 50, 15, 5)
