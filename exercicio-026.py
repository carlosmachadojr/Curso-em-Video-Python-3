##### PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 026:

Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece
a letra "A", em que posição ela aparece a primeira vez e em que posição ela
aparece a última vez.

Link: https://youtu.be/23UOVEetNPY

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

texto = input('Digite uma frase:\n\n').lower().strip()

quantidade = texto.count('a')
primeira   = texto.find('a') + 1
ultima     = texto.rfind('a')  

if quantidade == '0':
    print("\nA letra 'A' aparece {} vezes, ".format(quantidade) +
    "sendo a primeira na posição {} e a última na posição {}."
    .format(primeira , ultima))
else:
    print("\nA frase digitada não contém a letra 'A'")

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
