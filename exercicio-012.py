
##### PORCENTAGEM - CÁLCULO DE DESCONTOS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 12:

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
com 5% de desconto.

Link: https://youtu.be/4MAmKOT9FeU

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*25 + '\n'

print(separador_1)

preco = round(float(input('Qual o preço do produto? R$ ')) , 2)

desconto = 5    # em %

novo_preco = round(preco * (1 - desconto/100) , 2)

print(separador_2)

print('Com o desconto de 5' + '% ' + 'o produto que custa ' +
    'R$ {} passa a custar R$ {}.'.format(preco , novo_preco))

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
