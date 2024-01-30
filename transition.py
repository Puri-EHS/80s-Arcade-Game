import pygame

class transition():
    def __init__(self):
        self.fading = None
        self.alpha = 0
        self.fade_effect = pygame.Surface(pygame.display.get_surface().get_rect().size)
        self.fade_effect.fill((0, 0, 0))

    def reset(self):
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0

    def draw(self, screen):
        if self.fading:
            self.fade_effect.set_alpha(self.alpha)
            screen.blit(self.fade_effect, (0, 0))

    def update(self):
        if self.fading == 'OUT':
            self.alpha += 8
            if self.alpha >= 255:
                self.fading = 'IN'
                return True
        else:
            self.alpha -= 8
            if self.alpha <= 0:
                self.fading = None
