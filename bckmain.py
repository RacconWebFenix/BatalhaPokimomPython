import random
from personagem import Personagem
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
pesonagens = utils.instanciaDePersonagens()

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
    ash = pesonagens[0]
    misty = pesonagens[1]
    ash.adicionar_pokemon(pokimonsPersonagem[0])
    misty.adicionar_pokemon(pokimonsPersonagem[1])
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
        personagem.getImg()
        print('Localizando pokimons...')
        time.sleep(3)
        inicioGame = 1
    elif x == 2:
        utils.clear_screen()
        personagem = misty
        print(f'Você escolheu a {personagem.getNome()}')
        personagem.getImg()
        print('Localizando pokimons...')
        time.sleep(3)
        inicioGame = 1
    else:
        print('\033[1;91mOpção Inválida\033[m')
        time.sleep(2)
    while inicioGame == 1:
###########################STATUS INICIAL#######################################################    
        print('Instruções de jogo.')
        print('Durante a procura de pokinons')
        time.sleep(1)
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
        print('8 - Voltar para o menu de Personagens')
        print('9 - Sair do Jogo')
        x = personagem.resposta()
        if x == 1:
            if personagem.getEstamina() < 25:
                print('Seu personagem não possui Stamina suficiente')
                time.sleep(2)
                inicioGame = 1
            elif len(personagem.pokemons) <= 0:
                print('Seu personagem não possui Pokimons suficiente')
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
                            pokimon_encontrado = pokimonAleatorioSelvagem[0]
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
                                escolha_personagem = personagem.resposta()
                                if escolha_personagem == 1:
                                    utils.clear_screen()
                                    lutando = 2
                                    while lutando == 2:
                                        #testar a força para decidir qual pokemom ira ser encontrado
                                        print('Preare-se para batalha!')
                                        pokimonEscolhido = personagem.escolhaDePokimons(
                                        )
                                        pokimonEncontrado = pokimonAleatorioSelvagem[
                                            0]
                                        batalha = 0
                                        while batalha == 0:
                                            utils.clear_screen()
                                            resultado = utils.resultadoDeBatalha(
                                                pokimonEscolhido,
                                                pokimonEncontrado, personagem)
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
                                                print(
                                                    'Os Pokimons continuan na batalha!'
                                                )
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
                                            resp = personagem.resposta()
                                            if resp == 1:
                                                #Ataque do Pokimom escolhido
                                                utils.clear_screen()
                                                dano = pokimonEscolhido.atacar(
                                                    pokimonEncontrado)
                                                recebeDano = pokimonEncontrado.receberDano(
                                                    pokimonEncontrado, dano)
                                                print(
                                                    f'O seu Pokimom {pokimonEscolhido.getNome()} causou {dano} de dano no Pokimon Encontrado {pokimonEncontrado.getNome()}'
                                                )
                                                time.sleep(2)
                                                utils.clear_screen()
                                                #Ataque do Pokimom Encontrado
                                                utils.clear_screen()
                                                dano = pokimonEncontrado.atacar(
                                                    pokimonEscolhido)
                                                recebeDano = pokimonEscolhido.receberDano(
                                                    pokimonEscolhido, dano)
                                                print(
                                                    f'O Pokimom encontrado {pokimonEncontrado.getNome()} causou {dano} de dano no seu Pokimon {pokimonEscolhido.getNome()}'
                                                )
                                                time.sleep(2)
                                            elif resp == 2:
                                                utils.clear_screen()
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
                                                utils.clear_screen()
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
                                    print('\033[0;31mOpção inválida.\033[m')
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
                        print(
                            '\033[0;31mSeu personagem não possui Stamina suficiente para continuar. Descanse para prosseguir.\033[m'
                        )
                        time.sleep(2)
                    else:
                        print('\033[0;31mOpção inválida.\033[m')
                        time.sleep(2)

        elif x == 2:
            print('Treinar')
            time.sleep(2)
        elif x == 3:
            print('Descansar')
            telaDescansar = 0
            while telaDescansar == 0:
                utils.clear_screen()
                print('Ao descanar seu personagem perde 25 de dinheiro.')
                print('Um de seus Pokimons se recupera totalmente.')
                print('Desesa realmente descansar?')
                print('1 - Sim\n2 - Não')
                x = personagem.resposta()
                if x == 1:
                    novoDinheiro = personagem.getDinheiro() - 25
                    personagem.setDinheiro(novoDinheiro)
                    pokimonDescansado = 0
                    pokimonEscolhido = personagem.escolhaDePokimons()
                    for v in pokimonAleatorioSelvagem:
                        if pokimonEscolhido.getNome() == v.getNome():
                            pokimonDescansado = v
                    utils.descansar(pokimonEscolhido, pokimonDescansado,
                                    personagem)
                    utils.clear_screen()
                    print(
                        f'O Pokimon {pokimonEscolhido.getNome()} se sente pronto para batalha!'
                    )
                    time.sleep(2)
                    print(f'{personagem.getNome()} dormiu e acordou renovado!')
                    time.sleep(2)
                    break
                elif x == 2:
                    print('Saindo para o menu principal')
                    time.sleep(2)
                    break
                else:
                    print('\033[0;31mOpção inválida.\033[m')
                    time.sleep(2)
        elif x == 4:
            print('Comprar')
            time.sleep(2)
        elif x == 5:
            telaPokimons = 0
            while telaPokimons == 0:
                pokimomEscolhido = personagem.escolhaDePokimons()
                print(
                    f'Nome: {pokimomEscolhido.getNome()} HP: {pokimomEscolhido.getHp()} Ataque: {pokimomEscolhido.getAtaque()} Defesa: {pokimomEscolhido.getDefesa()}'
                )
                pokimomEscolhido.getImg()
                time.sleep(5)
                break
            time.sleep(2)
        elif x == 6:
            print(
                'Para ver a participação especial seu personagem deve possuir ao menos 3 Pokimons'
            )
            time.sleep(2)
        elif x == 7:
            print(
                'Para ver os agradecimentos especiais seu personagem deve possuir ao menos 4 Pokimons'
            )
            time.sleep(2)
        elif x == 8:
            telaVoltarMenuPersonagem = 0
            while telaVoltarMenuPersonagem == 0:
                utils.clear_screen()
                print('Tem certeza que deseja voltar para o menu de Personagens? Isso vai apagar seu progresso no jogo!')
                print('1 - Sim\n2 - Não')
                x = personagem.resposta()
                if x == 1:
                    print('Voltando ao menu de personagens...')
                    time.sleep(2)
                    inicioGame = 0
                    break
                elif x == 2:
                    break
                else:
                    print('\033[0;31mOpção inválida.\033[m')
                    time.sleep(2)
        elif x == 9:
            telaSairDoJogo = 0
            while telaSairDoJogo == 0:
                utils.clear_screen()
                print('Tem certeza que deseja sair do jogo? Isso vai apagar seu progresso no jogo!')
                print('1 - Sim\n2 - Não')
                x = personagem.resposta()
                if x == 1:
                    print('Obrigado por Jogar!')
                    time.sleep(2)
                    inicioGame = 30
                    break
                elif x == 2:
                    break
                else:
                    print('\033[0;31mOpção inválida.\033[m')
                    time.sleep(2)
        else:
            print('\033[0;31mOpção inválida.\033[m')
            time.sleep(2)
