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
        return super().update()

    def update_action(self, event):
        if event.key == pygame.K_PERIOD:
            self.cur_type_animation = "punch"
            self.isAttacking = True
        if event.key == pygame.K_SLASH:
            self.cur_type_animation = "kick"
            self.isAttacking = True
        if event.key == pygame.K_RSHIFT:
            self.cur_pressed_keys["powerup"] = True
            self.isAttacking = True      

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
            if event.key == pygame.K_RIGHT:
                self.cur_pressed_keys["right"] = False