import pygame
import os


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class GameOverScreen():

    def __init__(self, game_screen, screen_width, screen_height) -> None:
        self.screen = game_screen
        self.background = pygame.image.load(os.path.join('Backgrounds', "game_over_screen.jpeg"))
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        self.font = pygame.font.Font(None, 36)

    def update(self, events, winner):
        text = self.font.render(f"PLAYER {winner} WINS", 1, WHITE)
        restart_text = self.font.render("PRESS R TO RESTART", 1, WHITE)
        text_pos = text.get_rect()
        text_pos.center = self.background.get_rect().center
        restart_text_pos = text_pos
        restart_text_pos.y += 40
        text_pos.y += 20
        self.screen.blit(self.background, (0,0))
        self.screen.blit(text, text_pos)
        self.screen.blit(restart_text, restart_text_pos)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
        return False