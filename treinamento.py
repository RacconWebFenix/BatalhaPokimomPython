from pokimon import Pokimon



class PokimonTreinado(Pokimon):
    def __init__(self, nome, hp, ataque, defesa, treinamento):
        self.__Treinamento = treinamento
        super().__init__(nome, hp, ataque, defesa)

    def getTreinamento(self):
        return self.__Treinamento

    def setTreinamento(self, treinamento):
        self.__Treinamento = treinamento
    
    def get_ataque(self):
        return super().get_ataque() + self.__Treinamento * 2
    
    def get_defesa(self):
        return super().get_defesa() + self.__Treinamento + 5
 
