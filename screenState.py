import pygame
import os
from playerState import playerState


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

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
        self.char_buttons = ["Balrog", "Blanka", "Chun Li", "Chalsim", "E Honda", "Guile", "Ken", "M Bison", "Ryu", "Sagat", "Vega", "Zangief"]
        self.num_char_selected = 0
        self.map_testing = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
        self.map_backgrounds = ["Blanka Stage.png", "E Honda Stage (1).png", "Guile Stage.png", "Ken Stage.png", "Ryu Stage (1).png", "Zangief Stage (1).png"]
        self.map_buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        self.current_map = 3
        self.is_map_selected = False
        self.testPlayer = playerState("Bob", 100, True, False)

    def update_screen(self, events, players):
        if self.current_screen == 0:
            self.start_screen()
        elif self.current_screen == 1:
             self.champ_select_screen(events, players)
        elif self.current_screen == 2:
            # self.map_select_screen(events)
            self.map_carousel_select_screen(events)
        elif self.current_screen == 3:
            self.fight_screen(events)

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

    # old map selection screen
    def map_select_screen(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.select_controls(event.key):
                    self.map_selected = self.map_buttons[self.button_pos[0] + self.button_pos[1]*4]
                    self.current_screen += 1
        self.draw_select_boxes(False)

    def map_carousel_select_screen(self, events):
        
        for event in events: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.is_map_selected:
                    self.current_screen += 1
                else: 
                    if event.key == pygame.K_RIGHT:
                        self.current_map += 1
                    if event.key == pygame.K_LEFT:
                        self.current_map -= 1
                    if self.current_map == len(self.map_backgrounds):
                        self.current_map = 0
                    if self.current_map < 0:
                        self.current_map = len(self.map_backgrounds) - 1
                    if event.key == pygame.K_RETURN:
                        self.is_map_selected = True
                        self.map_selected = self.current_map

                
        
        self.draw_map_boxes(self.current_map)

    def fight_screen(self, events):
        map_image = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[self.map_selected])), SCREEN_SIZE)
        self.game_screen.blit(map_image, self.select_screen_background.get_rect())

        for event in events: 
            if event.type == pygame.KEYDOWN:
                self.testPlayer.update(event.key)

        pygame.draw.rect(self.game_screen, (0, 0, 255), pygame.Rect(self.testPlayer.pos.get('x'), self.testPlayer.pos.get('y'), 50, 100))
        
        
        # health bar
        pygame.draw.rect(self.game_screen, (0, 0, 0), (30, 20, 200, 50), 5)
        self.update_player_health(20, 1)

        pygame.draw.rect(self.game_screen, (0, 0, 0), (570, 20, 200, 50), 5)
        self.update_player_health(80, 2)

    def update_player_health(self, health, player_number):
        health_color = None
        if health > 70:
            health_color = (0, 255, 0)
        elif health > 30:
            health_color = (255, 255, 0)
        else:
            health_color = (255, 0, 0)

        if player_number == 1:
            pygame.draw.rect(self.game_screen, health_color , (35, 25, health * 2, 40))
        else: 
            pygame.draw.rect(self.game_screen, health_color , (SCREEN_WIDTH - health * 2 - 35, 25, health * 2, 40))

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
                text_surface = self.font.render(self.char_buttons[(i*4) + j], True, (0, 255, 0))
                img = pygame.image.load(os.path.join('char_select_img', f'{self.char_buttons[i*4 + j]}' + '.gif'))
                if img.get_rect().x > 120:
                    img = pygame.transform.scale(img, (120,100))
                self.game_screen.blit(img, self.rect)
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
    
    def draw_map_boxes(self, cur_map):
        # self.game_screen.fill(BLACK)
        self.game_screen.blit(self.select_screen_background, self.select_screen_background.get_rect())
        

        if(self.is_map_selected):
            self.game_screen.fill((255, 255, 255))

        rect_left = pygame.Rect(50, 250, 120, 80)
        rect_middle = pygame.Rect(250, 200, 300, 200)
        rect_right = pygame.Rect(630, 250, 120, 80)

        rect_left_arrow = pygame.Rect(200, 350, 30, 30)
        rect_right_arrow = pygame.Rect(480, 350, 30, 30)

        ARROW_RECT_SIZE = (30, 30)

        image_left_arrow = pygame.transform.scale(pygame.image.load(os.path.join('Character_Images', 'left_arrow.png')), ARROW_RECT_SIZE)
        pygame.draw.rect(self.game_screen, (0, 0, 0), rect_left_arrow)
        self.game_screen.blit(image_left_arrow, rect_left_arrow)

        image_right_arrow = pygame.transform.scale(pygame.image.load(os.path.join('Character_Images', 'right_arrow.png')), ARROW_RECT_SIZE)
        pygame.draw.rect(self.game_screen, (0, 0, 0), rect_right_arrow)
        self.game_screen.blit(image_right_arrow, rect_right_arrow)

        SMALL_RECT_SIZE = (120, 80)
        LARGE_RECT_SIZE = (300, 200)
        # LARGE_SIZE_TEST = (250, 200, 300, 200)

        if(cur_map - 1 < 0):
            map_left = len(self.map_backgrounds) - 1
        else:
            map_left = cur_map - 1

        if(cur_map + 1 >= len(self.map_backgrounds)):
            map_right = 0
        else:
            map_right = cur_map + 1
        

        image_left = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[map_left])), SMALL_RECT_SIZE)
        pygame.draw.rect(self.game_screen, self.map_testing[map_left], rect_left)
        self.game_screen.blit(image_left, rect_left)

        image_middle = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[cur_map])), LARGE_RECT_SIZE)
        # image_middle = pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[cur_map]))
        pygame.draw.rect(self.game_screen, self.map_testing[cur_map], rect_middle)
        self.game_screen.blit(image_middle, rect_middle)

        image_right = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[map_right])), SMALL_RECT_SIZE)
        pygame.draw.rect(self.game_screen, self.map_testing[map_right], rect_right)
        self.game_screen.blit(image_right, rect_right)

        


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