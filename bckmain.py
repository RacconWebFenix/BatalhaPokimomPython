import random
from personagem import Personagem
from pokimon import Pokimon
from treinamento import PokimonTreinado
import utils
import time
'''import pygame'''
'''import ascii

#Agradecimento especial
url7 = 'https://media-exp1.licdn.com/dms/image/C5603AQHCwoSDIiHTvg/profile-displayphoto-shrink_800_800/0/1618974047796?e=1628121600&v=beta&t=3a-Iu0M4bliPUwRMKWL62FQ84ZWlRtHe0sDnbgWc45E'

output7 = ascii.loadFromUrl(url7)

#POKEBOLA
url1 = 'https://1.bp.blogspot.com/_KBmmkCxTLY8/TMBfCU6xtBI/AAAAAAAAAFI/Ia5W4Suucww/s1600/kawax-pokeball-3097.png'
output1 = ascii.loadFromUrl(url1)

#ASH
url2 = 'https://i.pinimg.com/originals/8f/0c/42/8f0c42e4b5ffd76f3863950582070c1c.png'
output2 = ascii.loadFromUrl(url2)

#MYSTI
url3 = 'https://static.wikia.nocookie.net/pocketmonster/images/f/f0/Misty.png/revision/latest?cb=20160607230147&path-prefix=pt-br'
output3 = ascii.loadFromUrl(url3)
#Condição de Vitória
url4 = 'https://www.acasadocogumelo.com/wp-content/uploads/2015/02/happy_pokemon.png'
output4 = ascii.loadFromUrl(url4)

#Participação especial
url5 = 'https://avatars.githubusercontent.com/u/70485830?v=4'
output5 = ascii.loadFromUrl(url5)

#Condição de Derrota
url6 = 'https://www.criatives.com.br/wp-content/uploads/2012/01/3227198501_8315360dde_o.jpeg'

output6 = ascii.loadFromUrl(url6)
''' '''
pygame.init()
pygame.mixer.music.load('inicio.ogg')
pygame.mixer.music.play()
pygame.event.wait()'''

pikachu = Pokimon('PIKACHU', 50, 15, 5)
charmander = Pokimon('CHARMANDER', 50, 15, 5)
bulbasaur = Pokimon('BULBASAUR', 50, 15, 5)
staryu = Pokimon('STARYU', 50, 15, 5)
gyarados = Pokimon('GYARADOS', 50, 15, 5)
lapras = Pokimon('LAPRAS', 50, 15, 5)

pokimonAleatorio = [charmander, bulbasaur, gyarados, lapras]

#Quando for segunda batalha
pokimonsTreinados = []
pokimonsTreinados.append(
    PokimonTreinado(charmander.getNome(), charmander.getHp(),
                    charmander.getAtaque(), charmander.getDefesa(), 10))
pokimonsTreinados.append(
    PokimonTreinado(lapras.getNome(), lapras.getHp(), lapras.getAtaque(),
                    lapras.getDefesa(), 10))
pokimonsTreinados.append(
    PokimonTreinado(gyarados.getNome(), gyarados.getHp(), gyarados.getAtaque(),
                    gyarados.getDefesa(), 10))
pokimonsTreinados.append(
    PokimonTreinado(bulbasaur.getNome(), bulbasaur.getHp(),
                    bulbasaur.getAtaque(), bulbasaur.getDefesa(), 10))

#Valores dos laços While
#inicio do game 0
#Menu de Batalha 1
#Tela de Treinamento 2
#status inicial do personagem  e menu do jogo 3
#Descansar 4
#Ver Pokimons 5

inicioGame = 0
###########################INICIO DO JOGO#######################################################
while inicioGame == 0:
    ash = Personagem('ASH', 3, 100, 100)
    misty = Personagem('MISTY', 3, 100, 100)
    ash.adicionar_pokemon(pikachu)
    misty.adicionar_pokemon(staryu)
    print('Carregando jogo...')
    utils.clear_screen()
    print('Bem - vindo ao jogo de captura de pokimons')
    print('Por favor selecione seu personagem:\n1 - ASH\n2 - MISTY\n ')
    personagem = ash
    x = personagem.resposta()
    if x == 1:
        utils.clear_screen()
        personagem = ash

        print(f'Você escolheu o {personagem.getNome()}')
        print('Localizando pokimons...')

        inicioGame = 1
    elif x == 2:
        utils.clear_screen()

        personagem = misty
        print('Localizando pokimons...')

        print(f'Você escolheu a {personagem.getNome()}')
        inicioGame = 1
    else:
        print('\033[1;91mOpção Inválida\033[m')
        time.sleep(2)
    while inicioGame == 1:
        hpGlobalPkl1 = 50
        hpGlobalPkl2 = 70
        ###########################STATUS INICIAL#######################################################
        if len(personagem.pokemons) >= 3:
            print('!!!!!!!!!PARABÉNS!!!!!!!!!!!!!!!')
            print(
                '!!!!!!!!!!!!!!!!Você conseguiu capturar 3 pokimons!!!!!!!!!!!!!'
            )
            break
        elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(
                personagem.pokemons) < 1 and personagem.getEstamina(
                ) <= 0 or personagem.getVida() <= 0 or personagem.getDinheiro(
                ) <= 0 and len(personagem.pokemons) <= 0:
            print('Nao é possivel continuar o jogo!')
            print('Reiniciando...')
            utils.clear_screen()
            inicioGame = 0
        else:
            print('Instruções de jogo.')
            print('Durante a procura de pokinons')
            utils.clear_screen()
            print('!!!ATRIBUTOS DO PERSONAGEM!!!')
            print(
                f'Nome: {personagem.getNome()} Vida: {personagem.getVida()} Estamina: {personagem.getEstamina()} Dinheiro: {personagem.getDinheiro()}'
            )
            print('POKIMON:')
            for v in personagem.pokemons:
                print(
                    f'Nome: {v.getNome()} HP: {v.getHp()} Ataque: {v.getAtaque()} Defesa: {v.getDefesa()}'
                )
            print('Escolha uma opção:')
            print('1 - Procurar pokimon (Gasta 25 de Estamina)')
            print('2 - Treinar pokimon (Gasta 50 de Dinheiro)')
            print(
                '3 - Descansar (Gasta 50 de Dinheiro e recupera 70 de HP para 1 Pokimon)'
            )
            print('4 - Comprar Pokimom (Gasta 100 de Dinheiro)')
            print('5 - Ver seus Pokimons')
            print('6 - Ver participação especial!')
            print('7 - Ver agradecimento especial!')
            x = personagem.resposta()
            if x == 1:
                testeDeForca = 0
                for v in personagem.pokemons:
                    if v.getAtaque() > 15:
                        testeDeForca = 1
                    else:
                        testeDeForca = 0

                if testeDeForca == 0:
                    inicioGame = 2
                    while inicioGame == 2:
                        if personagem.getVida() <= 0 or len(
                                personagem.pokemons
                        ) == 0 or personagem.getEstamina() < 25:
                            print(
                                'Seu personagem não possui pokemons, vidas ou stamina suficientes'
                            )
                            inicioGame = 1
                        else:
                            telaDeBatalha = 0
                            while telaDeBatalha == 0:
                                utils.clear_screen()
                                print('!!!ATRIBUTOS DO PERSONAGEM!!!')
                                print(
                                    f'Nome: {personagem.getNome()} Vida: {personagem.getVida()} Estamina: {personagem.getEstamina()} Dinheiro: {personagem.getDinheiro()}'
                                )
                                print()
                                print('---POKIMONS---')
                                for v in personagem.pokemons:
                                    print(
                                        f'Nome: {v.getNome()} HP: {v.getHp()} Ataque: {v.getAtaque()} Defesa: {v.getDefesa()}'
                                    )
                                print('---POKIMONS---')
                                print()
                                print('!!!BEM VINDO AO MENU DE BATALHA!!!\n')
                                print('Você deseja procurar pokimons?')
                                print('1 - Sim\n2 - Não')
                                x = personagem.resposta()
                                if x == 1:
                                    lutando = 0
                                    while lutando == 0:
                                        random.shuffle(pokimonAleatorio)
                                        pokimon_encontrado = pokimonAleatorio[
                                            0]
                                        utils.clear_screen()
                                        utils.listaPokimons(personagem)
                                        while lutando == 0:
                                            lutando = 0
                                            utils.clear_screen()
                                            print(
                                                f'{personagem.getNome()} busca por Pokimons, ao se deparar com um {pokimon_encontrado.getNome()} selvagem, \033[1;31m{utils.reacaoDosPokimons()}\033[m e vai em sua direção.\n'
                                            )
                                            print(
                                                'O que você deseja fazer?\n\033[0;31m1 - Atacar\033[m\n\033[0;92m2 - Correr\n\033[m'
                                            )
                                            escolha_personagem = personagem.resposta(
                                            )
                                            if escolha_personagem == 1:
                                                utils.clear_screen()
                                                lutando = 2
                                                while lutando == 2:
                                                    #testar a força para decidir qual pokemom ira ser encontrado
                                                    print(
                                                        'Preare-se para batalha!'
                                                    )
                                                    pokimonEscolhido = personagem.escolhaDePokimons(
                                                    )
                                                    pokimonEncontrado = pokimonAleatorio[
                                                        0]
                                                    batalha = 0
                                                    while batalha == 0:
                                                        utils.clear_screen()
                                                        print(
                                                            f'Status do Pokimon do personagem {personagem.getNome()} - Nome: {pokimonEscolhido.getNome()} HP: {pokimonEscolhido.getHp()} Ataque: {pokimonEscolhido.getAtaque()} Defesa: {pokimonEscolhido.getDefesa()}'
                                                        )
                                                        print(
                                                            f'Status do Pokimon encontrado - Nome: {pokimonEncontrado.getNome()} HP: {pokimonEncontrado.getHp()} Ataque: {pokimonEncontrado.getAtaque()} Defesa: {pokimonEncontrado.getDefesa()}'
                                                        )
                                                        print(
                                                            f'O Pokimon {pokimonEncontrado.getNome()} {utils.reacaoDosPokimons()}'
                                                        )
                                                        print(
                                                            'O que você deseja fazer?\n\033[0;31m1 - Atacar\033[m\n\033[0;92m2 - Correr\n\033[m'
                                                        )
                                                        resp = personagem.resposta(
                                                        )
                                                        if resp == 1:
                                                            utils.clear_screen(
                                                            )
                                                            dano = pokimonEscolhido.atacar(
                                                                pokimonEncontrado
                                                            )
                                                            recebeDano = pokimonEncontrado.receberDano(
                                                                pokimonEncontrado,
                                                                dano)
                                                            print(
                                                                f'dano causado no pokimon encontrado: {dano}'
                                                            )
                                                            print(
                                                                'batalha acontece'
                                                            )
                                                            #verificado ate aki
                                                            time.sleep(4)
                                                        elif resp == 2:
                                                            utils.clear_screen(
                                                            )
                                                            print(
                                                                f'{personagem.getNome()} percebeu que esta fraco e fugiu da batalha.'
                                                            )
                                                            print(
                                                                f'{personagem.getNome()} perdeu 25 de Stamina'
                                                            )
                                                            time.sleep(2)
                                                            batalha = 1
                                                            lutando = 30
                                                        else:
                                                            utils.clear_screen(
                                                            )
                                                            print(
                                                                '\033[0;31mOpção inválida\033[m'
                                                            )
                                                            time.sleep(2)
                                            elif escolha_personagem == 2:
                                                print(
                                                    f'\033[0;31m{personagem.getNome()} ficou com medo e fugiu da batalha.\033[m'
                                                )
                                                time.sleep(2)
                                                lutando = 1
                                                inicioGame = 1
                                                break
                                            else:
                                                print(
                                                    '\033[0;31mOpção inválida.\033[m'
                                                )
                                                time.sleep(2)

                                elif x == 2:
                                    print(
                                        '\033[0;37mVocê decidiu não procurar por pokimons agora.\033[m'
                                    )
                                    time.sleep(2)
                                    lutando = 1
                                    inicioGame = 1
                                    break
                                else:
                                    print('\033[0;31mOpção inválida.\033[m')
                                    time.sleep(2)
