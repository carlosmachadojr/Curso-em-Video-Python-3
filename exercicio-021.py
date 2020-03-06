##### EXECUTANDO UM ARQUIVO MP3 #####

""" CURSO EM VÍDEO - EXERCÍCIO PYTHON 021:

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

Link: https://youtu.be/9FiEji_fzvk

"""

###############################################################################
### INÍCIO DO PROGRAMA ########################################################
###############################################################################

# NÃO FUNCIONOU
"""
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3)
pygame.mixer.music.play()
pygame.event.wait()
"""

# FUNCIONOU
from pygame import mixer
mixer.init()
mixer.music.load('ex1.mp3')
mixer.music.play()
import time
time.sleep(360)

###############################################################################
### FIM DO PROGRAMA ###########################################################
###############################################################################