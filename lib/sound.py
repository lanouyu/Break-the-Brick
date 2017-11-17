import pygame
import util

def load():
    pygame.mixer.music.load(util.file_path('background.mp3'))
    pygame.mixer.music.play(-1)

def bounce_sound():
    bounce = pygame.mixer.Sound(util.file_path('bounce.ogg'))
    bounce.play()
