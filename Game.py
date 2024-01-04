import pygame
from playerState import playerState
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
screen.get_rect()
players = {}
game_screen = screenState(screen)

# Time
frame = 0
time = 0


# Screen flags

font = pygame.font.Font(None, 36)


# Button data for Screen 2
buttons_screen2 = ["Green", "Yellow", "Blue", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

#Initialize the Power_up icon
powerup_image = pygame.image.load(os.path.join('Other_images', "Powerup_icon.png"))
powerup_image = pygame.transform.scale(powerup_image, (93, 93))
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
        if event.type == pygame.K_p: 
            playerState.usePowerup()
            game_screen.blit(powerup_image, (0, 89))
            text_timer = 1.75 
            while text_timer > 0.0:
                font = pygame.font.Font(None, 26)
                text = font.render(playerState.getPowerup(), True, (0,0,0))
                game_screen.blit(text, (400,300)) 
                text_timer = text_timer-1

    #if len(players.keys()) == 0:
        #players["1"] = playerState(game_screen.char_selected[0])
        #players["2"] = playerState(game_screen.char_selected[1])

    game_screen.update_screen(events, players, frame=frame)
 

    frame += 1
    if(frame == 60):
        time += 1
        frame = 0

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
