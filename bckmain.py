import random
from personagem import Personagem
from pokimon import Pokimon
from treinamento import PokimonTreinado
import utils
import time
import pygame
import ascii

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


pygame.init()
pygame.mixer.music.load('inicio.ogg')
pygame.mixer.music.play()
pygame.event.wait()

pikachu = Pokimon('PIKACHU', 50, 15, 5)
charmander = Pokimon('CHARMANDER', 50, 15, 5)
bulbasaur = Pokimon('BULBASAUR', 50, 15, 5)
staryu = Pokimon('STARYU', 50, 15, 5)
gyarados = Pokimon('GYARADOS', 50, 15, 5)
lapras = Pokimon('LAPRAS', 50, 15, 5)



#Quando for segunda batalha
pokimonsTreinados = []
pokimonsTreinados.append(
    PokimonTreinado(charmander.get_nome(), charmander.get_hp(),
                    charmander.get_ataque(), charmander.get_defesa(), 10))
pokimonsTreinados.append(
    PokimonTreinado(lapras.get_nome(), lapras.get_hp(), lapras.get_ataque(),
                    lapras.get_defesa(), 10))
pokimonsTreinados.append(
    PokimonTreinado(gyarados.get_nome(), gyarados.get_hp(),
                    gyarados.get_ataque(), gyarados.get_defesa(), 10))
pokimonsTreinados.append(
    PokimonTreinado(bulbasaur.get_nome(), bulbasaur.get_hp(),
                    bulbasaur.get_ataque(), bulbasaur.get_defesa(), 10))

reacao_aleatoria_pokimon = ['rosna', 'grita', 'pisca', 'pula']
random.shuffle(reacao_aleatoria_pokimon)
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
    hpPokimonSemTreinamento = 50
    hpPokimonTreinado = 70
    print('Carregando jogo...')
    time.sleep(6)
    utils.clear_screen()
    print(output1)
    print('Bem - vindo ao jogo de captura de pokimons')
    personagem = int(
        input(
            'Por favor selecione seu personagem:\n1 - ASH\n2 - MISTY\nResposta: '
        ))
    if personagem == 1:
        utils.clear_screen()
        personagem = ash
        print(output2)
        print(f'Você escolheu o {personagem.getNome()}')
        print('Localizando pokimons...')
        time.sleep(5)
        inicioGame = 1
    elif personagem == 2:
        utils.clear_screen()
        print(output3)
        personagem = misty
        print('Localizando pokimons...')
        time.sleep(5)
        print(f'Você escolheu a {personagem.getNome()}')
        inicioGame = 1
    else:
        utils.clear_screen()
        print('Opção Invalida.')
    while inicioGame == 1:
        ###########################STATUS INICIAL#######################################################
        if len(personagem.pokemons) >= 3:
            print('!!!!!!!!!PARABÉNS!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!!!!!!!Você conseguiu capturar 3 pokimons!!!!!!!!!!!!!')
            print(output4)
            time.sleep(6)
            break
        elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(personagem.pokemons) < 1 and personagem.getEstamina() <= 0 or personagem.getVida() <= 0 or personagem.getDinheiro() <= 0 and len(personagem.pokemons) <= 0:
            print('Nao é possivel continuar o jogo!')
            print('Reiniciando...')
            print(url6)
            time.sleep(3)
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
                    f'Nome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
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
            x = int(input('Resposta: '))
            if x == 1:
                testeDeForca = 0
                for v in personagem.pokemons:
                    if v.get_ataque() > 15:
                        testeDeForca = 1
                    else:
                        testeDeForca = 0

                if testeDeForca == 0:
###########################################MENU DE BATALHA#######################################################
                    inicioGame = 2
                    while inicioGame == 2:
                        if personagem.getVida() <= 0 or len(
                                personagem.pokemons
                        ) == 0 or personagem.getEstamina() < 25:
                            print(
                                'Seu personagem não possui pokemons, vidas ou stamina suficientes'
                            )
                            time.sleep(2)
                            inicioGame = 1
                        else:
                            telaDeBatalha = 0
                            while telaDeBatalha == 0:
                                pikachu = Pokimon('PIKACHU', 50, 15, 5)
                                charmander = Pokimon('CHARMANDER', 50, 15, 5)
                                bulbasaur = Pokimon('BULBASAUR', 50, 15, 5)
                                staryu = Pokimon('STARYU', 50, 15, 5)
                                gyarados = Pokimon('GYARADOS', 50, 15, 5)
                                lapras = Pokimon('LAPRAS', 50, 15, 5)
                                pokimon_aleatorio = [
                                    charmander, bulbasaur, gyarados, lapras
                                ]
                                utils.clear_screen()
                                print('!!!ATRIBUTOS DO PERSONAGEM!!!')
                                print(
                                    f'Nome: {personagem.getNome()} Vida: {personagem.getVida()} Estamina: {personagem.getEstamina()} Dinheiro: {personagem.getDinheiro()}'
                                )
                                print()
                                print('---POKIMONS---')
                                for v in personagem.pokemons:
                                    print(
                                        f'Nome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                                    )
                                print('---POKIMONS---')
                                print()
                                print('!!!BEM VINDO AO MENU DE BATALHA!!!\n')
                                print('Você deseja procurar pokimons?')
                                print('1 - Sim / 2 - Não')
                                y = int(input('Resposta: '))
                                utils.clear_screen()
                                if y != 1:
                                    lutando = 10
                                    telaDeBatalha = 10
                                    inicioGame = 1
                                    qtdBatalha2 = 0
                                elif len(personagem.pokemons) >= 3:
                                    print('!!!!!!!!!PARABÉNS!!!!!!!!!!!!!!!')
                                    print('Você conseguir 3 pokimons!!!!!!!!!!!!!1')
                                    time.sleep(5)
                                    print(output4)
                                    break
                                elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(personagem.pokemons) < 1 and personagem.getEstamina() <= 0 or personagem.getVida() <= 0:
                                    print('Nao é possivel continuar o jogo!')
                                    print('Reiniciando...')
                                    print(output6)
                                    time.sleep(3)
                                    utils.clear_screen()
                                    inicioGame = 0
                                elif y == 1:
                                    gastoStamina = personagem.getEstamina() - 25
                                    personagem.setEstamina(gastoStamina)
                                    telaDeBatalha = 1
    #PRIMEIR BATALHA###############################################PRIMEIRA BATALHA##############################################################
                                    qtdBatalha2 = 0
                                    while telaDeBatalha == 1:
                                        if qtdBatalha2 < 2:
                                            pokimon_aleatorio = [
                                                charmander, bulbasaur, gyarados, lapras
                                            ]
                                            random.shuffle(pokimon_aleatorio)
                                            reacao_aleatoria_pokimon = [
                                                'rosna', 'grita', 'pisca', 'pula'
                                            ]
                                            random.shuffle(pokimon_aleatorio)
                                            random.shuffle(reacao_aleatoria_pokimon)
                                            pokimon_encontrado = pokimon_aleatorio[0]
                                            print(
                                                f'Você encontrou o pokimon {pokimon_encontrado.get_nome()}'
                                            )
                                            print('Deseja atacar?\n1 - sim\n2 - não')
                                            atacar = int(input('Resposta: '))
                                            if atacar == 1:
                                                utils.clear_screen()
                                                if len(personagem.pokemons) > 1:
    #########################Personagem com 2 Pokimons###############################################################################
                                                    print('Escolha um de seus Pokimons:')
                                                    count = 0
                                                    for v in personagem.pokemons:
                                                        count += 1
                                                        print(f'POKIMON: {count} - {v.get_nome()} HP:{v.get_hp()} Ataque:{v.get_ataque()} Defesa:{v.get_defesa()}')
                                                    pokimon_escolhido = int(input('Resposta: '))
                                                    if pokimon_escolhido == 1:
    #########################Condição de Pokimon na posição 0 ###############################################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            0]
                                                        utils.clear_screen()
                                                        print(
                                                            f'Status do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'O Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    'O que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
                                                                ))
                                                            if escolha_personagem == 1:
    #########################Escolha do personagem Atacar##############################################################
                                                                utils.clear_screen()
                                                                defesaTotalEncontrado = pokimon_encontrado.get_defesa(
                                                                )
                                                                danoPokimonEscolhio = pokimon_para_batalha.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEncontrado
                                                                )
                                                                inserindoDano = pokimon_encontrado.get_hp(
                                                                ) - danoPokimonEscolhio
                                                                pokimon_encontrado.set_hp(
                                                                    inserindoDano)
                                                                defesaTotalEscolhido = pokimon_para_batalha.get_defesa(
                                                                )
                                                                danoPokimonEncontrado = pokimon_encontrado.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEscolhido
                                                                )
                                                                inserindoDano = pokimon_para_batalha.get_hp(
                                                                ) - danoPokimonEncontrado
                                                                pokimon_para_batalha.set_hp(
                                                                    inserindoDano)
                                                                print(
                                                                    f'Seu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'O pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonSemTreinamento
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'O pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(4)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                                    qtdBatalha2 = 0
                                                                if pokimon_para_batalha.get_hp(
                                                                ) > 1:
                                                                    print(
                                                                        f'O seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'O pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu 1 vida!'
                                                                    )
                                                                    personagem.remover_pokemon(
                                                                        pokimon_para_batalha
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(3)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                            elif escolha_personagem == 2:
                                                                print(
                                                                    'Você correu da batalha!'
                                                                )
                                                                lutando = 1
                                                    elif pokimon_escolhido == 2:
    ##############################Escolha do personagem segundo pokimon POKIMON LISTA COM 2########################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            1]
                                                        utils.clear_screen()
                                                        print(
                                                            f'Status do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'O Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    'O que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
                                                                ))
                                                            if escolha_personagem == 1:
    #########################Escolha do personagem Atacar##############################################################
                                                                utils.clear_screen()
                                                                defesaTotalEncontrado = pokimon_encontrado.get_defesa(
                                                                )
                                                                danoPokimonEscolhio = pokimon_para_batalha.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEncontrado
                                                                )
                                                                inserindoDano = pokimon_encontrado.get_hp(
                                                                ) - danoPokimonEscolhio
                                                                pokimon_encontrado.set_hp(
                                                                    inserindoDano)
                                                                defesaTotalEscolhido = pokimon_para_batalha.get_defesa(
                                                                )
                                                                danoPokimonEncontrado = pokimon_encontrado.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEscolhido
                                                                )
                                                                inserindoDano = pokimon_para_batalha.get_hp(
                                                                ) - danoPokimonEncontrado
                                                                pokimon_para_batalha.set_hp(
                                                                    inserindoDano)
                                                                print(
                                                                    f'Seu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'O pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonSemTreinamento
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'O pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
                                                                    )
    ####################################RESLTADO DE BATALHA COM O SEGUNDO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(4)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                                    qtdBatalha2 = 0
                                                                if pokimon_para_batalha.get_hp(
                                                                ) > 1:
                                                                    print(
                                                                        f'O seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'O pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu 1 vida!'
                                                                    )
                                                                    personagem.remover_pokemon(
                                                                        pokimon_para_batalha
                                                                    )
    ####################################RESLTADO DE BATALHA COM O SEGUNDO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(3)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                            elif escolha_personagem == 2:
                                                                print(
                                                                    'Você correu da batalha!'
                                                                )
                                                                time.sleep(2)
                                                                lutando = 10
                                                                telaDeBatalha = 10
                                                                inicioGame = 1
    ####################################Ataque com 1 pokimom#####################################################################################################################################################################################################
                                                else:
                                                    lutando = 0
                                                    while lutando == 0:
    #########################Condição de Pokimon na posição 0 ###############################################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            0]
                                                        utils.clear_screen()
                                                        print(
                                                            f'Status do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'O Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    'O que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
                                                                ))
                                                            if escolha_personagem == 1:
    #########################Escolha do personagem Atacar##############################################################
                                                                utils.clear_screen()
                                                                defesaTotalEncontrado = pokimon_encontrado.get_defesa(
                                                                )
                                                                danoPokimonEscolhio = pokimon_para_batalha.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEncontrado
                                                                )
                                                                inserindoDano = pokimon_encontrado.get_hp(
                                                                ) - danoPokimonEscolhio
                                                                pokimon_encontrado.set_hp(
                                                                    inserindoDano)
                                                                defesaTotalEscolhido = pokimon_para_batalha.get_defesa(
                                                                )
                                                                danoPokimonEncontrado = pokimon_encontrado.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEscolhido
                                                                )
                                                                inserindoDano = pokimon_para_batalha.get_hp(
                                                                ) - danoPokimonEncontrado
                                                                pokimon_para_batalha.set_hp(
                                                                    inserindoDano)
                                                                print(
                                                                    f'Seu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'O pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonSemTreinamento
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'O pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(4)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                                    qtdBatalha2 = 0
                                                                if pokimon_para_batalha.get_hp(
                                                                ) > 1:
                                                                    print(
                                                                        f'O seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'O pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu 1 vida!'
                                                                    )
                                                                    personagem.remover_pokemon(
                                                                        pokimon_para_batalha
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(3)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                            elif escolha_personagem == 2:
                                                                print(
                                                                    'Você correu da batalha!'
                                                                )
                                                                lutando = 1
                                            else:
                                                print('Você correu da batalha!')
                                                time.sleep(2)
                                                lutando = 10
                                                telaDeBatalha = 10
                                                inicioGame = 1
                                        else:
                                            print('Você correu da batalha!')
                                            time.sleep(2)
                                            lutando = 10
                                            telaDeBatalha = 10
                                            inicioGame = 1
                else:
                    inicioGame = 7
                    while inicioGame == 7:
                        if personagem.getVida() <= 0 or len(
                                personagem.pokemons
                        ) == 0 or personagem.getEstamina() < 25:
                            print(
                                'Seu personagem não possui pokemons, vidas ou stamina suficientes'
                            )
                            time.sleep(2)
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
                                        f'Nome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                                    )
                                print('---POKIMONS---')
                                print()
                                print('!!!BEM VINDO AO MENU DE BATALHA!!!\n')
                                print('Você deseja procurar pokimons?')
                                print('1 - Sim / 2 - Não')
                                y = int(input('Resposta: '))
                                utils.clear_screen()
                                if y != 1:
                                    lutando = 10
                                    telaDeBatalha = 10
                                    inicioGame = 1
                                    qtdBatalha2 = 0
                                elif len(personagem.pokemons) >= 3:
                                    print('!!!!!!!!!PARABÉNS!!!!!!!!!!!!!!!')
                                    print('Você conseguir 3 pokimons!!!!!!!!!!!!!1')
                                    time.sleep(5)
                                    print(output4)
                                    break
                                elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(personagem.pokemons) < 1 and personagem.getEstamina() <= 0 or personagem.getVida() <= 0:
                                    print('Nao é possivel continuar o jogo!')
                                    print('Reiniciando...')
                                    print(output6)
                                    time.sleep(3)
                                    utils.clear_screen()
                                    inicioGame = 0
                                elif y == 1:
                                    gastoStamina = personagem.getEstamina() - 25
                                    personagem.setEstamina(gastoStamina)
                                    telaDeBatalha = 1
    #PRIMEIR BATALHA###############################################PRIMEIRA BATALHA##############################################################
                                    qtdBatalha2 = 0
                                    while telaDeBatalha == 1:
                                        if qtdBatalha2 < 2:
                                            pokimonAleatorioTreinado = pokimonsTreinados
                                            for v in pokimonsTreinados:
                                                v.set_hp(70)
                                            random.shuffle(pokimonAleatorioTreinado)
                                            reacao_aleatoria_pokimon = [
                                                'rosna', 'grita', 'pisca', 'pula'
                                            ]
                                            random.shuffle(pokimonAleatorioTreinado)
                                            random.shuffle(reacao_aleatoria_pokimon)
                                            pokimon_encontrado = pokimonAleatorioTreinado[0]
                                            print(
                                                f'Você encontrou o pokimon {pokimon_encontrado.get_nome()}'
                                            )
                                            print('Deseja atacar?\n1 - sim\n2 - não')
                                            atacar = int(input('Resposta: '))
                                            if atacar == 1:
                                                utils.clear_screen()
                                                if len(personagem.pokemons) > 1:
    #########################Personagem com 2 Pokimons###############################################################################
                                                    print('Escolha um de seus Pokimons:')
                                                    count = 0
                                                    for v in personagem.pokemons:
                                                        count += 1
                                                        print(f'POKIMON: {count} - {v.get_nome()} HP:{v.get_hp()} Ataque:{v.get_ataque()} Defesa:{v.get_defesa()}')
                                                    pokimon_escolhido = int(input('Resposta: '))
                                                    if pokimon_escolhido == 1:
    #########################Condição de Pokimon na posição 0 ###############################################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            0]
                                                        utils.clear_screen()
                                                        print(
                                                            f'Status do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'O Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    'O que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
                                                                ))
                                                            if escolha_personagem == 1:
    #########################Escolha do personagem Atacar##############################################################
                                                                utils.clear_screen()
                                                                defesaTotalEncontrado = pokimon_encontrado.get_defesa(
                                                                )
                                                                danoPokimonEscolhio = pokimon_para_batalha.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEncontrado
                                                                )
                                                                inserindoDano = pokimon_encontrado.get_hp(
                                                                ) - danoPokimonEscolhio
                                                                pokimon_encontrado.set_hp(
                                                                    -inserindoDano)
                                                                defesaTotalEscolhido = pokimon_para_batalha.get_defesa(
                                                                )
                                                                danoPokimonEncontrado = pokimon_encontrado.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEscolhido
                                                                )
                                                                inserindoDano = pokimon_para_batalha.get_hp(
                                                                ) - danoPokimonEncontrado
                                                                pokimon_para_batalha.set_hp(
                                                                    -inserindoDano)
                                                                print(
                                                                    f'Seu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'O pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonTreinado
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'O pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(4)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                                    qtdBatalha2 = 0
                                                                if pokimon_para_batalha.get_hp(
                                                                ) > 1:
                                                                    print(
                                                                        f'O seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'O pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu 1 vida!'
                                                                    )
                                                                    personagem.remover_pokemon(
                                                                        pokimon_para_batalha
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(3)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                            elif escolha_personagem == 2:
                                                                print(
                                                                    'Você correu da batalha!'
                                                                )
                                                                lutando = 1
                                                    elif pokimon_escolhido == 2:
    ##############################Escolha do personagem segundo pokimon POKIMON LISTA COM 2########################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            1]
                                                        utils.clear_screen()
                                                        print(
                                                            f'Status do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'O Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    'O que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
                                                                ))
                                                            if escolha_personagem == 1:
    #########################Escolha do personagem Atacar##############################################################
                                                                utils.clear_screen()
                                                                defesaTotalEncontrado = pokimon_encontrado.get_defesa(
                                                                )
                                                                danoPokimonEscolhio = pokimon_para_batalha.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEncontrado
                                                                )
                                                                inserindoDano = pokimon_encontrado.get_hp(
                                                                ) - danoPokimonEscolhio
                                                                pokimon_encontrado.set_hp(
                                                                    inserindoDano)
                                                                defesaTotalEscolhido = pokimon_para_batalha.get_defesa(
                                                                )
                                                                danoPokimonEncontrado = pokimon_encontrado.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEscolhido
                                                                )
                                                                inserindoDano = pokimon_para_batalha.get_hp(
                                                                ) - danoPokimonEncontrado
                                                                pokimon_para_batalha.set_hp(
                                                                    inserindoDano)
                                                                print(
                                                                    f'Seu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'O pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonTreinado
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'O pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
                                                                    )
    ####################################RESLTADO DE BATALHA COM O SEGUNDO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(4)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                                    qtdBatalha2 = 0
                                                                if pokimon_para_batalha.get_hp(
                                                                ) > 1:
                                                                    print(
                                                                        f'O seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'O pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu 1 vida!'
                                                                    )
                                                                    personagem.remover_pokemon(
                                                                        pokimon_para_batalha
                                                                    )
    ####################################RESLTADO DE BATALHA COM O SEGUNDO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(3)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                            elif escolha_personagem == 2:
                                                                print(
                                                                    'Você correu da batalha!'
                                                                )
                                                                time.sleep(2)
                                                                lutando = 10
                                                                telaDeBatalha = 10
                                                                inicioGame = 1
    ####################################Ataque com 1 pokimom#####################################################################################################################################################################################################
                                                else:
                                                    lutando = 0
                                                    while lutando == 0:
    #########################Condição de Pokimon na posição 0 ###############################################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            0]
                                                        utils.clear_screen()
                                                        print(
                                                            f'Status do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'O Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    'O que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
                                                                ))
                                                            if escolha_personagem == 1:
    #########################Escolha do personagem Atacar##############################################################
                                                                utils.clear_screen()
                                                                defesaTotalEncontrado = pokimon_encontrado.get_defesa(
                                                                )
                                                                danoPokimonEscolhio = pokimon_para_batalha.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEncontrado
                                                                )
                                                                inserindoDano = pokimon_encontrado.get_hp(
                                                                ) - danoPokimonEscolhio
                                                                pokimon_encontrado.set_hp(
                                                                    inserindoDano)
                                                                defesaTotalEscolhido = pokimon_para_batalha.get_defesa(
                                                                )
                                                                danoPokimonEncontrado = pokimon_encontrado.get_ataque(
                                                                ) - random.randint(
                                                                    1,
                                                                    defesaTotalEscolhido
                                                                )
                                                                inserindoDano = pokimon_para_batalha.get_hp(
                                                                ) - danoPokimonEncontrado
                                                                pokimon_para_batalha.set_hp(
                                                                    inserindoDano)
                                                                print(
                                                                    f'Seu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'O HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'O HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'O pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonTreinado
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'O pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(4)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                                if pokimon_para_batalha.get_hp(
                                                                ) > 1:
                                                                    print(
                                                                        f'O seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'O pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'O personagem {personagem.getNome()} perdeu 1 vida!'
                                                                    )
                                                                    personagem.remover_pokemon(
                                                                        pokimon_para_batalha
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(3)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                            elif escolha_personagem == 2:
                                                                print(
                                                                    'Você correu da batalha!'
                                                                )
                                                                lutando = 1
                                            else:
                                                print('Você correu da batalha!')
                                                time.sleep(2)
                                                lutando = 10
                                                telaDeBatalha = 10
                                                inicioGame = 1
                                        else:
                                            print('Você correu da batalha!')
                                            time.sleep(2)
                                            lutando = 10
                                            telaDeBatalha = 10
                                            inicioGame = 1
###########################POKEMONS TREINADOS Segunda batalha###############################################
            
            elif x == 2:
                ###########################TREINAMENTO#######################################################
                inicioGame = 3
                while inicioGame == 3:
                    if personagem.getDinheiro() < 50:
                        print(
                            f'Você não possui dinheiro suficiente: {personagem.getDinheiro()} '
                        )
                        time.sleep(2)
                        inicioGame = 1
                    else:
                        #tela de treinamento
                        if len(personagem.pokemons) > 1:
                            #personagem com 2 pokimons
                            print('Bem vindo ao Treinamento')
                            print('Selecione um pokimom para ser treinado')
                            selecaoPokimon = int(
                                input(
                                    f'1 - {personagem.pokemons[0].get_nome()}\n2 - {personagem.pokemons[1].get_nome()}\nResposta: '
                                ))
                            utils.clear_screen()
                            if selecaoPokimon == 1:
                                pokimonSelecionado = personagem.pokemons[0]
                                print(
                                    f'Você selecionu o pokimon {pokimonSelecionado.get_nome()}: '
                                )
                                print(
                                    f'Status do pokimom:\nNome: {pokimonSelecionado.get_nome()} HP: {pokimonSelecionado.get_hp()} Ataque: {pokimonSelecionado.get_ataque()} Defesa: {pokimonSelecionado.get_defesa()}'
                                )
                                confirmar = int(
                                    input(
                                        'Você deseja confirmar o treinamento?\n1 - Sim\n2 - Não\nResposta: '
                                    ))
                                utils.clear_screen()
                                if confirmar == 1:
                                    pokimonSelecionadoTreinado = PokimonTreinado(
                                        pokimonSelecionado.get_nome(),
                                        pokimonSelecionado.get_hp(),
                                        pokimonSelecionado.get_ataque(),
                                        pokimonSelecionado.get_defesa(), 10)
                                    pokimonSelecionadoTreinado.set_hp(70)    
                                    personagem.remover_pokemon(pokimonSelecionado)
                                    personagem.adicionar_pokemon(
                                        pokimonSelecionadoTreinado)
                                    print(
                                        f'O status do seu pokimon agora é:\nNome: {pokimonSelecionadoTreinado.get_nome()}\nHP: {pokimonSelecionadoTreinado.get_hp()}\nAtaque: {pokimonSelecionadoTreinado.get_ataque()}\nDefesa: {pokimonSelecionadoTreinado.get_defesa()}'
                                    )
                                    x = personagem.getDinheiro() - 50
                                    personagem.setDinheiro(x)
                                    inicioGame = 1
                                elif confirmar == 2:
                                    inicioGame = 1
                                elif personagem.getDinheiro < 50:
                                    print(
                                        f'Seu personagem não possui dinheiro suficiente: {personagem.getDinheiro()}'
                                    )
                                    inicioGame = 1
                            elif selecaoPokimon == 2:
                                pokimonSelecionado = personagem.pokemons[1]
                                print(
                                    f'Você selecionu o pokimon {pokimonSelecionado.get_nome()}: '
                                )
                                print(
                                    f'Status do pokimom:\nNome: {pokimonSelecionado.get_nome()} HP: {pokimonSelecionado.get_hp()} Ataque: {pokimonSelecionado.get_ataque()} Defesa: {pokimonSelecionado.get_defesa()}'
                                )
                                confirmar = int(
                                    input(
                                        'Você deseja confirmar o treinamento?\n1 - Sim\n2 - Não\nResposta: '
                                    ))
                                utils.clear_screen()
                                if confirmar == 1:
                                    pokimonSelecionadoTreinado = PokimonTreinado(
                                        pokimonSelecionado.get_nome(),
                                        pokimonSelecionado.get_hp(),
                                        pokimonSelecionado.get_ataque(),
                                        pokimonSelecionado.get_defesa(), 10)
                                    personagem.remover_pokemon(pokimonSelecionado)
                                    pokimonSelecionado.set_hp(70)    
                                    personagem.adicionar_pokemon(
                                        pokimonSelecionadoTreinado)
                                    print(
                                        f'O status do seu pokimon agora é:\nNome: {pokimonSelecionadoTreinado.get_nome()}\nHP: {pokimonSelecionadoTreinado.get_hp()}\nAtaque: {pokimonSelecionadoTreinado.get_ataque()}\nDefesa: {pokimonSelecionadoTreinado.get_defesa()}'
                                    )
                                    x = personagem.getDinheiro() - 50
                                    personagem.setDinheiro(x)
                                    inicioGame = 1
                                elif confirmar == 2:
                                    inicioGame = 1
                                elif personagem.getDinheiro() < 50:
                                    print(
                                        f'Seu personagem não possui dinheiro suficiente: {personagem.getDinheiro()}'
                                    )
                                    inicioGame = 1
                        elif len(personagem.pokemons) == 1:
                            #personagem com 1 pokimons
                            print('Bem vindo ao Treinamento')
                            print('Selecione um pokimom para ser treinado')
                            selecaoPokimon = int(
                                input(
                                    f'1 - {personagem.pokemons[0].get_nome()}\nResposta: '
                                ))
                            utils.clear_screen()
                            if selecaoPokimon == 1:
                                pokimonSelecionado = personagem.pokemons[0]
                                print(
                                    f'Você selecionu o pokimon {pokimonSelecionado.get_nome()}: '
                                )
                                print(
                                    f'Status do pokimom:\nNome: {pokimonSelecionado.get_nome()} HP: {pokimonSelecionado.get_hp()} Ataque: {pokimonSelecionado.get_ataque()} Defesa: {pokimonSelecionado.get_defesa()}'
                                )
                                confirmar = int(
                                    input(
                                        'Você deseja confirmar o treinamento?\n1 - Sim\n2 - Não\nResposta: '
                                    ))
                                utils.clear_screen()
                                if confirmar == 1:
                                    pokimonSelecionadoTreinado = PokimonTreinado(
                                        pokimonSelecionado.get_nome(),
                                        pokimonSelecionado.get_hp(),
                                        pokimonSelecionado.get_ataque(),
                                        pokimonSelecionado.get_defesa(), 10)
                                    personagem.remover_pokemon(pokimonSelecionado)
                                    pokimonSelecionadoTreinado.set_hp(70)
                                    personagem.adicionar_pokemon(
                                        pokimonSelecionadoTreinado)
                                    print(
                                        f'O status do seu pokimon agora é:\nNome: {pokimonSelecionadoTreinado.get_nome()}\nHP: {pokimonSelecionadoTreinado.get_hp()}\nAtaque: {pokimonSelecionadoTreinado.get_ataque()}\nDefesa: {pokimonSelecionadoTreinado.get_defesa()}'
                                    )
                                    x = personagem.getDinheiro() - 50
                                    personagem.setDinheiro(x)
                                    inicioGame = 1
                                elif confirmar == 2:
                                    inicioGame = 1
                                elif personagem.getDinheiro() < 50:
                                    print(
                                        f'Seu personagem não possui dinheiro suficiente: {personagem.getDinheiro()}'
                                    )
                                    inicioGame = 1
                        else:
                            print('Você não possui pokimons para ser treinados')
                            inicioGame = 1
            elif x == 3:
                ###########################DESCANSAR#######################################################
                inicioGame = 4
                while inicioGame == 4:
                    if personagem.getDinheiro() < 50:
                        print(
                            f'Você não possui dinheiro suficiente: {personagem.getDinheiro()} '
                        )
                        time.sleep(2)
                        inicioGame = 1
                    elif len(personagem.pokemons) == 0:
                        print(f'Você não possui pokimons!')
                        time.sleep(2)
                        inicioGame = 1
                    else:
                        if len(personagem.pokemons) > 1:
                            pokimon_escolhido = int(
                                input(
                                    f'Escolha um de seus pokimons\nPokimon 1 - {personagem.pokemons[0].get_nome()} HP:{personagem.pokemons[0].get_hp()} Ataque:{personagem.pokemons[0].get_ataque()} Defesa:{personagem.pokemons[0].get_defesa()}\nPokimon 2 - {personagem.pokemons[1].get_nome()} HP:{personagem.pokemons[1].get_hp()} Ataque:{personagem.pokemons[1].get_ataque()} Defesa:{personagem.pokemons[1].get_defesa()}\n'
                                ))
                            if pokimon_escolhido == 1:
                                x = personagem.getDinheiro() - 50
                                personagem.setDinheiro(x)
                                personagem.pokemons[0].set_hp(70)
                                print('Seu pokimon agora possui 70 de hp')
                                time.sleep(2)
                                inicioGame = 1
                            elif pokimon_escolhido == 2:
                                x = personagem.getDinheiro() - 50
                                personagem.setDinheiro(x)
                                personagem.pokemons[1].set_hp(70)
                                print('Seu pokimon agora possui 70 de hp')
                                time.sleep(2)
                                inicioGame = 1
                            else:
                                print('Opção invalida')
                                time.sleep(2)
                                inicioGame = 1
                        elif len(personagem.pokemons) == 1:
                            x = personagem.getDinheiro() - 50
                            personagem.setDinheiro(x)
                            personagem.pokemons[0].set_hp(70)
                            print('Seu pokimon agora possui 70 de hp')
                            time.sleep(2)
                            inicioGame = 1
                        else:
                            print('Opção invalida')
                            time.sleep(2)
                            inicioGame = 1
            elif x == 4:
                ###########################COMPRAR POKIMONS#######################################################
                inicioGame = 5
                pokimon_aleatorio = [charmander, bulbasaur, gyarados, lapras]
                for v in pokimon_aleatorio:
                    v.set_hp(50)
                while inicioGame == 5:
                    if personagem.getDinheiro() < 100 and len(
                            personagem.pokemons) > 1:
                        print(
                            'Não é possivel adquirir mais pokimons! Dinheiro Insuficiente ou você já possui 2 pokinons.'
                        )
                        time.sleep(4)
                        inicioGame = 1
                    else:
                        telaDeCompra = 0
                        while telaDeCompra == 0:
                            utils.clear_screen()
                            print('Bem vindo a loja de Pokimons.')
                            print(
                                'Por favor selecione o pokimon que deseja comprar')
                            pokimon_aleatorio = [
                                charmander, bulbasaur, gyarados, lapras
                            ]
                            cont = 0
                            for v in pokimon_aleatorio:
                                cont += 1
                                print(
                                    f'{cont} - Nome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                                )
                            x = int(input('Resposta: '))
                            if x == 1:
                                telaDeCompra = 1
                                while telaDeCompra == 1:
                                    print(
                                        f'Deseja realmente comprar o pokimon {pokimon_aleatorio[0].get_nome()}'
                                    )
                                    print('1 - Sim / 2 - Não')
                                    y = int(input('Resposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[0])
                                        print(
                                            f'Você adquiriu o pokimon {pokimon_aleatorio[0].get_nome()}'
                                        )
                                        time.sleep(2)
                                        telaDeCompra = 10
                                        inicioGame = 1
                                    else:
                                        telaDeCompra = 0
                            elif x == 2:
                                telaDeCompra = 2
                                while telaDeCompra == 2:
                                    print(
                                        f'Deseja realmente comprar o pokimon {pokimon_aleatorio[1].get_nome()}'
                                    )
                                    print('1 - Sim / 2 - Não')
                                    y = int(input('Resposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[1])
                                        print(
                                            f'Você adquiriu o pokimon {pokimon_aleatorio[1].get_nome()}'
                                        )
                                        time.sleep(2)
                                        telaDeCompra = 10
                                        inicioGame = 1
                                    else:
                                        telaDeCompra = 0
                            elif x == 3:
                                telaDeCompra = 3
                                while telaDeCompra == 3:
                                    print(
                                        f'Deseja realmente comprar o pokimon {pokimon_aleatorio[2].get_nome()}'
                                    )
                                    print('1 - Sim / 2 - Não')
                                    y = int(input('Resposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[2])
                                        print(
                                            f'Você adquiriu o pokimon {pokimon_aleatorio[2].get_nome()}'
                                        )
                                        time.sleep(2)
                                        telaDeCompra = 10
                                        inicioGame = 1
                                    else:
                                        telaDeCompra = 0
                            elif x == 4:
                                telaDeCompra = 4
                                while telaDeCompra == 4:
                                    print(
                                        f'Deseja realmente comprar o pokimon {pokimon_aleatorio[3].get_nome()}'
                                    )
                                    print('1 - Sim / 2 - Não')
                                    y = int(input('Resposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[3])
                                        print(
                                            f'Você adquiriu o pokimon {pokimon_aleatorio[3].get_nome()}'
                                        )
                                        time.sleep(2)
                                        telaDeCompra = 10
                                        inicioGame = 1
                                    else:
                                        telaDeCompra = 0
                            else:
                                print('Opção Inválida')
                                time.sleep(2)
                                telaDeCompra = 10
                                inicioGame = 1
            elif x == 5:
                ###########################VER POKIMONS#######################################################
                for v in personagem.pokemons:
                    print(
                        f'Nome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                    )
                time.sleep(2)
                inicioGame = 1
            elif x == 6:
                print(output5)
                time.sleep(6)
                inicioGame = 1
            elif x == 7:
                print(output7)
                print('Agradecimento especial a nossa querida professora DUDA.')
                print('Foi breve mas especial.')
                time.sleep(6)

            else:
                print('Opção Invalida')