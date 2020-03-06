##### SEPARANDO DÍGITOS DE UM NÚMERO #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 023:

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos 
dígitos separados.

Link: https://youtu.be/wD2aerLMBWA

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

numero = int(input('Digite um número inteiro de 0 a 9999 --> '))

unidade = numero // 1 % 10
dezena  = numero // 10 % 10
centena = numero // 100 % 10
milhar  = numero // 1000 % 10

print()
print('Unidade: {}'.format(unidade))
print('Dezena:  {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar:  {}'.format(milhar))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################