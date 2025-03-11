# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_text(screen, font_pose, text='No text', font_size=10, font_name='DejaVuSans.ttf', font_color= (0,0,0), italic=False, bold=False, rotation=0):
    pygame.font.init()
    font = pygame.font.Font(font_name, font_size)
    font.set_italic(italic)
    font.set_bold(bold)
    text_surface = font.render(text, True, font_color)
    if rotation != 0:
        text_surface = pygame.transform.rotate(text_surface, rotation)
    text_rect = text_surface.get_rect(center=(font_pose))
    screen.blit(text_surface, text_rect.topleft)

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    rotation = 0
    while running:
        running = handle_events()
        screen.fill(config.BLACK) # Use color from config

        rotation += 1

        draw_text(screen, [400,400], 'round and round', 50, font_color=config.RED, rotation=rotation)
        draw_text(screen, [401,401], 'round and round', 50, font_color=config.RED, rotation=rotation)
        draw_text(screen, [402,402], 'round and round', 50, rotation=rotation)
        draw_text(screen, [403,403], 'round and round', 50, rotation=rotation)
        draw_text(screen, [404,404], 'round and round', 50, rotation=rotation)

        pygame.display.flip()
        
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()
