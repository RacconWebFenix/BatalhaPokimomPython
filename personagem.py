class Personagem():
    pokemons = []

    def __init__(self, nome, vida, dinheiro, estamina):
        self.__Nome = nome
        self.__Vida = vida
        self.__Dinheiro = dinheiro
        self.__Estamina = estamina
        self.pokemons = []

    def getNome(self):
        return self.__Nome

    def getVida(self):
        return self.__Vida

    def getDinheiro(self):
        return self.__Dinheiro

    def getEstamina(self):
        return self.__Estamina
    
    def setNome(self, nome):
        self.__Nome = nome

    def setVida(self, vida):
        self.__Vida = vida

    def setDinheiro(self, dinheiro):
        self.__Dinheiro = dinheiro

    def setEstamina(self, estamina):
        self.__Estamina = estamina

    def adicionar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def remover_pokemon(self, pokemon):
        self.pokemons.remove(pokemon)


ash = Personagem('ASH', 3, 100, 100)
misty = Personagem('MISTY', 3, 100, 100)

