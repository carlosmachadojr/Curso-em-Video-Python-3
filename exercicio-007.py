
##### MÉDIA ARITMÉTICA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 007:

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a 
sua média.

Link: https://youtu.be/_QfISzy0IKs

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80

print(separador)

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('\nDigite a segunda nota: '))

media = (n1 + n2) / 2
media = round(media,1)

print('\nA média das notas é: {}'.format(media))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
