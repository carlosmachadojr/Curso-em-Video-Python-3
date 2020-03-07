##### APROVANDO EMPRÉSTIMO #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 036:

Escreva um programa para aprovar o empréstimo bancário para a compra de uma 
casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele 
vai pagar. A prestação mensal não pode exceder 30% do salário ou então o 
empréstimo será negado.

Link: https://youtu.be/IV13X0QOMU8

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

valor   = float(input('Digite o valor do imóvel: R$ '))
salario = float(input('Qual o salário do comprador: R$ '))
financ  = int(input('Quantos anos de financiamento: '))

prestacao = round(valor / (financ * 12), 2)
valor = round(valor , 2)

print('''
Uma casa no valor de R$ {} financiada em R$ {} nos resulta em {} prestações 
de R$ {}.'''.format(valor , financ , financ * 12 , prestacao))

if prestacao <= 0.30 * salario:
    print('\nEmpréstimo APROVADO.')
else:
    print('\nEmpréstimo NEGADO.')

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
