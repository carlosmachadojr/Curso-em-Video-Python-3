##### PROCURANDO UMA STRING DENTRO DE OUTRA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 025:

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no 
nome.

Link: https://youtu.be/WHWGz2Dy1ZU

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

nome = input('Digite o seu nome completo: ').lower().strip()

print("\nSeu nome tem 'Silva'? {}".format('silva' in nome))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################