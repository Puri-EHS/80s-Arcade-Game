import pygame
import sys
import os

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
current_screen = 0
button_pos = [0, 0]

background_image1 = pygame.image.load("testimage.jpg")
background_image1 = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)


# Button data for Screen 2
buttons_screen2 = ["Green", "Yellow", "Blue", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

def start_screen():
    start_text = font.render("PRESS SPACE TO START", 1, (0, 0, 0))
    start_text_pos = start_text.get_rect()
    start_text_pos.center = background_image1.get_rect().center
    start_text_pos.y += 200
    screen.blit(background_image1, background_image1.get_rect())
    screen.blit(start_text, start_text_pos)

def champ_select_screen(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                button_pos[1] += 1
            elif event.key == pygame.K_UP:
                button_pos[1] -= 1
            elif event.key == pygame.K_RIGHT:
                button_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                button_pos[0] -= 1
        if button_pos[0] < 0:
            button_pos[0] = 3
        else:
            button_pos[0] = abs(button_pos[0])%4
        button_pos[1] = button_pos[1]%3
    draw_champ_boxes()

def draw_champ_boxes():
    screen.fill(BLACK)
    x = 100
    y = 150
    for i in range(3):
        for j in range(4):
            rect = pygame.Rect(x, y, 120, 100)
            if i == button_pos[1] and j == button_pos[0]:
                pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 255, 0), rect, 3)
            text_surface = font.render(buttons_screen2[(i*4) + j], True, (0, 255, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(pygame.image.load(f"IMG_878{i + 1}.gif"), rect)
            screen.blit(text_surface, text_rect)
            x += 150
        x = 100
        y += 150

# Main loop
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if current_screen == 0 and event.key == pygame.K_RETURN:
                current_screen = 1
            elif current_screen == 1:
                if event.key == pygame.K_RETURN:
                    # Add code to perform actions when a button is selected
                    print(f"Button '{buttons_screen2[button_pos[0] + button_pos[1]*4]}' selected.")

    if current_screen == 0:
        start_screen()
    elif current_screen == 1:
        champ_select_screen(events)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()