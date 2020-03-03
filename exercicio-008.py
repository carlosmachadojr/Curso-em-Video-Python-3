
##### CONVERSOR DE MEDIDAS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 008:

Escreva um programa que leia um valor em metros e o exiba convertido em 
centímetros e milímetros.

Link: https://youtu.be/KjcdG05EAZc

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

m = round(float(input('Digite um valor em metro (m): ')),3)

dam = round(m * 0.1   , 3)
hm  = round(m * 0.01  , 3)
km  = round(m * 0.001 , 3)

dm  = round(m * 10   , 3)
cm  = round(m * 100  , 3)
mm  = round(m * 1000 , 3)

print('\nO valor {} metro(s) corresponde a: '.format(m))
print()
print('   {} decâmetro(s)' .format(dam))
print('   {} hectômetro(s)'.format(hm))
print('   {} quilômetro(s)'.format(km))
print()
print('   {} decímetro(s)' .format(dm))
print('   {} centímetro(s)'.format(cm))
print('   {} milimetro(s)' .format(mm))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
