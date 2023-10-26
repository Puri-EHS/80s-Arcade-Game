import pygame
pygame.init()

# Set up the window and display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame UI with Background")

# Define colors and fonts
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Load background image
background_image = pygame.image.load("testimage.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Function to draw a button
def draw_button(x, y, width, height, color, text, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = font.render(text, True, text_color)
    button_text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(button_text, button_text_rect)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ##draws background image
        screen.blit(background_image, (0, 0))

        # Draw UI elements
        draw_button(300, 500, 200, 50, black, "Start", white)
        #draw_button(100, 200, 200, 50, black, "Button 2", white)

        pygame.display.update()
    pygame.quit()  
if __name__ == "__main__":
    main()