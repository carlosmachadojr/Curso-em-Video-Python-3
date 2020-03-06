##### ANALISANDO TRIÂNGULO V1.0 #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 035:

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
se elas podem ou não formar um triângulo.

Link: https://youtu.be/NZiNphKkxhg

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

c1 = float(input('Digite o comprimento do primeiro segmento: '))
c2 = float(input('Digite o comprimento do segundo segmento: '))
c3 = float(input('Digite o comprimento do terceiro segmento: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    validacao = 'PODEM'
else:
    validacao = 'NÃO PODEM'

print('\nOs segmentos medindo {}, {} e {}, {} formar um triângulo.'
    .format(c1 , c2 , c3 , validacao))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
