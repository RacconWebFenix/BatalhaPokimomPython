import random
import funcImagens




class Pokimon:
    def __init__(self, nome, hp, ataque, defesa, img):
        self.__nome = nome
        self.__hp = hp
        self.__ataque = ataque
        self.__defesa = defesa
        self.__img = img

    def getNome(self):
        return self.__nome

    def getHp(self):
        return self.__hp

    def getAtaque(self):
        return self.__ataque

    def getDefesa(self):
        return self.__defesa
    
    def getImg(self):
        return self.__img()

    def setNome(self, nome):
        self.__nome = nome

    def setHp(self, hp):
        self.__hp = hp

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa
    
    def setImg(self, img):
        self.__img = img()
    
    def atacar(self, pokimon):
        dano = self.getAtaque() - random.randint(1, pokimon.getDefesa())
        return dano
   
    def receberDano(self, pokimon, dano):
        resultado = pokimon.getHp() - dano
        return pokimon.setHp(resultado)



imgPikachu = funcImagens.imgPrintPikachu
imgCharmander = funcImagens.imgPrintCharmander
imgBulbasaur = funcImagens.imgPrintBulbasaur
imgStaryu = funcImagens.imgPrintStaryu
imgSnorlax = funcImagens.imgPrintSnorlax
imgStarly = funcImagens.imgPrintStarly
imgEevee = funcImagens.imgPrintEevee
imgPidgeotto = funcImagens.imgPrintPidgeotto
imgZubat = funcImagens.imgPrintZubat
imgChicorita = funcImagens.imgPrintChicorita



pikachu = Pokimon('PIKACHU', 50, 17, 7, imgPikachu)
charmander = Pokimon('CHARMANDER', 50, 20, 7, imgCharmander)
bulbasaur = Pokimon('BULBASAUR', 50, 15, 5, imgBulbasaur)
staryu = Pokimon('STARYU', 55, 16, 6, imgStaryu)
<<<<<<< HEAD
snorlax = Pokimon('SNORLAX', 70, 10, 10, imgSnorlax)
=======
snorlax = Pokimon('SNORLAX', 70, 10, 7, imgSnorlax)
>>>>>>> b9fa4b308c3edc5a1f701d79a2a75c4ec51d6e22
starly = Pokimon('STARLY', 50, 14, 5, imgStarly)
eevee = Pokimon('EEVEE', 56, 13, 6, imgEevee)
pidgeotto = Pokimon('PIDGEOTTO', 55, 16, 6, imgPidgeotto)
zubat = Pokimon('ZUBAT', 50, 15, 5, imgZubat)
chicorita = Pokimon('CHICORITA', 55, 17, 4, imgChicorita)

