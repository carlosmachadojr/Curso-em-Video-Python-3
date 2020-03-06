##### RADAR ELETRÔNICO #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 029:

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 
R$7,00 por cada Km acima do limite.

Link: https://youtu.be/hgJ_ETNGSj8

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

velocidade = float(input('Qual a velocidade atual? '))
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('\nVocê ultrapassou o limite de velocidade de 80 km/h e foi ' +
        'multado em {}'.format(multa))

print('\nTenha um bom dia! Dirija com segurança!')

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################