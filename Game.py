import pygame
from screenState import screenState
import sys
import os
# Initialize Pygame
pygame.init()


class Game(): 
    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    # Initialize the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Street Fighter with a Twist ")
    screen.get_rect()
    game_screen = screenState(screen)

    # Time
    clock = pygame.time.Clock()
    frame = 0
    time = 0


    # Screen flags

    font = pygame.font.Font(None, 36)


    # Button data for Screen 2
    buttons_screen2 = ["Green", "Yellow", "Blue", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    #Initialize the Power_up icon


    # Main loop
    running = True
    char_selected = 0
    while running:
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        game_screen.update_screen(events)
    

        frame += 1
        if(frame == 60):
            time += 1
            frame = 0 

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()
