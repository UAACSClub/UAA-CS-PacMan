import pygame
import os

pygame.init()

# Constant Variables
WIDTH = 1000
HEIGHT = 900
# CURR_DIR = os.path.dirname(__file__)

# Screen Setup
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def MainMenu():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


# Pygame Loop

MainMenu()
