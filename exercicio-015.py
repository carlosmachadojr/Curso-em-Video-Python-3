
##### ALUGUEL DE CARROS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 15:

Escreva um programa que pergunte a quantidade de km percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a 
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Link: https://youtu.be/I4NYUeetLAc

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*20 + '\n'

print(separador_1)

diarias = int(input('Quantidade de diárias: '))
quilometragem = round(float(input('\nQuilômetros percorridos: ')) , 2)

custo_diaria = 60
custo_km = 0.15

custo_total = diarias * custo_diaria + quilometragem * custo_km

print(separador_2)

print('Com um total de {} diárias e {} quilômetros percorridos, o valor a '
    .format(diarias , quilometragem) + 'pagar pelo aluguel do veículo ' +
    'é de: R$ {}.'.format(custo_total))

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
