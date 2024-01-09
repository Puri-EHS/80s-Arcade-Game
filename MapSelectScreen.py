import pygame
import os

class MapSelectScreen():

    def __init__(self, game_screen, screen_width, screen_height) -> None:
        self.screen = game_screen
        self.map_backgrounds = ["Blanka Stage.png", "E Honda Stage (1).png", "Guile Stage.png", "Ken Stage.png", "Ryu Stage (1).png", "Zangief Stage (1).png"]
        self.background = pygame.image.load(os.path.join('Backgrounds', "Character Select Background.jpg"))
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        self.map_testing = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
        self.map_selected = 3

    def update(self, events):
        for event in events: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return self.map_backgrounds[self.map_selected]
                if event.key == pygame.K_RIGHT:
                    self.map_selected += 1
                if event.key == pygame.K_LEFT:
                    self.map_selected -= 1

                if self.map_selected == len(self.map_backgrounds):
                    self.map_selected = 0
                if self.map_selected < 0:
                    self.map_selected = len(self.map_backgrounds) - 1

        self.draw_map_boxes(self.map_selected)
        return None
    
    def draw_map_boxes(self, cur_map):
        # self.game_screen.fill(BLACK)
        self.screen.blit(self.background, self.background.get_rect())

        rect_left = pygame.Rect(50, 250, 120, 80)
        rect_middle = pygame.Rect(250, 200, 300, 200)
        rect_right = pygame.Rect(630, 250, 120, 80)

        rect_left_arrow = pygame.Rect(200, 350, 30, 30)
        rect_right_arrow = pygame.Rect(480, 350, 30, 30)

        ARROW_RECT_SIZE = (30, 30)

        image_left_arrow = pygame.transform.scale(pygame.image.load(os.path.join('Character_Images', 'left_arrow.png')), ARROW_RECT_SIZE)
        pygame.draw.rect(self.screen, (0, 0, 0), rect_left_arrow)
        self.screen.blit(image_left_arrow, rect_left_arrow)

        image_right_arrow = pygame.transform.scale(pygame.image.load(os.path.join('Character_Images', 'right_arrow.png')), ARROW_RECT_SIZE)
        pygame.draw.rect(self.screen, (0, 0, 0), rect_right_arrow)
        self.screen.blit(image_right_arrow, rect_right_arrow)

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
        pygame.draw.rect(self.screen, self.map_testing[map_left], rect_left)
        self.screen.blit(image_left, rect_left)

        image_middle = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[cur_map])), LARGE_RECT_SIZE)
        # image_middle = pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[cur_map]))
        pygame.draw.rect(self.screen, self.map_testing[cur_map], rect_middle)
        self.screen.blit(image_middle, rect_middle)

        image_right = pygame.transform.scale(pygame.image.load(os.path.join('Backgrounds', self.map_backgrounds[map_right])), SMALL_RECT_SIZE)
        pygame.draw.rect(self.screen, self.map_testing[map_right], rect_right)
        self.screen.blit(image_right, rect_right)