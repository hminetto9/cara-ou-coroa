import random
from time import sleep

opcoes_moeda = ['Cara', "Coroa"]
escolha_jogador = int(input('Escolha 1 para Cara e 2 para Coroa: '))

if escolha_jogador not in [1, 2]:
    print('Por favor, escolha 1 ou 2.')
else:
    resultado_moeda = random.choice(opcoes_moeda)

    print('Jogamos a moeda e...')
    for n in range(3, 0, -1):
        print(n)
        sleep(1)
    print(f'Caiu {resultado_moeda}!')

    if (resultado_moeda == 'Cara' and escolha_jogador == 1) or \
       (resultado_moeda == 'Coroa' and escolha_jogador == 2):
        print('VOCÊ GANHOU!')
    else:
        print('Você perdeu.')
