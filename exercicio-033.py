##### MAIOR E MENOR VALOR #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 034:

Faça um programa que leia três números e mostre qual é o maior e qual é o 
menor.

Link: https://youtu.be/a_8FbW5oH6I

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = max(n1 , n2 , n3)
menor = min(n1 , n2 , n3)


print('\nO maior número é o {}.'.format(maior))
print(  'O menor número é o {}.'.format(menor))


print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
