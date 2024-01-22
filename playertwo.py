from playerState import playerState
import pygame

class player2(playerState):
    pass

    def __init__(self, champion: str, isPlayer2=True):
        super().__init__(champion, isPlayer2)
    
    def update(self, key):
        self.update_action(key)
        self.update_continuous(key)
        return super().update(key)

    def update_action(self, key):
            if key == pygame.K_f:
                 self.cur_type_animation = "punch"
            if key == pygame.K_g:
                 self.cur_type_animation = "kick"
            if key == pygame.K_h:
                self.cur_pressed_keys["powerup"] = True         
    
    def update_continuous(self, key):
        if(key.type == pygame.KEYDOWN):
            if key == pygame.K_a:
                self.cur_pressed_keys["left"] = True
                self.cur_type_animation = "walk"
                self.cur_animation = 0
            if key == pygame.K_d:
                self.cur_pressed_keys["right"] = True
                self.cur_type_animation = "walk"
        if(key.type == pygame.KEYUP):
            self.frame = 0
            if key == pygame.K_a:
                self.cur_pressed_keys["left"] = False
            if key == pygame.K_d:
                self.cur_pressed_keys["right"] = False