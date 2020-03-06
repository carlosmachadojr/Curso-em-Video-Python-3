##### CUSTO DA VIAGEM #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 031:

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o 
preço da passagem, cobrando R$0,50 por Km para viagens de até 200 km e R$0,45 
parta viagens mais longas.

Link: https://youtu.be/PGqHyzWoagc

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

distancia = float(input('Qual a distância de sua viagem? '))

if distancia <= 200:
    preco_por_km = 0.50
else:
    preco_por_km = 0.45

preco = distancia * preco_por_km

print('\nO custo da viagem é R$ {}'.format(round(preco,2)))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
