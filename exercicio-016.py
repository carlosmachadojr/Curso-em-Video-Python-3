
##### PORÇÃO INTEIRA DE UM NÚMERO #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 16:

Crie um programa que leia um número Real qualquer pelo 
teclado e mostre na tela a sua porção Inteira.

Link: https://youtu.be/-iSbDpl5Jhw

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

from math import trunc

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*20 + '\n'

print(separador_1)

num = float(input('Digite um número real: '))

inteiro = trunc(num)

print(separador_2)

print('O valor digitado foi {} e sua porção inteira é {}.'.format(num,inteiro))

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
