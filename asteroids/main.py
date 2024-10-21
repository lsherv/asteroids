import pygame
from constants import *

def main():

    pygame.init()
    print(f'''
    Starting asteroids!
    Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while pygame.display.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        pygame.display.flip()


if __name__ == "__main__":
    main()
