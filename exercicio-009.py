
##### TABUADA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 009:

Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua 
tabuada.

Link: https://youtu.be/qajq3SI0QQs

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

num = int(input('Digite o número para ver sua tabuada: '))

print('\nTabuada do {}:\n'.format(num))

print('{} × {:2} = {}'.format(num , 1  , num * 1))
print('{} × {:2} = {}'.format(num , 2  , num * 2))
print('{} × {:2} = {}'.format(num , 3  , num * 3))
print('{} × {:2} = {}'.format(num , 4  , num * 4))
print('{} × {:2} = {}'.format(num , 5  , num * 5))
print('{} × {:2} = {}'.format(num , 6  , num * 6))
print('{} × {:2} = {}'.format(num , 7  , num * 7))
print('{} × {:2} = {}'.format(num , 8  , num * 8))
print('{} × {:2} = {}'.format(num , 9  , num * 9))
print('{} × {:2} = {}'.format(num , 10 , num * 10))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
