import pygame
from playerState import playerState

class player2(playerState):

    def __init__(self, champion: str, isPlayer2=True):
        super().__init__(champion, isPlayer2)

    def update(self, events):
        for event in events:
            if((event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP)) and self.isAttacking == False:
                self.update_action(event)
                self.update_continuous(event)
                if (event.key == pygame.K_l): 
                    self.usePowerup()
        return super().update()

    def update_action(self, event):
        if event.key == pygame.K_UP:
            self.cur_type_animation = 'jump'
            self.jump = True
            self.isBlocking = False
        if event.key == pygame.K_PERIOD:
            self.cur_type_animation = "punch"
            self.isAttacking = True
            self.isBlocking = False
        if event.key == pygame.K_SLASH:
            self.cur_type_animation = "kick"
            self.isAttacking = True
            self.isBlocking = False
        if event.key == pygame.K_RSHIFT:
            self.cur_pressed_keys["powerup"] = True   

    def update_continuous(self, event):
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                if event.key == pygame.K_RIGHT:
                    self.cur_pressed_keys["right"] = True
                if event.key == pygame.K_LEFT:
                    self.cur_pressed_keys["left"] = True
                self.cur_type_animation = "walk"
                self.cur_animation = 0
        if(event.type == pygame.KEYUP):
            self.frame = 0
            if event.key == pygame.K_LEFT:
                self.cur_pressed_keys["left"] = False
                self.cur_frame = 0
            if event.key == pygame.K_RIGHT:
                self.cur_pressed_keys["right"] = False
                self.cur_frame = 0
    
    def usePowerup(self):
        powerup_length = 7
        counter = 0 
        while powerup_length > counter:
            character_powerup_damage = self.getPowerupInfo(self.champion, 1)
            if "kick" in self.getPowerupInfo(self.champion, 0): 
                self.setAttackVal(self.champion, True, character_powerup_damage)
            else: 
                self.setAttackVal(self.champion, False, character_powerup_damage)
            counter+=1

        if "kick" in self.getPowerupInfo(self.champion, 0):
            self.resetAttackVal(self.champion,True, character_powerup_damage); 
        else:
            self.resetAttackVal(self.champion, False, character_powerup_damage);  

