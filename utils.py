from pokimon import Pokimon
import os, sys
import personagem
import pokimon
import random
import utils
import time

hpGlobalPkl1 = 50
hpGlobalPkl2 = 70


def listaPokimons(personagem):
    count = 0
    for v in personagem.pokemons:
        count += 1
        print(
            f'{count} - Nome: {v.getNome()} HP: {v.getHp()} Ataque: {v.getAtaque()} Defesa: {v.getDefesa()}'
        )


def clear_screen():  #Simple function that clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')


def reacaoDosPokimons():
    reacaoAleatoria = ['Rosna', 'Grita', 'Pisca', 'Pula', 'Dança', 'Corre']
    random.shuffle(reacaoAleatoria)
    return reacaoAleatoria[0]


def resposta():
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


def resultadoDeBatalha(pokimonEscolhido, pokimonEncontrado, personagem):
    if pokimonEscolhido.getHp() <= 0 and pokimonEncontrado.getHp() >= 1:
        print('Você perdeu a batalha')
        x = personagem.getVida() - 1
        personagem.setVida(x)
        print(
            f'{personagem.getNome()} perdeu 1 de vida e o Pokimon {pokimonEscolhido.getNome()}'
        )
        personagem.remover_pokemon(pokimonEscolhido)
        time.sleep(4)
        resultado = 1
        return resultado
    elif pokimonEncontrado.getHp() <= 0 and pokimonEscolhido.getHp() >= 1:
        print('Você venceu a batalha')
        x = personagem.getDinheiro() + 25
        personagem.setDinheiro(x)
        pokimonEncontrado.setHp(hpGlobalPkl1)
        time.sleep(4)
        utils.clear_screen()
        personagem.adicionar_pokemon(pokimonEncontrado)
        print(
            f'{personagem.getNome()} ganhou 25 de dinheiro e o Pokimon {pokimonEncontrado.getNome()}'
        )
        time.sleep(4)
        resultado = 2
        return resultado
    elif pokimonEncontrado.getHp() <= 0 and pokimonEscolhido.getHp() <= 0:
        print(
            f'Em uma batalha épica, {pokimonEncontrado.getNome()} e {pokimonEscolhido.getNome()} usaram todas as suas forças e os dois foram mortos em uma explosão de seus próprios poderes'
        )
        time.sleep(2)
        print(
            f'Com suas forças esgotadas o Pokimon {pokimonEscolhido.getNome()} se levanta porém seus machucados o impedem de contiuar a batalha.'
        )
        pokimonEscolhido.setHp(1)
        time.sleep(3)
        utils.clear_screen()
        resultado = 3
        return resultado
    else:
        resultado = 0
        return resultado


def instanciaDePokimons():
    pikachu = Pokimon('PIKACHU', 50, 15, 5)
    staryu = Pokimon('STARYU', 50, 15, 5)
    charmander = Pokimon('CHARMANDER', 50, 15, 5)
    bulbasaur = Pokimon('BULBASAUR', 50, 15, 5)
    gyarados = Pokimon('GYARADOS', 50, 15, 5)
    lapras = Pokimon('LAPRAS', 50, 15, 5)
    pokimonAleatorioSelvagem = [
        pikachu, staryu, charmander, bulbasaur, gyarados, lapras
    ]
    return pokimonAleatorioSelvagem


def condicaoVitoriaDerrota(personagem):
    if personagem.getVida() <= 0:
        return 0
    elif len(personagem.pokemons) <= 0 and personagem.getDinheiro() < 1:
        return 1
    elif len(personagem.pokemons) >= 5:
        return 2
    else:
        return 3