
##### SORTEANDO UMA ORDEM NUMA LISTA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 20:

O mesmo professor do desafio 019 quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
mostre a ordem sorteada.

Link: https://youtu.be/OPh0nngbBSY

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

from random import shuffle

separador = '\n' + '-'*80 + '\n'

print(separador)

aluno_1 = input('Digite o nome do primeiro aluno: ').title()
aluno_2 = input('Digite o nome do segundo aluno: ').title()
aluno_3 = input('Digite o nome do terceiro aluno: ').title()
aluno_4 = input('Digite o nome do quarto aluno: ').title()

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

shuffle(lista)

print(lista)
print('\nA ordem da apresentação será:')
print('{}'.format(', '.join(lista)))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
