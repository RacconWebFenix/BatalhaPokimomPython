class Pokimon:
    def __init__(self, nome, hp, ataque, defesa):
        self.__nome = nome
        self.__hp = hp
        self.__ataque = ataque
        self.__defesa = defesa

    def get_nome(self):
        return self.__nome

    def get_hp(self):
        return self.__hp

    def get_ataque(self):
        return self.__ataque

    def get_defesa(self):
        return self.__defesa

    def set_nome(self, nome):
        self.__nome = nome

    def set_hp(self, hp):
        self.__hp = hp

    def set_ataque(self, ataque):
        self.__ataque = ataque

    def set_defesa(self, defesa):
        self.__defesa = defesa


pikachu = Pokimon('PIKACHU', 50, 15, 5)
charmander = Pokimon('CHARMANDER', 50, 15, 5)
bulbasaur = Pokimon('BULBASAUR', 50, 15, 5)
staryu = Pokimon('STARYU', 50, 15, 5)
gyarados = Pokimon('GYARADOS', 50, 15, 5)
lapras = Pokimon('LAPRAS', 50, 15, 5)
