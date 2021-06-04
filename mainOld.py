import random
from personagem import Personagem
from pokimon import Pokimon
from treinamento import PokimonTreinado
import utils
import time
import pygame
import ascii



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

#Agradecimento especial
url7 = 'https://media-exp1.licdn.com/dms/image/C5603AQHCwoSDIiHTvg/profile-displayphoto-shrink_800_800/0/1618974047796?e=1628121600&v=beta&t=3a-Iu0M4bliPUwRMKWL62FQ84ZWlRtHe0sDnbgWc45E'

output7 = ascii.loadFromUrl(url7)

#coraçãolaura
urlcore = 'https://i.pinimg.com/736x/d6/5a/b7/d65ab76968d74ccad914d5f8df56a5e0.jpg'
output8 = ascii.loadFromUrl(urlcore)




pygame.init()
pygame.mixer.music.load('inicio.ogg')
pygame.mixer.music.play(-1)
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
    print('	\033[1;36m Carregando jogo...')
    time.sleep(6)
    utils.clear_screen()
    print(  output1  )
    print('\033[1;33m Bem - vindo a Batalha Pokimon')
    personagem = int(
        input(
            '\033[1;35mPor favor selecione seu personagem:\n1 - ASH \n2 - MISTY\nResposta: '
        ))
    if personagem == 1:
        utils.clear_screen()
        personagem = ash
        print(output2)
        print(f'\033[1;34m Você escolheu o {personagem.getNome()}')
        #print('Localizando pokimons...')
        time.sleep(5)
        inicioGame = 1
    elif personagem == 2:
        utils.clear_screen()
        print(output3)
        personagem = misty
        #print('Localizando pokimons...')
        print(f'\033[1;35m Você escolheu a {personagem.getNome()}')
        time.sleep(5)
        inicioGame = 1
    else:
        utils.clear_screen()
        print('\033[1;31m Opção Invalida.')
    while inicioGame == 1:
        ###########################STATUS INICIAL#######################################################
        if len(personagem.pokemons) >= 3:
            print('	\033[1;33m=================PARABÉNS!=================')
            print('	\033[1;33mVocê conseguiu capturar 3 pokimons e com isto é o grande vencedor da Batalha Pokimon!')
            print(output4)
            time.sleep(6)
            break
        elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(personagem.pokemons) < 1 and personagem.getEstamina() <= 0 or personagem.getVida() <= 0 or personagem.getDinheiro() <= 0 and len(personagem.pokemons) <= 0:
            print('\033[1;31mVocê perdeu e não é possivel continuar o jogo!')
            print('\033[1;31mReiniciando...')
            print(url6)
            time.sleep(3)
            utils.clear_screen()
            inicioGame = 0
        else:
            utils.clear_screen()
            print('\033[1;31m Instruções de jogo: \n')
            print('\033[1;31mDurante o jogo você terá 3 vidas e para vencer deve conseguir 3 Pokimons. \n')
            print('\033[1;31mVocê perde o jogo ao perder suas vidas ou se sua stamina chegar a 0.\n')
            print('\033[1;34m=================ATRIBUTOS DO PERSONAGEM=================')
            print(
                f'	\033[1;37mNome: {personagem.getNome()} Vida: {personagem.getVida()} Estamina: {personagem.getEstamina()} Dinheiro: {personagem.getDinheiro()}'
            )
            print()
            print('\033[1;34m=================ATRIBUTOS DO POKIMON=================\n')
    
            for v in personagem.pokemons:
                print(
                    f'	\033[1;37mNome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                )
            print()
            print('\033[1;32mEscolha uma opção: \n')
            print('\033[1;32m1 - Procurar pokimon (Gasta 25 de Estamina)')
            print('\033[1;32m2 - Treinar pokimon (Gasta 50 de Dinheiro)')
            print(
                '\033[1;32m3 - Descansar (Gasta 50 de Dinheiro e recupera 70 de HP para 1 Pokimon)'
            )
            print('\033[1;32m4 - Comprar Pokimom (Gasta 100 de Dinheiro)')
            print('\033[1;32m5 - Ver seus Pokimons')
            print('\033[1;32m6 - Ver participação especial!')
            print('\033[1;32m7 - Ver agradecimento especial!')
            x = int(input('\033[1;32mResposta: '))
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
                                '\033[1;31mSeu personagem não possui pokemons, vidas ou stamina suficientes'
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
                                print('\033[1;34m=================ATRIBUTOS DO PERSONAGEM=================')
                                print(
                                    f'	\033[1;37mNome: \033[1;37m{personagem.getNome()} \033[1;37mVida: \033[1;37m{personagem.getVida()} \033[1;37mEstamina: \033[1;37m{personagem.getEstamina()} \033[1;37mDinheiro: \033[1;37m{personagem.getDinheiro()}'
                                )
                                print()
                                print('\033[1;34m=================POKIMONS=================')
                                for v in personagem.pokemons:
                                    print(
                                        f'\033[1;37mNome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                                    )
                                print()
                                print('\033[1;32m=================BEM VINDO AO MENU DE BATALHA=================\n')
                                print('\033[1;33mVocê deseja procurar Pokimons?')
                                print('\033[1;33m1 - Sim / 2 - Não')
                                y = int(input('\033[1;33mResposta: '))
                                utils.clear_screen()
                                if y != 1:
                                    lutando = 10
                                    telaDeBatalha = 10
                                    inicioGame = 1
                                    qtdBatalha2 = 0
                                elif len(personagem.pokemons) >= 3:
                                    print('\033[1;33m=================PARABÉNS=================')
                                    print('\033[1;33mVocê conseguiu capturar 3 pokimons e com isto é o grande vencedor da Batalha Pokimon!')
                                    time.sleep(5)
                                    print(output4)
                                    break
                                elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(personagem.pokemons) < 1 and personagem.getEstamina() <= 0 or personagem.getVida() <= 0:
                                    print('\033[1;31mVocê perdeu e não é possivel continuar o jogo!')
                                    print('\033[1;31mReiniciando...')
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
                                                f'\033[1;34mVocê encontrou o pokimon {pokimon_encontrado.get_nome()}'
                                            )
                                            print('\033[1;34mDeseja atacar?\n1 - sim\n2 - não\n')
                                            atacar = int(input('\033[1;34mResposta: \n'))
                                            if atacar == 1:
                                                utils.clear_screen()
                                                if len(personagem.pokemons) > 1:
    #########################Personagem com 2 Pokimons###############################################################################
                                                    print('\033[1;33mEscolha um de seus Pokimons:')
                                                    count = 0
                                                    for v in personagem.pokemons:
                                                        count += 1
                                                        print(f'\033[1;37mPOKIMON: {count} - {v.get_nome()} HP:{v.get_hp()} Ataque:{v.get_ataque()} Defesa:{v.get_defesa()}')
                                                    pokimon_escolhido = int(input('\033[1;33mResposta: '))
                                                    if pokimon_escolhido == 1:
    #########################Condição de Pokimon na posição 0 ###############################################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            0]
                                                        utils.clear_screen()
                                                        print(
                                                            f'\033[1;37mStatus do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'\033[1;34mO Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    '\033[1;33mO que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: \n'
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
                                                                    f'\033[1;34mSeu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;34mO pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'\033[1;35mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'\033[1;34mO pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonSemTreinamento
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'\033[1;34mO pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;33mO personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
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
                                                                        f'\033[1;33mO seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'\033[1;31mO pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu 1 vida!'
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
                                                                    '\033[1;31mVocê correu da batalha!'
                                                                )
                                                                lutando = 1
                                                    elif pokimon_escolhido == 2:
    ##############################Escolha do personagem segundo pokimon POKIMON LISTA COM 2########################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            1]
                                                        utils.clear_screen()
                                                        print(
                                                            f'\033[1;34mStatus do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'\033[1;34mO Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    '\033[1;33mO que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: \n'
                                                                ))
                                                            if escolha_personagem == 1:
    #########################Escolha do personagem Atacar##############################################################
                                                                utils.clear_screen()                             
                                                                lutando = 10
                                                                telaDeBatalha = 10
                                                                inicioGame = 1
                                                                qtdBatalha2 = 0
                                                            elif len(personagem.pokemons) >= 3:
                                                                print('\033[1;33m=================PARABÉNS=================')
                                                                print('\033[1;33mVocê conseguiu 3 pokimons e venceu a Batalha Pokimon!')
                                                                time.sleep(5)
                                                                print(output4)
                                                                break
                                                            elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(personagem.pokemons) < 1 and personagem.getEstamina() <= 0 or personagem.getVida() <= 0:
                                                                print('\033[1;31mVocê perdeu e não é possivel continuar o jogo!')
                                                                print('\033[1;31mReiniciando...')
                                                                print(output6)
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                inicioGame = 0
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
                                                                    f'\033[1;34mSeu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;34mO pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'\033[1;34mO pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonSemTreinamento
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'\033[1;34mO pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;33mO personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
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
                                                                        f'\033[1;34mO seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'\033[1;31mO pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu 1 vida!'
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
                                                                    '\033[1;31mVocê correu da batalha!'
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
                                                            f'\033[1;37mStatus do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'\033[1;34mO Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    '\033[1;32mO que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: \n'
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
                                                                    f'\033[1;34mSeu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;34mO pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'\033[1;34mO pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonSemTreinamento
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;33mO personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
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
                                                                        f'\033[1;34mO seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'\033[1;31mO pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu 1 vida!'
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
                                                                    '\033[1;31mVocê correu da batalha!'
                                                                )
                                                                lutando = 1
                                            else:
                                                print('\033[1;31mVocê correu da batalha!')
                                                time.sleep(2)
                                                lutando = 10
                                                telaDeBatalha = 10
                                                inicioGame = 1
                                        else:
                                            print('\033[1;31mVocê correu da batalha!')
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
                                '\033[1;31mSeu personagem não possui pokemons, vidas ou stamina suficientes'
                            )
                            time.sleep(2)
                            inicioGame = 1
                        else:
                            telaDeBatalha = 0
                            while telaDeBatalha == 0:
                                utils.clear_screen()
                                print('\033[1;34m\033[1;31m==================ATRIBUTOS DO PERSONAGEM=================')
                                print(
                                    f'\033[1;37mNome: {personagem.getNome()} Vida: {personagem.getVida()} Estamina: {personagem.getEstamina()} Dinheiro: {personagem.getDinheiro()}'
                                )
                                print()
                                print('\033[1;34m=================POKIMONS=================')
                                for v in personagem.pokemons:
                                    print(
                                        f'\033[1;37mNome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                                    )
                                print('\033[1;34m=================POKIMONS=================')
                                print()
                                print('\033[1;33m=================BEM VINDO AO MENU DE BATALHA=================\n')
                                print('\033[1;34mVocê deseja procurar pokimons?')
                                print('\033[1;34m1 - Sim / 2 - Não')
                                y = int(input('\033[1;34mResposta: '))
                                utils.clear_screen()
                                if y != 1:
                                    lutando = 10
                                    telaDeBatalha = 10
                                    inicioGame = 1
                                    qtdBatalha2 = 0
                                elif len(personagem.pokemons) >= 3:
                                    print('\033[1;33m=================PARABÉNS=================')
                                    print('\033[1;33mVocê conseguiu 3 Pokimons e venceu a Batalha Pokimon')
                                    time.sleep(5)
                                    print(output4)
                                    break
                                elif len(personagem.pokemons) < 1 and personagem.getVida() <= 0 or len(personagem.pokemons) < 1 and personagem.getEstamina() <= 0 or personagem.getVida() <= 0:
                                    print('\033[1;31mNao é possivel continuar o jogo!')
                                    print('\033[1;31mReiniciando...')
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
                                                f'\033[1;34mVocê encontrou o pokimon {pokimon_encontrado.get_nome()}'
                                            )
                                            print('\033[1;34mDeseja atacar?\n1 - sim\n2 - não')
                                            atacar = int(input('\033[1;34mResposta: '))
                                            if atacar == 1:
                                                utils.clear_screen()
                                                if len(personagem.pokemons) > 1:
    #########################Personagem com 2 Pokimons###############################################################################
                                                    print('\033[1;33mEscolha um de seus Pokimons:')
                                                    count = 0
                                                    for v in personagem.pokemons:
                                                        count += 1
                                                        print(f'\033[1;37mPOKIMON: {count} - {v.get_nome()} HP:{v.get_hp()} Ataque:{v.get_ataque()} Defesa:{v.get_defesa()}')
                                                    pokimon_escolhido = int(input('\033[1;34mResposta: '))
                                                    if pokimon_escolhido == 1:
    #########################Condição de Pokimon na posição 0 ###############################################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            0]
                                                        utils.clear_screen()
                                                        print(
                                                            f'\033[1;37mStatus do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'\033[1;34mO Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    '\033[1;34mO que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
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
                                                                    f'\033[1;34mSeu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;34mO pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'\033[1;34mO pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonTreinado
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
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
                                                                        f'\033[1;33mO seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'\033[1;31mO pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu 1 vida!'
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
                                                                    '\033[1;31mVocê correu da batalha!'
                                                                )
                                                                lutando = 1
                                                    elif pokimon_escolhido == 2:
    ##############################Escolha do personagem segundo pokimon POKIMON LISTA COM 2########################################################
                                                        pokimon_para_batalha = personagem.pokemons[
                                                            1]
                                                        utils.clear_screen()
                                                        print(
                                                            f'\033[1;37mStatus do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'\033[1;34mO Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    '\033[1;34mO que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: '
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
                                                                    f'\033[1;34mSeu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;34mO pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'\033[1;34mO pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonTreinado
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;33mO personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
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
                                                                        f'\033[1;33mO seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'\033[1;31mO pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu 1 vida!'
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
                                                                    '\033[1;31mVocê correu da batalha!'
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
                                                            f'\033[1;37mStatus do Pokimon escolhido: {pokimon_para_batalha.get_nome()} HP:{pokimon_para_batalha.get_hp()} Ataque:{pokimon_para_batalha.get_ataque()} Defesa:{pokimon_para_batalha.get_defesa()}'
                                                        )
                                                        lutando = 0
                                                        while lutando == 0:
    #########################Entrando na luta laço while lutando = 0 #############################################################################################
                                                            print(
                                                                f'\033[1;34mO Pokimom encontrado {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[0]} para você'
                                                            )
                                                            escolha_personagem = int(
                                                                input(
                                                                    '\033[1;34mO que você deseja fazer?\n1 - Atacar\n2 - Correr\nReação: \n'
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
                                                                    f'\033[1;34mSeu pokimom {pokimon_para_batalha.get_nome()} atacou e causou {danoPokimonEscolhio} de dano no pokimom {pokimon_encontrado.get_nome()}'
                                                                )
                                                                time.sleep(1)
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;34mO pokimon encontrado {pokimon_encontrado.get_nome()} contra-atacou e causou {danoPokimonEncontrado} de dano no pokimom {pokimon_para_batalha.get_nome()}'
                                                                )
                                                                time.sleep(3)
                                                                utils.clear_screen()
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom escolhido {pokimon_para_batalha.get_nome()} é de {pokimon_para_batalha.get_hp()}'
                                                                )
                                                                print(
                                                                    f'\033[1;37mO HP atual do pokimom encontrado {pokimon_encontrado.get_nome()} é de {pokimon_encontrado.get_hp()}'
                                                                )
                                                                if pokimon_encontrado.get_hp(
                                                                ) >= 1:
                                                                    print(
                                                                        f'\033[1;34mO pokimon {pokimon_encontrado.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    pokimon_encontrado.set_hp(
                                                                        hpPokimonTreinado
                                                                    )
                                                                    personagem.adicionar_pokemon(
                                                                        pokimon_encontrado
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO pokemon encontrado {pokimon_encontrado.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;33mO personagem {personagem.getNome()} ganhou o pokimom {pokimon_encontrado.get_nome()}'
                                                                    )
    ####################################RESLTADO DE BATALHA COM O PRIMEIRO POKIMON LISTA COM 2########################################################
                                                                    time.sleep(4)
                                                                    lutando = 10
                                                                    telaDeBatalha = 10
                                                                    inicioGame = 1
                                                                if pokimon_para_batalha.get_hp(
                                                                ) > 1:
                                                                    print(
                                                                        f'\033[1;34mO seu pokimon {pokimon_para_batalha.get_nome()} {reacao_aleatoria_pokimon[random.randint(0 , 3)]} e continua vivo!\n'
                                                                    )
                                                                else:
                                                                    print(
                                                                        f'\033[1;31mO pokemon {pokimon_para_batalha.get_nome()} morreu!'
                                                                    )
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu o pokimom {pokimon_para_batalha.get_nome()}'
                                                                    )
                                                                    vidaPers = personagem.getVida(
                                                                    ) - 1
                                                                    personagem.setVida(
                                                                        vidaPers)
                                                                    print(
                                                                        f'\033[1;31mO personagem {personagem.getNome()} perdeu 1 vida!'
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
                                                                    '\033[1;31mVocê correu da batalha!'
                                                                )
                                                                lutando = 1
                                            else:
                                                print('\033[1;31mVocê correu da batalha!')
                                                time.sleep(2)
                                                lutando = 10
                                                telaDeBatalha = 10
                                                inicioGame = 1
                                        else:
                                            print('\033[1;31mVocê correu da batalha!')
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
                            f'\033[1;31mVocê não possui dinheiro suficiente: {personagem.getDinheiro()} '
                        )
                        time.sleep(2)
                        inicioGame = 1
                    else:
                        #tela de treinamento
                        if len(personagem.pokemons) > 1:
                            #personagem com 2 pokimons
                            print('\033[1;33mBem vindo ao Treinamento!\n')
                            print('\033[1;34mSelecione um pokimom para ser treinado: \n')
                            selecaoPokimon = int(
                                input(
                                    f'\033[1;34m1 - {personagem.pokemons[0].get_nome()}\n2 - {personagem.pokemons[1].get_nome()}\nResposta: '
                                ))
                            utils.clear_screen()
                            if selecaoPokimon == 1:
                                pokimonSelecionado = personagem.pokemons[0]
                                print(
                                    f'\033[1;34mVocê selecionu o pokimon {pokimonSelecionado.get_nome()}: '
                                )
                                print(
                                    f'\033[1;37mStatus do pokimom:\nNome: {pokimonSelecionado.get_nome()} HP: {pokimonSelecionado.get_hp()} Ataque: {pokimonSelecionado.get_ataque()} Defesa: {pokimonSelecionado.get_defesa()}'
                                )
                                confirmar = int(
                                    input(
                                        '\033[1;32mVocê deseja confirmar o treinamento?\n1 - Sim\n2 - Não\nResposta: '
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
                                        f'\033[1;37mO status do seu pokimon agora é:\nNome: {pokimonSelecionadoTreinado.get_nome()}\nHP: {pokimonSelecionadoTreinado.get_hp()}\nAtaque: {pokimonSelecionadoTreinado.get_ataque()}\nDefesa: {pokimonSelecionadoTreinado.get_defesa()}'
                                    )
                                    x = personagem.getDinheiro() - 50
                                    personagem.setDinheiro(x)
                                    inicioGame = 1
                                elif confirmar == 2:
                                    inicioGame = 1
                                elif personagem.getDinheiro < 50:
                                    print(
                                        f'\033[1;31mSeu personagem não possui dinheiro suficiente: {personagem.getDinheiro()}'
                                    )
                                    inicioGame = 1
                            elif selecaoPokimon == 2:
                                pokimonSelecionado = personagem.pokemons[1]
                                print(
                                    f'\033[1;34mVocê selecionou o pokimon {pokimonSelecionado.get_nome()}: '
                                )
                                print(
                                    f'\033[1;37mStatus do pokimom:\nNome: {pokimonSelecionado.get_nome()} HP: {pokimonSelecionado.get_hp()} Ataque: {pokimonSelecionado.get_ataque()} Defesa: {pokimonSelecionado.get_defesa()}'
                                )
                                confirmar = int(
                                    input(
                                        '\033[1;32mVocê deseja confirmar o treinamento?\n1 - Sim\n2 - Não\nResposta: '
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
                                        f'\033[1;37mO status do seu pokimon agora é:\nNome: {pokimonSelecionadoTreinado.get_nome()}\nHP: {pokimonSelecionadoTreinado.get_hp()}\nAtaque: {pokimonSelecionadoTreinado.get_ataque()}\nDefesa: {pokimonSelecionadoTreinado.get_defesa()}'
                                    )
                                    x = personagem.getDinheiro() - 50
                                    personagem.setDinheiro(x)
                                    inicioGame = 1
                                elif confirmar == 2:
                                    inicioGame = 1
                                elif personagem.getDinheiro() < 50:
                                    print(
                                        f'\033[1;31mSeu personagem não possui dinheiro suficiente: {personagem.getDinheiro()}'
                                    )
                                    inicioGame = 1
                        elif len(personagem.pokemons) == 1:
                            #personagem com 1 pokimons
                            print('\033[1;33mBem vindo ao Treinamento')
                            print('\033[1;34mSelecione um pokimom para ser treinado')
                            selecaoPokimon = int(
                                input(
                                    f'\033[1;34m1 - {personagem.pokemons[0].get_nome()}\nResposta: '
                                ))
                            utils.clear_screen()
                            if selecaoPokimon == 1:
                                pokimonSelecionado = personagem.pokemons[0]
                                print(
                                    f'\033[1;34mVocê selecionu o pokimon {pokimonSelecionado.get_nome()}: '
                                )
                                print(
                                    f'\033[1;37mStatus do pokimom:\nNome: {pokimonSelecionado.get_nome()} HP: {pokimonSelecionado.get_hp()} Ataque: {pokimonSelecionado.get_ataque()} Defesa: {pokimonSelecionado.get_defesa()}'
                                )
                                confirmar = int(
                                    input(
                                        '\033[1;32mVocê deseja confirmar o treinamento?\n1 - Sim\n2 - Não\nResposta: '
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
                                        f'\033[1;37mO status do seu pokimon agora é:\nNome: {pokimonSelecionadoTreinado.get_nome()}\nHP: {pokimonSelecionadoTreinado.get_hp()}\nAtaque: {pokimonSelecionadoTreinado.get_ataque()}\nDefesa: {pokimonSelecionadoTreinado.get_defesa()}'
                                    )
                                    x = personagem.getDinheiro() - 50
                                    personagem.setDinheiro(x)
                                    inicioGame = 1
                                elif confirmar == 2:
                                    inicioGame = 1
                                elif personagem.getDinheiro() < 50:
                                    print(
                                        f'\033[1;31mSeu personagem não possui dinheiro suficiente: {personagem.getDinheiro()}'
                                    )
                                    inicioGame = 1
                        else:
                            print('\033[1;31mVocê não possui pokimons para ser treinados')
                            inicioGame = 1
            elif x == 3:
                ###########################DESCANSAR#######################################################
                inicioGame = 4
                while inicioGame == 4:
                    if personagem.getDinheiro() < 50:
                        print(
                            f'\033[1;31mVocê não possui dinheiro suficiente: {personagem.getDinheiro()} '
                        )
                        time.sleep(2)
                        inicioGame = 1
                    elif len(personagem.pokemons) == 0:
                        print(f'\033[1;31mVocê não possui pokimons!')
                        time.sleep(2)
                        inicioGame = 1
                    else:
                        if len(personagem.pokemons) > 1:
                            pokimon_escolhido = int(
                                input(
                                    f'\033[1;34mEscolha um de seus pokimons\nPokimon 1 - {personagem.pokemons[0].get_nome()} HP:{personagem.pokemons[0].get_hp()} Ataque:{personagem.pokemons[0].get_ataque()} Defesa:{personagem.pokemons[0].get_defesa()}\nPokimon 2 - {personagem.pokemons[1].get_nome()} HP:{personagem.pokemons[1].get_hp()} Ataque:{personagem.pokemons[1].get_ataque()} Defesa:{personagem.pokemons[1].get_defesa()}\n'
                                ))
                            if pokimon_escolhido == 1:
                                x = personagem.getDinheiro() - 50
                                personagem.setDinheiro(x)
                                personagem.pokemons[0].set_hp(70)
                                print('\033[1;33mSeu pokimon agora possui 70 de hp')
                                time.sleep(2)
                                inicioGame = 1
                            elif pokimon_escolhido == 2:
                                x = personagem.getDinheiro() - 50
                                personagem.setDinheiro(x)
                                personagem.pokemons[1].set_hp(70)
                                print('\033[1;33mSeu pokimon agora possui 70 de hp')
                                time.sleep(2)
                                inicioGame = 1
                            else:
                                print('\033[1;31mOpção invalida')
                                time.sleep(2)
                                inicioGame = 1
                        elif len(personagem.pokemons) == 1:
                            x = personagem.getDinheiro() - 50
                            personagem.setDinheiro(x)
                            personagem.pokemons[0].set_hp(70)
                            print('\033[1;33mSeu pokimon agora possui 70 de hp')
                            time.sleep(2)
                            inicioGame = 1
                        else:
                            print('\033[1;31mOpção invalida')
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
                            '\033[1;31mNão é possivel adquirir mais pokimons! \nDinheiro Insuficiente ou você já possui 2 pokinons.'
                        )
                        time.sleep(4)
                        inicioGame = 1
                    else:
                        telaDeCompra = 0
                        while telaDeCompra == 0:
                            utils.clear_screen()
                            print('\033[1;33mBem vindo a loja de Pokimons.')
                            print(
                                '\033[1;34mPor favor selecione o pokimon que deseja comprar')
                            pokimon_aleatorio = [
                                charmander, bulbasaur, gyarados, lapras
                            ]
                            cont = 0
                            for v in pokimon_aleatorio:
                                cont += 1
                                print(
                                    f'\033[1;37m{cont} - Nome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                                )
                            x = int(input('\033[1;33mResposta: '))
                            if x == 1:
                                telaDeCompra = 1
                                while telaDeCompra == 1:
                                    print(
                                        f'\033[1;32mDeseja realmente comprar o pokimon {pokimon_aleatorio[0].get_nome()}'
                                    )
                                    print('\033[1;32m1 - Sim / 2 - Não')
                                    y = int(input('\033[1;32mResposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[0])
                                        print(
                                            f'\033[1;33mVocê adquiriu o pokimon {pokimon_aleatorio[0].get_nome()}'
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
                                        f'\033[1;32mDeseja realmente comprar o pokimon {pokimon_aleatorio[1].get_nome()}'
                                    )
                                    print('\033[1;32m1 - Sim / 2 - Não')
                                    y = int(input('\033[1;32mResposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[1])
                                        print(
                                            f'\033[1;33mVocê adquiriu o pokimon {pokimon_aleatorio[1].get_nome()}'
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
                                        f'\033[1;32mDeseja realmente comprar o pokimon {pokimon_aleatorio[2].get_nome()}'
                                    )
                                    print('\033[1;32m1 - Sim / 2 - Não')
                                    y = int(input('\033[1;32mResposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[2])
                                        print(
                                            f'\033[1;33mVocê adquiriu o pokimon {pokimon_aleatorio[2].get_nome()}'
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
                                        f'\033[1;32mDeseja realmente comprar o pokimon {pokimon_aleatorio[3].get_nome()}'
                                    )
                                    print('\033[1;32m1 - Sim / 2 - Não')
                                    y = int(input('\033[1;32mResposta: '))
                                    if y == 1:
                                        utils.clear_screen()
                                        personagem.setDinheiro(0)
                                        personagem.adicionar_pokemon(
                                            pokimon_aleatorio[3])
                                        print(
                                            f'\033[1;33mVocê adquiriu o pokimon {pokimon_aleatorio[3].get_nome()}'
                                        )
                                        time.sleep(2)
                                        telaDeCompra = 10
                                        inicioGame = 1
                                    else:
                                        telaDeCompra = 0
                            else:
                                print('\033[1;31mOpção Inválida')
                                time.sleep(2)
                                telaDeCompra = 10
                                inicioGame = 1
            elif x == 5:
                ###########################VER POKIMONS#######################################################
                for v in personagem.pokemons:
                    print(
                        f'\033[1;35mNome: {v.get_nome()} HP: {v.get_hp()} Ataque: {v.get_ataque()} Defesa: {v.get_defesa()}'
                    )
                time.sleep(2)
                inicioGame = 1
            elif x == 6:
                print(output5)
                time.sleep(6)
                inicioGame = 1
            elif x == 7:
                print(output7,output8)
                print('\033[1;35mAgradecimento especial a nossa querida professora DUDA.')
                print('\033[1;35mFoi breve mas especial.')
                time.sleep(8)
                inicioGame = 1

            else:
                print('\033[1;31mOpção Invalida')



