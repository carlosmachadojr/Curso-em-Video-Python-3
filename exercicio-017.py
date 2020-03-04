
##### CATETOS E HIPOTENUSA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 17:

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

Link: https://youtu.be/vmPW9iWsYkY

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

from math import hypot

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*20 + '\n'

print(separador_1)

print('Digite os catetos de um triângulo retângulo:\n')

cat_1 = float(input('Cateto 1: '))
cat_2 = float(input('Cateto 1: '))

hipotenusa = hypot(cat_1 , cat_2)

print('\nUm triângulo retângulo com catetos iguais a ' +
    '{} e {} possui hipotenusa igual a {}'.format(cat_1 , cat_2 , hipotenusa))

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
