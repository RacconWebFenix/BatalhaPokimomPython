import os,sys
import personagem
import pokimon
import random

def listaPokimons(personagem):
    count = 0
    for v in personagem.pokemons:
        count += 1
        print(f'{count} - Nome: {v.getNome()} HP: {v.getHp()} Ataque: {v.getAtaque()} Defesa: {v.getDefesa()}')

def clear_screen():  #Simple function that clears the screen
    os.system('cls' if os.name=='nt' else 'clear')

def reacaoDosPokimons():
    reacaoAleatoria = ['Rosna', 'Grita', 'Pisca', 'Pula', 'Dança', 'Corre']
    random.shuffle(reacaoAleatoria)
    return reacaoAleatoria[0]

