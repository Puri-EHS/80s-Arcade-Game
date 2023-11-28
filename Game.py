import pygame
import playerState
from screenState import screenState
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter with a Twist ")

players = {}
game_screen = screenState(screen)

# Screen flags

font = pygame.font.Font(None, 36)

<<<<<<< HEAD
background_image1 = pygame.image.load("testimage.jpg")
background_image1 = pygame.transform.scale(background_image1, (screen_width, screen_height))
background_image2 = pygame.image.load("Balrog.jpg")
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
                button1_rect = draw_button(300, 500, 200, 50, black, "Back", white)
                button2_rect = draw_button(575, 500, 200, 50, black, "Button 2", white)
                if button1_rect.collidepoint(mouse_pos):
                    return current_background
                elif button2_rect.collidepoint(mouse_pos):
                    current_background = background_image2


        screen.blit(current_background, (0, 0))
        draw_button(25, 500, 200, 50, black, "Back", white)
        draw_button(575, 500, 200, 50, black, "Continue", white)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
=======

# Button data for Screen 2
buttons_screen2 = ["Green", "Yellow", "Blue", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

# Main loop
running = True
char_selected = 0
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_screen.current_screen != 3 and game_screen.current_screen != 1:
                    game_screen.current_screen += 1
            elif game_screen.current_screen == 1:
                if event.key == pygame.K_RETURN:
                    # Add code to perform actions when a button is selected
                    button_selected_text = font.render((f"Button '{buttons_screen2[game_screen.button_pos[0] + game_screen.button_pos[1]*4]}' selected."), True, (0,0,255))
                    screen.blit(button_selected_text, (0, 0))

    game_screen.update_screen(events, players)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
>>>>>>> 0f66d9412fac031aa468a23e1a2a9b3d665bf359
