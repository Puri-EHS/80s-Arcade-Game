import pygame
class spritesheet:
    def __init__(self, filename, row, col):
        self.sheet = pygame.image.load(filename)