import random
import funcImagens
import funcSonsPokimons



class Pokimon:
    def __init__(self, nome, hp, ataque, defesa, img, som):
        self.__nome = nome
        self.__hp = hp
        self.__ataque = ataque
        self.__defesa = defesa
        self.__img = img
        self.__som = som

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
    
    def getSom(self):
        return self.__som

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
    
    def setImg(self, som):
        self.__som = som
    
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

bulbasaurSom = funcSonsPokimons.bulbasaurSom 
charmanderSom = funcSonsPokimons.charmanderSom 
chikoritaSom = funcSonsPokimons.chikoritaSom
eeveeSom = funcSonsPokimons.eeveeSom 
pidgeotSom = funcSonsPokimons.pidgeotSom 
pikachuSom = funcSonsPokimons.pikachuSom 
snorlaxSom = funcSonsPokimons.snorlaxSom 
starlySom = funcSonsPokimons.starlySom 
staryuSom = funcSonsPokimons.staryuSom 
zubatSom = funcSonsPokimons.zubatSom

'''

pikachu = Pokimon('PIKACHU', 50, 17, 7, imgPikachu)
charmander = Pokimon('CHARMANDER', 50, 20, 7, imgCharmander)
bulbasaur = Pokimon('BULBASAUR', 50, 15, 5, imgBulbasaur)
staryu = Pokimon('STARYU', 55, 16, 6, imgStaryu)
snorlax = Pokimon('SNORLAX', 70, 10, 10, imgSnorlax)
starly = Pokimon('STARLY', 50, 14, 5, imgStarly)
eevee = Pokimon('EEVEE', 56, 13, 6, imgEevee)
pidgeotto = Pokimon('PIDGEOTTO', 55, 16, 6, imgPidgeotto)
zubat = Pokimon('ZUBAT', 50, 15, 5, imgZubat)
chicorita = Pokimon('CHICORITA', 55, 17, 4, imgChicorita)

'''