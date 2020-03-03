
##### DOBRO, TRIPLO E RAIZ QUADRADA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 006:

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

Link: https://youtu.be/mqcNw_dhl8I

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

num = abs(int(input('Digite um número inteiro positivo: ')))

dobro  = num * 2
triplo = num * 3
raiz   = round((num) ** 0.5 , 2)

print()

print('O dobro de {} vale: {}'.format(num , dobro))
print('O triplo de {} vale: {}'.format(num , triplo))
print('A raiz quadrada de {} vale: {}'.format(num , raiz))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
