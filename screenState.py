import pygame
import os
from playerState import playerState

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

class screenState():
    
    def __init__(self, game_screen) -> None:
        self.game_screen = game_screen
        self.font = pygame.font.Font(None, 36)
        self.start_screen_background = pygame.image.load(os.path.join('Backgrounds', "testimage.jpg"))
        self.start_screen_background = pygame.transform.scale(self.start_screen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.select_screen_background = pygame.image.load(os.path.join('Backgrounds', "Character Select Background.jpg"))
        self.select_screen_background = pygame.transform.scale(self.select_screen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.current_screen = 0
        self.map_selected = None
        self.rect = pygame.Rect(100, 150, 120, 100)
        self.screens = []
        self.button_pos = [0, 0]
        self.char_selected = []
        self.num_char_selected = 0
        self.char_buttons = ["Balrog", "Blanka", "Chun Li", "Chalsim", "E Honda", "Guile", "Ken", "M Bison", "Ryu", "Sagat", "Vega", "Vega"]
        self.map_buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        self.map_selected = BLUE

    def update_screen(self, events, players):
        if self.current_screen == 0:
            self.start_screen()
        elif self.current_screen == 1:
            self.champ_select_screen(events, players)
        elif self.current_screen == 2:
            self.map_select_screen(events)
        elif self.current_screen == 3:
            self.fight_screen()

    def start_screen(self):
        start_text = self.font.render("PRESS SPACE TO START", 1, (0, 0, 0))
        start_text_pos = start_text.get_rect()
        start_text_pos.center = self.start_screen_background.get_rect().center
        start_text_pos.y += 200
        self.game_screen.blit(self.start_screen_background, self.start_screen_background.get_rect())
        self.game_screen.blit(start_text, start_text_pos)

    def champ_select_screen(self, events, players):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.select_controls(event.key):
                    self.char_selected.append(self.button_pos)
                    players[f"{self.num_char_selected}"] = self.char_buttons[self.button_pos[0] + self.button_pos[1]*4]
                    self.num_char_selected += 1
                    if self.num_char_selected == 2:
                        self.current_screen += 1
        self.draw_select_boxes(True)
        return players

    def map_select_screen(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.select_controls(event.key):
                    self.map_selected = self.map_buttons[self.button_pos[0] + self.button_pos[1]*4]
                    self.current_screen += 1
        self.draw_select_boxes(False)

    def fight_screen(self):
        self.game_screen.blit(self.map_selected)

    def draw_select_boxes(self, char: bool):
        self.game_screen.blit(self.select_screen_background, self.select_screen_background.get_rect())
        x = 125
        y = 150
        for i in range(3):
            for j in range(4):
                self.rect.x = x
                self.rect.y = y
                if i == self.button_pos[1] and j == self.button_pos[0]:
                    pygame.draw.rect(self.game_screen, (0, 0, 255), self.rect)
                pygame.draw.rect(self.game_screen, (0, 255, 0), self.rect, 3)
                if char:
                    text_surface = self.font.render(self.char_buttons[(i*4) + j], True, (0, 255, 0))
                    self.game_screen.blit(pygame.image.load(os.path.join('char_select_img', f'{self.char_buttons[i*4 + j]}' + '.gif')), self.rect)
                else:
                    text_surface = self.font.render(self.map_buttons[(i*4) + j], True, (0, 255, 0))
                    self.game_screen.blit(pygame.image.load(os.path.join('char_select_img', f'{self.map_buttons[i*4 + j]}' + '.gif')), self.rect)
                text_rect = text_surface.get_rect(center=self.rect.center)
                self.game_screen.blit(text_surface, text_rect)
                x += 150
            x = 125
            y += 150
        
    def draw_selected_char(self):
        player1_text = self.font.render("Player 1:", 1, (0, 0, 0))
        text_rect = self.rect
        text_rect.x = 125
        text_rect.y = 10
        self.game_screen.blit(player1_text, text_rect)
        player2_text = self.font.render("Player 2:", 1, (0, 0, 0))
        text_rect.x = 500
        text_rect.y = 10
        self.game_screen.blit(player2_text, text_rect)
        for x in self.char_selected:
            self.game_screen.blit(pygame.image.load(os.path.join('char_select_img', f'{x}''.gif')), text_rect)
            text_rect.x -= 375


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