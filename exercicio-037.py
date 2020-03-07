##### CONVERSOR DE BASES NUMÉRICAS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 037:

Escreva um programa em Python que leia um número inteiro qualquer e peça para o 
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 
3 para hexadecimal.

Link: https://youtu.be/B3F0IjH5WAM

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

num = int(input('Digite um número inteiro: '))

print('\nDigite a base para conversão:')
print('\n[ 02 ] Binário\n[ 08 ] Octal\n[ 16 ] Hexadecimal\n')

while True:
    base = input('Opção escolhida: ')
    if base in ['2' , '8' , '16']:
        break

if base == '2':
    conv = str(bin(num))[2:]
    base_str = 'BINÁRIA'
if base == '8':
    conv = str(oct(num))[2:]
    base_str = 'OCTAL'
if base == '16':
    conv = str(hex(num))[2:]
    base_str = 'HEXADECIMAL'

print('\nO número {} convertido para a base {} é {}.'.format(num,base_str,conv))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
