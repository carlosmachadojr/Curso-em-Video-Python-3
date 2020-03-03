""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 002:

Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

Link: https://youtu.be/FNqdV5Zb_5Q

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*15 + '\n'

print(separador_1)

nome = input('Digite o seu nome: ')
mensagem = 'Olá {}, seja muito bem vindo(a)!'.format(nome.title())

print(separador_2)
print(mensagem)
print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
