
##### SENO, COSSENO E TANGENTE #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 18:

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
cosseno e tangente desse ângulo.

Link: https://youtu.be/9GvsphwW26k

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

from math import sin, cos, tan, radians

separador = '\n' + '-'*80 + '\n'

print(separador)

angulo = float(input('Digite o valor do ângulo: '))

angulo_rad = radians(angulo)

seno     = round(sin(angulo_rad) , 2) 
cosseno  = round(cos(angulo_rad) , 2)
tangente = round(tan(angulo_rad) , 2)

print('\nO seno de {}° é {}'.format(angulo , seno))
print('O cosseno de {}° = {}'.format(angulo , cosseno))
print('A tangente de {}° = {}'.format(angulo , tangente))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
