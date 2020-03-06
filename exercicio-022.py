##### ANALISADOR DE TEXTOS #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 022:

Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

Link: https://youtu.be/EQQt-6QqXOs

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

separador = '\n' + '-'*80 + '\n'

print(separador)

nome = input('Digite o seu nome completo: ').strip()

maiusculas = nome.upper()
minusculas = nome.lower()
letras_compl = len(nome.replace(' ',''))
letras_prime = len(nome.split()[0])

print()
print('Seu nome em letras maiúsculas é {}: '.format(maiusculas))
print('Seu nome em letras minúsculas é {}: '.format(minusculas))
print('Seu nome completo contém {} letras.'.format(letras_compl))
print('Seu primeiro nome contém {} letras.'.format(letras_prime))

print(separador)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################