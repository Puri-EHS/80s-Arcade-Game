import pygame
import os
from StartScreen import StartScreen
from ChampionSelectScreen import ChampionSelectScreen
from MapSelectScreen import MapSelectScreen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

class screenState():
    
    def __init__(self, game_screen) -> None:
        self.game_screen = game_screen
        self.current_screen = 0
        self.map_selected = ""
        self.rect = pygame.Rect(100, 150, 120, 100)
        self.screens = []
        self.num_char_selected = 0
        self.chars_selected = []
        self.players = pygame.sprite.Group()
        self.is_player2 = False
        self.is_zoomed_in = True
        self.startScreen = StartScreen(self.game_screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.champSelectScreen = ChampionSelectScreen(self.game_screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.mapSelectScreen = MapSelectScreen(self.game_screen, SCREEN_WIDTH, SCREEN_HEIGHT)


    def update_screen(self, events, players, frame):
        if self.current_screen == 0:
            if self.startScreen.update(events):
                self.current_screen += 1
        elif self.current_screen == 1:
            self.chars_selected = self.champSelectScreen.update(events)
            if self.chars_selected != None:
                self.current_screen += 1
        elif self.current_screen == 2:
            self.map_selected = self.mapSelectScreen.update(events)
            if self.map_selected != "":
                self.current_screen += 1
        elif self.current_screen == 3:
            self.fight_screen(events, frame)

    def fight_screen(self, events, frame):
        # image, (xcoordtobeplaced, ycoordtobeplaced), xcoordtostartcutting, ycoordtostartcutting, lenofimage, heightofimage
        
        for event in events:
            self.move_fight_border()
            self.players.update(event)
            self.players.draw(self.game_screen)

        
        # health bar
        pygame.draw.rect(self.game_screen, (0, 0, 0), (30, 20, 200, 50), 5)
        self.update_player_health(20, 1)

        pygame.draw.rect(self.game_screen, (0, 0, 0), (570, 20, 200, 50), 5)
        self.update_player_health(80, 2)

    def move_fight_border(self):
        # map_image = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[self.map_selected])), SCREEN_SIZE)
        # self.game_screen.blit(map_image, self.select_screen_background.get_rect())
        
        left_border = (self.players.pos.get('x')+self.players.pos.get('x'))/2

        if left_border < 0:
            left_border = 0
        elif left_border > 390:
            left_border = 390
        if self.is_zoomed_in:
            map_image = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[self.map_selected])), (1200, SCREEN_HEIGHT))
            self.game_screen.blit(map_image, (0, 0), (left_border, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        else: 
            map_image = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[self.map_selected])), (1200, SCREEN_HEIGHT))
            self.game_screen.blit(map_image, (0, 0), (200, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

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
