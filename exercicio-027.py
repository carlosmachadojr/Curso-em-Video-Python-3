##### PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 027:

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.

Link: https://youtu.be/SifYYsXhLM8

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

nome = input('Digite o seu nome completo: ').lower().strip()

primeiro = nome.split()[0].title()
ultimo   = nome.split()[-1].title()

print()
print('Seu primeiro nome é: {}. '.format(primeiro))
print('Seu último nome é: {}. '.format(ultimo))
print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################