##### ANO BISSEXTO #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 032:

Faça um programa que leia um ano qualquer e mostre se ele é bissexto

Link: https://youtu.be/cyGY_83m4Xw

"""

# DEFINIÇÃO DE ANO BISSEXTO:
"""
Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 
366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada 
quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400)

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

from datetime import date

separador = '\n' + '-'*80 + '\n'

print(separador)

ano = int(input('Que ano você quer analisar? Digite 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

verificacao = 'NÃO É'

if ano % 4 == 0:                            # Regra geral
    if ano % 100 == 0 and ano % 400 != 0:   # Exceção
        pass
    else:
        verificacao = 'É'

print('\nO ano {} {} bissexto.'.format(ano , verificacao))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
