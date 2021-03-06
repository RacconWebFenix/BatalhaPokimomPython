import funcImagens


class Personagem():
    pokemons = []

    def __init__(self, nome, vida, dinheiro, estamina, img):
        self.__Nome = nome
        self.__Vida = vida
        self.__Dinheiro = dinheiro
        self.__Estamina = estamina
        self.__img = img
        self.pokemons = []

    def getNome(self):
        return self.__Nome

    def getVida(self):
        return self.__Vida

    def getDinheiro(self):
        return self.__Dinheiro

    def getEstamina(self):
        return self.__Estamina

    def getImg(self):
        return self.__img()

    def setNome(self, nome):
        self.__Nome = nome

    def setVida(self, vida):
        self.__Vida = vida

    def setDinheiro(self, dinheiro):
        self.__Dinheiro = dinheiro

    def setEstamina(self, estamina):
        self.__Estamina = estamina

    def setImg(self, img):
        self.__img = img()

    def adicionar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def remover_pokemon(self, pokemon):
        self.pokemons.remove(pokemon)

    def resposta(self):
        ok = False
        while True:
            x = str(input('Resposta: '))
            if x.isnumeric():
                x = int(x)
                ok = True
            else:
                print('\033[0;31mErro! Digite um número Inteiro Válido.\033[m')
            if ok:
                break
        return x

    def escolhaDePokimons(self):
        pokimonEscolhido = []
        count = 0
        print('Escolha um de seus Pokimons.')
        for v in self.pokemons:
            count += 1
            print(
                f'\033[1;37mPOKIMON: {count} -  Nome: {v.getNome()} HP: {v.getHp()} Ataque: {v.getAtaque()} Defesa: {v.getDefesa()}'
            )
        ok = False
        while True:
            x = str(input('Resposta: '))
            if x.isnumeric():
                x = int(x)
                if x - 1 > len(self.pokemons) - 1 or x == 0:
                    print(
                        '\033[0;31mErro! Não existe Pokimons para o valor digitado.\033[m'
                    )
                else:
                    pokimonEscolhido = self.pokemons[x - 1]
                    ok = True
                    return pokimonEscolhido
            if ok:
                break
            else:
                print('\033[0;31mErro! Digite um número Inteiro Válido.\033[m')
        return x


imgAsh = funcImagens.imgPrintAsh
imgMisy = funcImagens.imgPrintMisty
