
##### SORTEANDO UM ITEM DE UMA LISTA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 19:

Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça 
um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome 
do escolhido.

Link: https://youtu.be/_Nk02-mfB5I

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

from random import choice

separador = '\n' + '-'*80 + '\n'

print(separador)

aluno_1 = input('Digite o nome do primeiro aluno: ').title()
aluno_2 = input('Digite o nome do segundo aluno: ').title()
aluno_3 = input('Digite o nome do terceiro aluno: ').title()
aluno_4 = input('Digite o nome do quarto aluno: ').title()

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteado = choice(lista)

print('\nO aluno escolhido para apagar o quadro foi: {} '.format(sorteado))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
