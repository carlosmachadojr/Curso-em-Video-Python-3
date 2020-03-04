
##### CONVERSOR DE TEMPERATURAS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 14:

Escreva um programa que converta uma temperatura digitando em graus Celsius e 
converta para graus Fahrenheit.

Link: https://youtu.be/9l_Gay8BuAw

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*20 + '\n'

print(separador_1)

C = round(float(input('Qual a temperatura em graus Celsius? ')) , 2)

# C/5 = (F - 32)/9
# 9C  = 5 * (F - 32)
# 5 * (F - 32) = 9C
# F - 32 = 9C / 5
# F = 9C / 5 + 32

F = 32 + 9 * C / 5
F = round(F,2)

print(separador_2)

print('A temperatura de {}°C (Celcius) corresponde a {}°F (Fahrenheit).'
    .format(C , F))

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
