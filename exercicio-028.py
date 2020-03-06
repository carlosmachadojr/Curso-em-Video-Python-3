##### JOGO DE ADVINHAÇÃO V1.0 #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 028:

Escreva um programa que faça o computador "pensar" em um número inteiro entre 
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo 
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

Link: https://youtu.be/kchC5KLZSZ4

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

from random import randint

separador = '\n' + '-'*80 + '\n'

print(separador)

print('JOGO DE ADVINHAÇÃO')

print('\nTente advinhar o número escolhido pelo computador')

palpite = int(input('\nDigite um número inteiro entre 0 e 5 --> '))

numero = randint(0,5)

print()

if palpite == numero:
    print('PARABÉNS, você acertou! O número escolhido pelo computador foi o {}.'
        .format(numero))
else:
    print('ERROU! O número escolhido pelo computador foi o {} e não o {}.'
        .format(numero , palpite))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################