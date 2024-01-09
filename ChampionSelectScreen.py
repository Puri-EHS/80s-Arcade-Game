import pygame
import os

class ChampionSelectScreen():

    def __init__(self, game_screen, screen_width, screen_height) -> None:
        self.screen = game_screen
        self.font = pygame.font.Font(None, 36)
        self.char_buttons = ["Balrog", "Blanka", "Chun Li", "Dhalsim", "E Honda", "Guile", "Ken", "M Bison", "Ryu", "Sagat", "Vega", "Zangief"]
        self.background = pygame.image.load(os.path.join('Backgrounds', "Character Select Background.jpg"))
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        self.rect = pygame.Rect(100, 150, 120, 100)
        self.button_pos = [0,0]
        self.char_selected = []

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.select_controls(event.key):
                    self.char_selected.append(self.char_buttons[self.button_pos[0] + self.button_pos[1]*4])
        self.draw_select_boxes(True)
        if len(self.char_selected) == 2:
            return self.char_selected
        return None
    
    def draw_select_boxes(self, char: bool):
        self.screen.blit(self.background, self.background.get_rect())
        x = 125
        y = 150
        for i in range(3):
            for j in range(4):
                self.rect.x = x
                self.rect.y = y
                if i == self.button_pos[1] and j == self.button_pos[0]:
                    pygame.draw.rect(self.screen, (0, 0, 255), self.rect)
                pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 3)
                text_surface = self.font.render(self.char_buttons[(i*4) + j], True, (0, 255, 0))
                img = pygame.image.load(os.path.join('char_select_img', f'{self.char_buttons[i*4 + j]}' + '.gif')).convert_alpha()
                img.set_colorkey((255,255,255))
                if img.get_rect().x > 120:
                    img = pygame.transform.scale(img, (120,100))
                self.screen.blit(img, self.rect)
                text_rect = text_surface.get_rect(center=self.rect.center)
                self.screen.blit(text_surface, text_rect)
                x += 150
            x = 125
            y += 150

    
    def select_controls(self, key):
        if key == pygame.K_DOWN:
            self.button_pos[1] += 1
        elif key == pygame.K_UP:
            self.button_pos[1] -= 1
        elif key == pygame.K_RIGHT:
            self.button_pos[0] += 1
        elif key == pygame.K_LEFT:
            self.button_pos[0] -= 1

        if key == pygame.K_RETURN:
            return True

        if self.button_pos[0] < 0:
            self.button_pos[0] = 3
        else:
            self.button_pos[0] = abs(self.button_pos[0])%4
        self.button_pos[1] = self.button_pos[1]%3
        return False
    
    #def draw_selected_char(self):
        #player1_text = self.font.render("Player 1:", 1, (0, 0, 0))
        #text_rect = self.rect
        #text_rect.x = 125
        #text_rect.y = 10
        #self.game_screen.blit(player1_text, text_rect)
        #player2_text = self.font.render("Player 2:", 1, (0, 0, 0))
        #text_rect.x = 500
        #text_rect.y = 10
        #self.game_screen.blit(player2_text, text_rect)
        #for x in self.char_selected:
            #self.game_screen.blit(pygame.image.load(os.path.join('char_select_img', f'{x}''.gif')), text_rect)
            #text_rect.x -= 375