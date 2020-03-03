
##### DISSECANDO UMA VARIÁVEL  #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 004:

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

Link: https://youtu.be/tHYxjJxtJko

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

entrada = input('Digite algo: ')

print()

print('O tipo primitivo desse valor é {} '.format(type(entrada)))
print('Só tem espaços? {}'.format(entrada.isspace()))
print('É numérico? {}'.format(entrada.isnumeric()))
print('É alfabético? {}'.format(entrada.isalpha()))
print('É alfanumérico? {}'.format(entrada.isalnum()))
print('Está em letras maiúsculas: {}'.format(entrada.islower()))
print('Está em letras minúsculas: {}'.format(entrada.isupper()))
print('Está capitalizado? {}' .format(entrada.istitle()))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
