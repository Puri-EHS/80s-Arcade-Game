import pygame
#https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/#a-simple-sprite-sheet
class spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)
    def get_image(self, rectangle, color):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        if color is not None:
            if color is not -1:
                color = image.get_at((0,0))
                image.set_colorkey(color, pygame.RLEACCEL)
        return image
    def get_multiple_images(self, rects, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey) 

        