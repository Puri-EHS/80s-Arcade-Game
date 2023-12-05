#the first parameter is the powerup. the second parameter is the damage it does 
import pygame 
import Game
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
        self.champAnimations = {}
        self.pos = {'x': 100, 'y': 300}
        self.jump = False
        self.velocity = 0
        self.start_frame = 0
        
    
    def load_animations(self, champion):
        
        """Will load the animations for the current champion into 
            champAnimations, and populate the dictinonary"""
        self.images = pygame.image.load('Character_images', f'{self.champion}', 'Basic_Attacks', f'{x}' + '.jpg')
        
    
    def update(self, key):
        
        if key == pygame.K_DOWN:
            if self.pos['y'] != 0:
                self.pos['y'] += -10
        if key == pygame.K_LEFT:
            self.pos['x'] += -10
        elif key == pygame.K_RIGHT:
            self.pos['x'] += 10
        """ Will update after any action is taken

        """
    
    def getPosition(self):
        return self.pos

        

    def updateHp(self, attack):
        """Will update the amount of helath remaining based on
            the attack the user was hit with  

        Args:
            attack (_type_): _description_
        """
    def getPowerup(self):
        character_powerup_name = character_powerups[self.champion][0]  
        return character_powerup_name   

    
                                                     
    def usePowerup(self):
        while Game.running:
            for event in Game.events:
                if event.type == pygame.K_P:
                    character_powerup_damage = character_powerups[self.champion][1]
                    self.updateHp(character_powerup_damage)
