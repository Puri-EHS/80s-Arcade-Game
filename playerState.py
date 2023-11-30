import pygame
import os

class playerState():
    def __init__(self, champion: str, hp : int, isBlocking: bool, inAninmation: False):
        self.champion = champion
        self.hp = hp
        self.isBlocking = isBlocking
        self.inAnimation = inAninmation
        self.cur_powerups = None
        self.champAnimations = {}
        self.start_frame = 0
        self.pos = []
        
    
    def load_animations(self, champion):
        
        """Will load the animations for the current champion into 
            champAnimations, and populate the dictinonary"""
        self.images = pygame.image.load('Character_images', f'{self.champion}', 'Basic_Attacks', f'{x}' + '.jpg')
        
    
    def update(self, events, frames):
        """ Will update after any action is taken
        
        """


    def updateHp(self, attack):
        """Will update the amount of helath remaining based on
            the attack the user was hit with  

        Args:
            attack (_type_): _description_
        """
        
