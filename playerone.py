import pygame
from playerState import playerState

class player1(playerState):

    def __init__(self, champion: str, isPlayer2=False):
        super().__init__(champion, isPlayer2)

    def update(self, key):
        if self.isAttacking == False:
            self.update_action(key)
            self.update_continuous(key)
        return super().update()

    def update_action(self, key):
        if key == pygame.K_PERIOD:
            self.cur_type_animation = "punch"
            self.isAttacking = True
        if key == pygame.K_SLASH:
            self.cur_type_animation = "kick"
            self.isAttacking = True
        if key == pygame.K_RSHIFT:
            self.cur_pressed_keys["powerup"] = True
            self.isAttacking = True      

    def update_continuous(self, key):
        if(key.type == pygame.KEYDOWN):
            if key == pygame.K_LEFT or key == pygame.K_RIGHT:
                if key == pygame.K_RIGHT:
                    self.cur_pressed_keys["right"] = True
                if key == pygame.K_LEFT:
                    self.cur_pressed_keys["left"] = True
                self.cur_type_animation = "walk"
                self.cur_animation = 0
        if(key.type == pygame.KEYUP):
            self.frame = 0
            if key == pygame.K_LEFT:
                self.cur_pressed_keys["left"] = False
            if key == pygame.K_RIGHT:
                self.cur_pressed_keys["right"] = False