from playerState import playerState
import pygame

class player1(playerState):

    def __init__(self, champion: str, isPlayer2=False):
        super().__init__(champion, isPlayer2)
    
    def update(self, events):
        for event in events:
            if((event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP)) and self.isAttacking == False:
                self.update_action(event)
                self.update_continuous(event)
                if (event.key == pygame.K_p): 
                    self.usePowerup(event)
        return super().update()

    def update_action(self, event):
        if event.key == pygame.K_w:
            self.cur_type_animation = "jump"
            self.jump = True
            self.isBlocking = False    
        if event.key == pygame.K_f:
            self.cur_type_animation = "punch"
            self.isAttacking = True
        if event.key == pygame.K_g:
            self.cur_type_animation = "kick"
            self.isAttacking = True
        if event.key == pygame.K_h:
            self.cur_pressed_keys["powerup"] = True
            self.isAttacking = True      

    def update_continuous(self, event):
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_a or event.key == pygame.K_d:
                if event.key == pygame.K_d:
                    self.cur_pressed_keys["right"] = True
                    self.isBlocking = False
                if event.key == pygame.K_a:
                    self.cur_pressed_keys["left"] = True
                    self.isBlocking = False
                self.cur_type_animation = "walk"
                self.cur_animation = 0
            if event.key == pygame.K_s:
                self.cur_pressed_keys["down"] = True
            self.cur_type_animation = "crouch"
            self.cur_animation = 0
        
        if(event.type == pygame.KEYUP):
            self.frame = 0
            if event.key == pygame.K_a:
                self.cur_pressed_keys["left"] = False
                self.isBlocking = True
            if event.key == pygame.K_d:
                self.cur_pressed_keys["right"] = False
                self.isBlocking = True
            if event.key == pygame.K_s:
                self.cur_pressed_keys["down"] = False
    
    def usePowerup(self, event):
        if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_p: 
                    powerup_length = 25 
                    counter = 0 
                    while powerup_length >= counter:
                        character_powerup_damage = player1.getPowerupInfo(self.champion, 1)
                        if "kick" in player1.getPowerupInfo(self.champion, 0): 
                            set_attack = player1.setAttackVal(self.champion, True, character_powerup_damage)
                        else: 
                            set_attack = player1.setAttackVal(self.champion, False, character_powerup_damage)
                        counter+=1
