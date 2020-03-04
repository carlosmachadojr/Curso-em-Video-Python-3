
##### PORCENTAGEM - REAJUSTE SALARIAL #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 13:

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento.

Link: https://youtu.be/cTkivN8XcJ0

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*25 + '\n'

print(separador_1)

salario = round(float(input('Qual salário do funcionário? R$ ')) , 2)

aumento = 15    # em %

novo_salario = round(salario * (1 + aumento/100) , 2)

print(separador_2)

print('Com o reajuste salarial de 15' + '% ' + 'o funcionário que ganhava '
    'R$ {}, passa a receber R$ {}.'.format(salario , novo_salario))

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
