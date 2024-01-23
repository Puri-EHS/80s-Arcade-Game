import os
import pygame
#the first parameter is the powerup. the second parameter is the damage it does  
character_powerups = {
            "Ryu": ["Fireball", 70], 
            "Balrog": ["Strong punch", 80], 
            "Blanka": ["Energized Attack", 65], 
            "Dhalsim": ["Fury Fire", 50],  
            "Sagat":  ["Rapid Hit", 45],  
            "Guile": ["Flash Punch", 40], 
            "Vega": ["Super Claw Attack", 130], 
            "Chun Li": ["Power Puunch", 25],  
            "Zangief": ["Lariat", 15], 
            "E Honda": ["Super Might", 100], 
            "M Bison": ["Super Strength", 110], 
            "Ken": ["Lgitightning Punch", 50]
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
    def __init__(self, champion: str, isPlayer2 = False):
        pygame.sprite.Sprite.__init__(self)
        self.cur_animation = 0
        self.cur_type_animation = "idle"
        self.champion = champion
        self.hp = 100
        self.isBlocking = False
        self.isAttacking = False
        self.attackValue = 0
        self.MIN_HP_NUM = 0
        self.powerup_usable = False
        self.champions_background_color = {"Balrog": [0, 0, 0], "Blanka": [], "ChunLi": [], "Dhalsim": [32, 144, 160], "E Honda": [], "Guile": [], "Ken": [128, 184, 168], "M Bison": [], "Ryu": [], "Sagat": [], "Vega":[], "Zangief": []}
        self.champAnimations = {"walk": [], "idle": [], "basic kick": [], "basic punch": [], "crouch": [], "jump": []}
        self.cur_pressed_keys = {"left": False, "right": False, "down": False, "kick": False, "punch": False, "powerup": False}
        self.jump = False
        self.velocity = 0
        self.character_powerup_name = None
        self.isPlayer2 = isPlayer2
        self.cur_facing_left = isPlayer2
        self.use_power_up = False
        self.cur_frame = 0
        self.load_animations()
        self.image = self.champAnimations["idle"][0]
        self.rect = self.image.get_rect()
        if isPlayer2:
            self.rect.x += 700
        else:
            self.rect.x += 50
        self.rect.y += 350
        
    
    def load_animations(self):
        
        """Will load the animations for the current champion into 
            champAnimations, and populate the dictinonary"""
        #for x in self.champAnimations.keys():
        for y in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'walk'))) - 1):
            image = pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'walk', f'{y}.png'))
            if self.isPlayer2:
                 image = pygame.transform.flip(image, True, False)
            image.convert_alpha()
            image.set_colorkey(self.champions_background_color[f"{self.champion}"])
            self.champAnimations[f"walk"].append(image)
        
        for x in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'idle'))) - 1):
            image = pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'idle', f'{x}.png'))
            if self.isPlayer2:
                 image = pygame.transform.flip(image, True, False)
            image.convert_alpha()
            image.set_colorkey(self.champions_background_color[f"{self.champion}"])
            self.champAnimations[f"idle"].append(image)
        
 """       for z in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'jump'))) - 1):
            image = pygame.image.load(os.path.join('Character_images', f'{self.champion}', 'jump', f'{z}.png'))
            if self.isPlayer2:
                 image = pygame.transform.flip(image, True, False)
            image.convert_alpha()
            image.set_colorkey(self.champions_background_color[f"{self.champion}"])
            self.champAnimations[f"jump"].append(image)

        for w in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'crouch'))) - 1):
            image = pygame.image.load(os.path.join('Character_Images',f'{self.champion}','crouch',f'{w}.png'))
            if self.isPlayer2:
                image = pygame.transform.flip(image,True,False)
            image.convert_alpha()
            image.set_colorkey(self.champions_background_color[f"{self.champion}"])
            self.champAnimations[f"crouch"].append(image)
            
        for v in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'basic kick'))) - 1):
            image = pygame.image.load(os.path.join('Character_Images',f'{self.champion}','basic kick',f'{v}.png'))
            if self.isPlayer2:
                image = pygame.transform.flip(image,True,False)
            image.convert_alpha()
            image.set_colorkey(self.champions_background_color[f"{self.champion}"])
            self.champAnimations[f"basic kick"].append(image)
        
        
        for u in range(len(os.listdir(os.path.join('Character_images', f'{self.champion}', 'basic punch'))) - 1):
            image = pygame.image.load(os.path.join('Character_Images',f'{self.champion}','basic punch',f'{u}.png'))
            if self.isPlayer2:
                image = pygame.transform.flip(image,True,False)
            image.convert_alpha()
            image.set_colorkey(self.champions_background_color[f"{self.champion}"])
            self.champAnimations[f"basic punch"].append(image)
            
            """
                    
        
    
    def update(self):
        if self.isAttacking == False:
            if self.cur_pressed_keys["left"]:
                    self.rect.x += -5
                    self.cur_frame += 1
                    if self.cur_frame/5 >= len(self.champAnimations["walk"]):
                         self.cur_frame = 0
                    self.image = self.champAnimations["walk"][self.cur_frame//5]
                    if self.cur_facing_left != True:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.cur_facing_left = True
            elif self.cur_pressed_keys["right"]:
                    self.rect.x += 5
                    self.cur_frame += 1
                    if self.cur_frame/5 >= len(self.champAnimations["walk"]):
                         self.cur_frame = 0
                    self.image = self.champAnimations["walk"][self.cur_frame//5]
                    if self.cur_facing_left:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.cur_facing_left = False
            else:
                if self.cur_frame >= len(self.champAnimations["idle"]):
                         self.cur_frame = 0
                self.image = self.champAnimations["idle"][self.cur_frame]
                if self.cur_facing_left != True:
                     self.image = pygame.transform.flip(self.image, True, False)
                self.cur_type_animation = "idle"
        else:
            if self.cur_pressed_keys["punch"]:
                 self.image = self.champAnimations["basic punch"][self.cur_animation]
                 self.attackValue = character_damage_values[self.champion][0]
            if self.cur_pressed_keys["kick"]:
                 self.image = self.champAnimations["basic kick"][self.cur_animation]
                 self.attackValue = character_damage_values[self.champion][1]

    def getPosition(self):
        return self.rect

        

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

    #def usePowerup(self, events):
    #    for event in events: 
    #        if event.type == pygame.KEYDOWN: 
    #            if event.key == pygame.K_p: 
    #                text_timer = 4 
    #                while text_timer > 0.0:
    #                    font = pygame.font.Font(None, 26)
    #                    if self.isPlayer2: 
    #                        text = font.render("Player 2 Uses " + self.getPowerup(), True, (0,0,0)) 
    #                    else: 
    #                        text = font.render("Player 1 Uses " + self.getPowerup(), True, (0,0,0))  
    #                    Game.game_screen.blit(text, (400,300)) 
    #                    text_timer -= 1.0
    #                powerup_length = 25 
    #                counter = 0 
    #                while powerup_length >= counter: 
    #                    character_powerup_damage = character_powerups[self.champion][1]
    #                    self.attackValue += character_powerup_damage
    #                    counter+=1
