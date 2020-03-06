##### AUMENTOS MÚLTIPLOS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 034:

Escreva um programa que pergunte o salário de um funcionário e calcule o valor 
do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

Link: https://youtu.be/Sfadj_AzKHw

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    aumento = 10
else:
    aumento = 15

salario_novo = round(salario * (1 + aumento / 100),2)

print('''\n
O funcionário com salário atual de R$ {}, com o aumento de {}% passará a 
receber R$ {}.'''.format(salario , aumento , salario_novo))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
