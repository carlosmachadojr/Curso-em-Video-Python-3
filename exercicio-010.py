
##### CONVERSOR DE MOEDAS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 10:

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre 
quantos dólares ela pode comprar.

Link: https://youtu.be/xM4AX3Lp2mo

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*25 + '\n'

print(separador_1)

real = float(input('Digite quanto você tem na carteira: R$ '))

dolar = 4.48    # Cotação do Dolar em 02/03/2020

print(separador_2)

print('Com R$ {} e Dolar cotado a R$ {}, você pode comprar U$ {}.'
.format(real , dolar , round(real/dolar,2)))

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
