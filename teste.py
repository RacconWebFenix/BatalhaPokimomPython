'''  print('Descansar')
            telaDescansar = 0
            while telaDescansar == 0:
                pokimonDescansado = 0
                pokimonEscolhido = personagem.escolhaDePokimons()
                for v in pokimonAleatorioSelvagem:
                    if pokimonEscolhido.gerNome() == v.getNome():
                        pokimonDescansado = v 
                
                utils.descansar(pokimonEscolhido, pokimonDescansado, personagem)
                utils.clear_screen()
                print(f'O Pokimon {pokimonEscolhido.getNome()} se sente pronto para batalha!')
                time.sleep(2)
                print(f'{personagem.getNome()} dormir e acordou renovado!')
                time.sleep(2)            '''