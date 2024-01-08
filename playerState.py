import os
import pygame
#the first parameter is the powerup. the second parameter is the damage it does  
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
        self.cur_type_animation = "idle"
        self.champion = champion
        self.hp = 100
        self.isBlocking = False
        self.inAnimation = False
        self.MIN_HP_NUM = 0
        self.powerup_usable = False
        self.champAnimations = {"walk": [], "idle": [], "basic kick": [], "basic punch": [], "crouch": [], "jump": []}
        self.cur_pressed_keys = {"left": False, "right": False, "down": False}
        self.pos = {'x': 100, 'y': 300}
        self.jump = False
        self.velocity = 0
        self.start_frame = 0
        self.character_powerup_name = None
        self.isPlayer2 = isPlayer2
        self.cur_facing_left = isPlayer2
        self.cur_frame = 0
        self.load_animations("Dhalsim")
        if isPlayer2:
            self.rect = self.image.get_rect()
            self.rect.x += 400
        self.rect.y -= 300
        
    
    def load_animations(self, champion):
        
        """Will load the animations for the current champion into 
            champAnimations, and populate the dictinonary"""
        #for x in self.champAnimations.keys():
        for y in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'walk'))) - 1):
            self.image = pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'walk', f'{y}.png'))
            self.champAnimations[f"walk"].append(self.image)
        
        for x in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'idle'))) - 1):
            self.champAnimations[f"idle"].append(pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'idle', f'{x}.png')))
        
        for z in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'jump'))) - 1):
            self.champAnimations[f"jump"].append(pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'jump', f'{x}.png')))
    def update(self, key):
        if(self.isPlayer2):

            if(key.type == pygame.KEYDOWN):
                if key == pygame.K_LEFT:
                    self.cur_pressed_keys["left"] = True
                    self.cur_type_animation = "walk"
                    self.cur_animation = 0
                if key == pygame.K_RIGHT:
                    self.cur_pressed_keys["right"] = True
                    self.cur_type_animation = "walk"
            if(key.type == pygame.KEYUP):
                if key == pygame.K_LEFT:
                    self.cur_pressed_keys["left"] = False
                    self.frame = 0
                if key == pygame.K_RIGHT:
                    self.cur_pressed_keys["right"] = False
                    self.frame = 0
        else:
            if(key.type == pygame.KEYDOWN):
                if key == pygame.K_a:
                    self.cur_pressed_keys["left"] = True
                    self.cur_type_animation = "walk"
                    self.cur_animation = 0
                if key == pygame.K_d:
                    self.cur_pressed_keys["right"] = True
                    self.cur_type_animation = "walk"
            if(key.type == pygame.KEYUP):
                if key == pygame.K_a:
                    self.cur_pressed_keys["left"] = False
                    self.frame = 0
                if key == pygame.K_d:
                    self.cur_pressed_keys["right"] = False
                    self.frame = 0
        if self.cur_pressed_keys["left"]:
                self.pos['x'] += -10
                self.image = self.champAnimations["walk"][self.cur_animation]
                if self.cur_facing_left != True:
                    self.image = pygame.transform.flip(self.image, True, False)
        if self.cur_pressed_keys["right"]:
                self.pos['x'] += 10
                self.image = self.champAnimations["walk"][self.cur_animation]
                if self.cur_facing_left:
                    self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.champAnimations["idle"][self.cur_animation]
            self.cur_type_animation = "idle"
    
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
                powerup_length = 25 
                while powerup_length > 0:
                    character_powerup_damage = character_powerups[self.champion][1]
                    self.updateHp(character_powerup_damage)
