
##### LARGURA, ALTURA E ÁREA #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 11:

Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada 
litro de tinta pinta uma área de 2 metros quadrados.

Link: https://youtu.be/mzSJpn9ldt4

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*25 + '\n'

print(separador_1)

# Dimensões da parede
print("Forneça as dimensões da parede, em metro.")
largura = float(input('Largura: '))
altura  = float(input('Altura: '))
area = largura * altura

# Rendimento da tinta (m²/L)
rendimento = 2

# Quantidade de tinta em litros
quant_tinta = round((area / rendimento) , 1)

print(separador_2)

# Resultado
print('São necessários {} litros de tinta para pintar uma parede de {} '
    .format(quant_tinta , area) + 'metros quadrados.')

print(separador_1)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################
