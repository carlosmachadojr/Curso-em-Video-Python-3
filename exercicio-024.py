##### VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 024:

Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o 
nome "SANTO".

Link: https://youtu.be/QroT8cZMRnc

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

cidade = input('Digite o nome de sua cidade: ').lower().strip()

print('santo' == cidade.split()[0])

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################