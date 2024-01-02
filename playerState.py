import os
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
class playerState(pygame.sprite.Sprite):
    def __init__(self, champion: str, isPlayer2):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.cur_animation = 0
        self.champion = champion
        self.hp = 100
        self.isBlocking = False
        self.inAnimation = False
        self.MIN_HP_NUM = 0
        self.powerup_usable = False
        self.champAnimations = {"walk": [], "basic kick": [], "basic punch": [], "crouch": [], "jump": []}
        self.pos = {'x': 100, 'y': 300}
        self.jump = False
        self.velocity = 0
        self.start_frame = 0
        self.character_powerup_name = None
        self.isPlayer2 = isPlayer2
        self.load_animations("Dalsim")
        
    
    def load_animations(self, champion):
        
        """Will load the animations for the current champion into 
            champAnimations, and populate the dictinonary"""
        #for x in self.champAnimations.keys():
        for y in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'walk')))):
            self.image = pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'walk', f'{y}'))
            self.champAnimations[f"walk"].append(self.image)

        
    
    def update(self, key):
        if(self.isPlayer2):
            if key == pygame.K_UP:
                self.pos['y'] += -10
            if key == pygame.K_LEFT:
                self.pos['x'] += -10
                self.image = self.champAnimations["walk"][self.cur_animation]
                self.cur_animation += 1
                if self.cur_animation > len(self.champAnimations["walk"].get()):
                    self.cur_animation = 0
            elif key == pygame.K_RIGHT:
                self.pos['x'] += 10
                self.image = self.champAnimations["walk"][self.cur_animation]
                self.image = pygame.transform.flip(self.image, True, False)
                self.cur_animation += 1
        else:
            if key == pygame.K_w:
                self.pos['y'] += -10
            if key == pygame.K_a:
                self.pos['x'] += -10
            elif key == pygame.K_d:
                self.pos['x'] += 10

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



    def usePowerup(self, events):
        for event in events:
            if event.type == pygame.K_P:
                character_powerup_damage = character_powerups[self.champion][1]
                self.updateHp(character_powerup_damage)
