#the first parameter is the powerup. the second parameter is the damage it does 
import pygame 
character_powerups = {
            "Ryu": ["Fireball", 70], 
            "Balrog": ["Superpunch", 80], 
            "Blanka": ["Energized Attack", 65], 
            "Dhalsim": ["Fury Fire", 50],  
            "Sagat":  ["Rapid Hit", 45],  
            "Guile": ["Flash Kick", 40], 
            "Vega": ["Super Claw Attack", 130], 
            "Chun Li": ["Power Kick", 25],  
            "Zangief": ["Lariat", 15], 
            "E Honda": ["Super Might", 100], 
            "M Bison": ["Super Strength", 110], 
            "Ken": ["Super Speed", 50]
        }
class playerState():
    def __init__(self, champion: str, hp : int, isBlocking: bool, inAninmation: False):
        self.champion = champion
        self.hp = hp
        self.isBlocking = isBlocking
        self.inAnimation = inAninmation
        self.MIN_HP_NUM = 0
        self.powerup_usable = False
        self.champAnimations = {}
        self.character_powerup_name = None
    
    def load_animations(self, champion):
        
        """Will load the animations for the current champion into 
            champAnimations, and populate the dictinonary"""
        self.images = pygame.image.load()
    
    def update(self, events, frames):
        """ Will update after any action is taken
        
        """
    def updateHp(self, attack, power_up:None):
        """Will update the amount of helath remaining based on
            the attack the user was hit with  

        Args:
            attack (_type_): _description_
        """
    def setPowerup(self):
        if self.powerup_usable:
            self.character_powerup_name = character_powerups[self.champion][0]  
    def usePowerup(self):
        character_powerup_damage = character_powerups[self.champion][1]
        self.updateHp(None, character_powerup_damage)
    def getHp(self):
        """"gets the remaining hp after an attack"""
