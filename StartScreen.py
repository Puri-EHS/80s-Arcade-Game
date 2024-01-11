import pygame
import os

class StartScreen():

    def __init__(self, game_screen, screen_width, screen_height) -> None:
        self.screen = game_screen
        self.background = pygame.image.load(os.path.join('Backgrounds', "testimage.jpg"))
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("PRESS SPACE TO START", 1, (0, 0, 0))
        self.text_pos = self.text.get_rect()
        self.text_pos.center = self.background.get_rect().center
        self.text_pos.y += 200

    def update(self, events):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.text, self.text_pos)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True