##### PAR OU ÍMPAR #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 030:

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou 
ÍMPAR.

Link: https://youtu.be/4vFCzKuHOn4

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    verificacao = 'PAR'
else:
    verificacao = 'ÍMPAR'

print('\nO número digitado é {}.'.format(verificacao))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################