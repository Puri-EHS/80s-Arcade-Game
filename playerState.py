import os
import pygame
from Game import Game
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

# formatted as [punch, kick]

character_damage_values = {
            "Ryu": [7, 10],
            "Balrog": [10, 7],
            "Blanka": [7, 8],
            "Dhalsim": [5, 11],
            "Sagat":  [10, 6],
            "Guile": [8, 8],
            "Vega": [9, 7],
            "Chun Li": [6, 9],
            "Zangief": [7, 7],
            "E Honda": [9, 7],
            "M Bison": [9, 6],
            "Ken": [7, 11]
}

class playerState(pygame.sprite.Sprite):
    def __init__(self, champion: str, isPlayer2):
        pygame.sprite.Sprite.__init__(self)
        self.cur_animation = 0
        self.cur_type_animation = "idle"
        self.champion = champion
        self.hp = 100
        self.isBlocking = False
        self.inAnimation = False
        self.isAttacking = False
        self.attackValue = 0
        self.MIN_HP_NUM = 0
        self.powerup_usable = False
        self.champAnimations = {"walk": [], "idle": [], "basic kick": [], "basic punch": [], "crouch": [], "jump": []}
        self.cur_pressed_keys = {"left": False, "right": False, "down": False, "kick": False, "punch": False}
        self.pos = {'x': 100, 'y': 300}
        self.jump = False
        self.velocity = 0
        self.start_frame = 0
        self.character_powerup_name = None
        self.isPlayer2 = isPlayer2
        self.cur_facing_left = isPlayer2
        self.use_power_up = False
        self.cur_frame = 0
        self.load_animations(f"{champion}")
        self.image = self.champAnimations["idle"][0]
        self.rect = self.image.get_rect()
        if isPlayer2:
            self.rect.x += 700
        else:
            self.rect.x += 50
        self.rect.y += 350
        
    
    def load_animations(self, champion):
        
        """Will load the animations for the current champion into 
            champAnimations, and populate the dictinonary"""
        #for x in self.champAnimations.keys():
        #for y in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'walk'))) - 1):
            #self.champAnimations[f"walk"].append(pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'walk', f'{y}.png')))
        
        for x in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'idle'))) - 1):
            self.champAnimations[f"idle"].append(pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'idle', f'{x}.png')))
        
        #for z in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'jump'))) - 1):
             #self.champAnimations[f"jump"].append(pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'jump', f'{z}.png')))
        
        
    
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

                if key == pygame.K_PERIOD:
                     self.cur_pressed_keys["punch"] = True
                     self.cur_type_animation = "punch"
                if key == pygame.K_SLASH:
                     self.cur_pressed_keys["kick"] = True
                     self.cur_type_animation = "kick"

            if(key.type == pygame.KEYUP):
                self.frame = 0
                if key == pygame.K_LEFT:
                    self.cur_pressed_keys["left"] = False
                if key == pygame.K_RIGHT:
                    self.cur_pressed_keys["right"] = False

                if key == pygame.K_PERIOD:
                     self.cur_pressed_keys["punch"] = False
                     self.isAttacking = False
                if key == pygame.K_SLASH:
                     self.cur_pressed_keys["kick"] = False
                     self.isAttacking = False
        else:
            if(key.type == pygame.KEYDOWN):
                if key == pygame.K_a:
                    self.cur_pressed_keys["left"] = True
                    self.cur_type_animation = "walk"
                    self.cur_animation = 0
                if key == pygame.K_d:
                    self.cur_pressed_keys["right"] = True
                    self.cur_type_animation = "walk"

                
                if key == pygame.K_f:
                     self.cur_pressed_keys["punch"] = True
                     self.cur_type_animation = "punch"
                if key == pygame.K_g:
                     self.cur_pressed_keys["kick"] = True
                     self.cur_type_animation = "kick"

            if(key.type == pygame.KEYUP):
                self.frame = 0
                if key == pygame.K_a:
                    self.cur_pressed_keys["left"] = False
                if key == pygame.K_d:
                    self.cur_pressed_keys["right"] = False

                if key == pygame.K_f:
                     self.cur_pressed_keys["punch"] = False
                     self.isAttacking = False
                if key == pygame.K_g:
                     self.cur_pressed_keys["kick"] = False
                     self.isAttacking = False

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

        if self.cur_pressed_keys["punch"]:
             self.image = self.champAnimations["basic punch"][self.cur_animation]
             self.isAttacking = True
             self.attackValue = character_damage_values[self.champion][0]
        if self.cur_pressed_keys["kick"]:
             self.image = self.champAnimations["basic kick"][self.cur_animation]
             self.isAttacking = True
             self.attackValue = character_damage_values[self.champion][1]



        else:
            self.image = self.champAnimations["idle"][self.cur_animation]
            self.cur_type_animation = "idle"
    
    def getPosition(self):
        return self.pos

        

    def updateHp(self, attackVal):
        if self.isBlocking == False:
             self.hp -= attackVal

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
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_p: 
                    text_timer = 1.75 
                    while text_timer > 0.0:
                        font = pygame.font.Font(None, 26)
                        text = font.render(self.getPowerup(), True, (0,0,0)) 
                        Game.game_screen.blit(text, (400,300)) 
                        text_timer -= 1
                    powerup_length = 25 
                    while powerup_length > 0:
                        character_powerup_damage = character_powerups[self.champion][1]
                        self.attackValue += character_powerup_damage
                        powerup_length -= 1
