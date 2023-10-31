import pygame
pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame UI with Background")

##colors
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

background_image1 = pygame.image.load("testimage.jpg")
background_image1 = pygame.transform.scale(background_image1, (screen_width, screen_height))
background_image2 = pygame.image.load("characterscreen.jpg")
background_image2 = pygame.transform.scale(background_image2, (screen_width, screen_height))

def draw_button(x, y, width, height, color, text, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = font.render(text, True, text_color)
    button_text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(button_text, button_text_rect)
    return pygame.Rect(x, y, width, height)

def main():
    current_background = background_image1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                button1_rect = draw_button(300, 500, 200, 50, black, "Start", white)
                button2_rect = draw_button(575, 500, 200, 50, black, "Button 2", white)
                if button1_rect.collidepoint(mouse_pos):
                    current_background = background_image2
                elif button2_rect.collidepoint(mouse_pos):
                    current_background = background_image2


        screen.blit(current_background, (0, 0))
        draw_button(300, 500, 200, 50, black, "Start", white)
        draw_button(575, 500, 200, 50, black, "Button 2", white)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()