import pygame
import os
from StartScreen import StartScreen
from ChampionSelectScreen import ChampionSelectScreen
from MapSelectScreen import MapSelectScreen
from playerone import player1
from playertwo import player2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

class screenState():
    
    def __init__(self, game_screen) -> None:
        self.game_screen = game_screen
        self.current_screen = 0
        self.map_selected = None
        self.map_image = None
        self.rect = pygame.Rect(100, 150, 120, 100)
        self.screens = []
        self.num_char_selected = 0
        self.chars_selected = []
        self.players = pygame.sprite.Group()
        self.is_zoomed_in = True
        self.startScreen = StartScreen(self.game_screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.champSelectScreen = ChampionSelectScreen(self.game_screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.mapSelectScreen = MapSelectScreen(self.game_screen, SCREEN_WIDTH, SCREEN_HEIGHT)


    def update_screen(self, events):
        if self.current_screen == 0:
            if self.startScreen.update(events):
                self.current_screen += 1
        elif self.current_screen == 1:
            self.chars_selected = self.champSelectScreen.update(events)
            if self.chars_selected != None:
                for x in self.chars_selected:
                    self.players.add(x)
                self.current_screen += 1
        elif self.current_screen == 2:
            self.map_selected = self.mapSelectScreen.update(events)
            if self.map_selected != None:
                self.map_image = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_selected)), (1200, SCREEN_HEIGHT))
                self.current_screen += 1
        elif self.current_screen == 3:
            self.fight_screen(events)

    def fight_screen(self, events):
        # image, (xcoordtobeplaced, ycoordtobeplaced), xcoordtostartcutting, ycoordtostartcutting, lenofimage, heightofimage
        
        self.move_fight_border()
        self.player_out_of_bounds()
        self.players.update(events)
        self.players.draw(self.game_screen)
        for event in events:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_p: 
                    pygame.draw.rect(self.game_screen, (0, 0, 0), (30, 15, 200, 50), 5)
                    self.update_powerup(1)

                    pygame.draw.rect(self.game_screen, (0, 0, 0), (570, 15, 200, 50), 5)
                    self.update_powerup(2)

        
        # health bar
        pygame.draw.rect(self.game_screen, (0, 0, 0), (30, 20, 200, 50), 5)
        self.update_player_health(20, 1)

        pygame.draw.rect(self.game_screen, (0, 0, 0), (570, 20, 200, 50), 5)
        self.update_player_health(80, 2)

    def move_fight_border(self):
        # map_image = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[self.map_selected])), SCREEN_SIZE)
        # self.game_screen.blit(map_image, self.select_screen_background.get_rect())
        player_list = self.players.sprites()
        left_border = (player_list[0].rect.x+player_list[1].rect.x)/2

        if left_border < 0:
            left_border = 0
        elif left_border > 390:
            left_border = 390
        if self.is_zoomed_in:
            self.game_screen.blit(self.map_image, (0, 0), (left_border, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        else: 
            self.game_screen.blit(self.map_image, (0, 0), (200, 0, SCREEN_WIDTH, SCREEN_HEIGHT))


    def player_out_of_bounds(self):
        player1_x = self.players.sprites()[0].rect.x
        player2_x = self.players.sprites()[0].rect.x

        if player1_x < 0:
            icon = pygame.image.load(os.path.join('Other_images', 'player1_left_outofbounds.png'))
            self.game_screen.blit(icon, pygame.Rect(20, 250, 20, 20))

        elif player1_x > SCREEN_WIDTH:
            icon = pygame.image.load(os.path.join('Other_images', 'player1_right_outofbounds.png'))
            self.game_screen.blit(icon, pygame.Rect(720, 250, 20, 20))

        if player2_x < 0:
            icon = pygame.image.load(os.path.join('Other_images', 'player2_left_outofbounds.png'))
            self.game_screen.blit(icon, pygame.Rect(20, 250, 20, 20))

        elif player2_x > SCREEN_WIDTH:
            icon = pygame.image.load(os.path.join('Other_images', 'player2_right_outofbounds.png'))
            self.game_screen.blit(icon, pygame.Rect(720, 250, 20, 20))
            


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

    def update_powerup(self, player_number):
        powerup_color = (0,0,255)
        text_timer = 3.0
        while text_timer > 0.0:
            font = pygame.font.Font(None, 26)
            if player_number == 1:
                text = font.render("Player 1 Uses " + player1.getPowerupInfo(player1.champion, 0), True, (0,0,0))  
            else: 
                text = font.render("Player 2 Uses " + player2.getPowerupInfo(player2.champion, 0), True, (0,0,0))  
            self.game_screen.blit(text, (400,300)) 
            text_timer -= 1.0

        time = 25 
        while time > 0:
            if player_number == 1: 
                pygame.draw.rect(self.game_screen, powerup_color, (45, 35, 20 ,50))
            else: 
                pygame.draw.rect(self.game_screen, powerup_color, (SCREEN_WIDTH-45, 20, 35, 50))
