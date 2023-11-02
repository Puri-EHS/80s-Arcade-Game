import pygame
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

# Screen flags
current_screen = 1
button_index = 0


# Button data for Screen 2
buttons_screen2 = ["Green", "Yellow", "Blue"]

def draw_screen1():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 48)
    text_surface = font.render("Press Enter to go to Screen 2", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

def draw_screen2():
    screen.fill(BLUE)
    button_height = 200
    y = 150
    for i, text in enumerate(buttons_screen2):
        rect = pygame.Rect(100, y, SCREEN_WIDTH - 200, button_height)
        if i == button_index:
            pygame.draw.rect(screen, (255, 255, 255), rect)
        pygame.draw.rect(screen, (0, 255, 0), rect, 3)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0, 255, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)
        y += button_height + 10

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if current_screen == 1 and event.key == pygame.K_RETURN:
                current_screen = 2
                button_index = 0
            elif current_screen == 2:
                if event.key == pygame.K_DOWN:
                    button_index = (button_index + 1) % len(buttons_screen2)
                elif event.key == pygame.K_UP:
                    button_index = (button_index - 1) % len(buttons_screen2)
                elif event.key == pygame.K_RETURN:
                    # Add code to perform actions when a button is selected
                    print(f"Button '{buttons_screen2[button_index]}' selected.")

    if current_screen == 1:
        draw_screen1()
    elif current_screen == 2:
        draw_screen2()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()