import random
from personagem import Personagem
from pokimon import Pokimon
from treinamento import PokimonTreinado
import utils
import time
'''import pygame'''
'''
pygame.init()
pygame.mixer.music.load('inicio.ogg')
pygame.mixer.music.play()
pygame.event.wait()0
'''


pokimonAleatorioSelvagem = utils.instanciaDePokimons()
pokimonsPersonagem = utils.instanciaDePokimons()

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
    ash.adicionar_pokemon(pokimonsPersonagem[0])
    misty.adicionar_pokemon(pokimonsPersonagem[1])
    print('Carregando jogo...')
    utils.clear_screen()
    print('Bem - vindo ao jogo de captura de pokimons')
    print('Por favor selecione seu personagem:\n1 - ASH\n2 - MISTY\n ')

    x = utils.resposta()
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
        condicaoDeVD = utils.condicaoVitoriaDerrota(personagem)
        print(condicaoDeVD)
        time.sleep(4)
        if condicaoDeVD == 2:
            print('Vitoria')
            break
        elif condicaoDeVD == 0 or condicaoDeVD == 1:
            print('Derrota')
            break
        elif condicaoDeVD == 3:
            print('Prepare-se para aventura')
            time.sleep(2)
            utils.clear_screen()    
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
            personagem.pokemons[0].getImg()
            print('Escolha uma opção:')
            print('1 - Procurar pokimon (Custo: 25 Estamina)')
            print('2 - Treinar pokimon (Custo: 50 Dinheiro)')
            print(
                f'3 - Descansar (Custo: 25 Dinheiro | Recupera o total de HP para 1 Pokimon + 25 Stamina para {personagem.getNome()})'
            )
            print('4 - Comprar Pokimom (Custo: 100 Dinheiro)')
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
                        if personagem.getEstamina() < 25:
                            print(
                                'Seu personagem não possui Stamina suficiente'
                            )
                            time.sleep(2)
                            inicioGame = 1
                        elif len(personagem.pokemons) <= 0:
                            print(
                                'Seu personagem não possui Pokimons suficiente'
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
                                        f'Nome: {v.getNome()} HP: {v.getHp()} Ataque: {v.getAtaque()} Defesa: {v.getDefesa()}'
                                    )
                                print('---POKIMONS---')
                                print()
                                print('!!!BEM VINDO AO MENU DE BATALHA!!!\n')
                                print('Você deseja procurar pokimons?')
                                print('1 - Sim\n2 - Não')
                                x = personagem.resposta()
                                if x == 1 and personagem.getEstamina() >= 1:
                                    lutando = 0
                                    stamina = personagem.getEstamina() - 25
                                    personagem.setEstamina(stamina)
                                    while lutando == 0:
                                        random.shuffle(pokimonAleatorioSelvagem)
                                        pokimon_encontrado = pokimonAleatorioSelvagem[
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
                                                    pokimonEncontrado = pokimonAleatorioSelvagem[
                                                        0]
                                                    batalha = 0
                                                    while batalha == 0:
                                                        utils.clear_screen()
                                                        resultado = utils.resultadoDeBatalha(pokimonEscolhido, pokimonEncontrado, personagem)
                                                        if resultado == 1:
                                                            lutando = 3
                                                            batalha = 3
                                                            telaDeBatalha = 5
                                                            inicioGame = 1
                                                            break
                                                        elif resultado == 2:
                                                            lutando = 3
                                                            batalha = 3
                                                            telaDeBatalha = 5
                                                            inicioGame = 1
                                                            break
                                                        elif resultado == 3:
                                                            lutando = 3
                                                            batalha = 3
                                                            telaDeBatalha = 5
                                                            inicioGame = 1
                                                            break
                                                        else:
                                                            print('Os Pokimons continuan na batalha!')    
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
                                                            #Ataque do Pokimom escolhido
                                                            utils.clear_screen()
                                                            dano = pokimonEscolhido.atacar(
                                                                pokimonEncontrado
                                                            )
                                                            recebeDano = pokimonEncontrado.receberDano(
                                                                pokimonEncontrado,
                                                                dano)
                                                            print(
                                                                f'O seu Pokimom {pokimonEscolhido.getNome()} causou {dano} de dano no Pokimon Encontrado {pokimonEncontrado.getNome()}'
                                                            )
                                                            time.sleep(2)
                                                            utils.clear_screen(
                                                            )
                                                            #Ataque do Pokimom Encontrado
                                                            utils.clear_screen(
                                                            )
                                                            dano = pokimonEncontrado.atacar(
                                                                pokimonEscolhido
                                                            )
                                                            recebeDano = pokimonEscolhido.receberDano(
                                                                pokimonEscolhido,
                                                                dano)
                                                            print(
                                                                f'O Pokimom encontrado {pokimonEncontrado.getNome()} causou {dano} de dano no seu Pokimon {pokimonEscolhido.getNome()}'
                                                            )
                                                            time.sleep(2)
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
                                elif x == 1 and personagem.getEstamina() <= 0:
                                    print('\033[0;31mSeu personagem não possui Stamina suficiente para continuar. Descanse para prosseguir.\033[m')
                                    time.sleep(2)
                                else:
                                    print('\033[0;31mOpção inválida.\033[m')
                                    time.sleep(2)
            
            elif x == 2:
                print('Treinar')
                time.sleep(2)                          
            elif x == 3:
                print('Descansar')
                time.sleep(2) 
            elif x == 4:
                print('Comprar')
                time.sleep(2) 
            elif x == 5:
                print('Ver')
                time.sleep(2) 
            elif x == 6:
                print('Participação')
                time.sleep(2) 
            elif x == 7:
                print('Agradecimentos')
                time.sleep(2) 
            else:
                print('\033[0;31mOpção inválida.\033[m')
                time.sleep(2)
