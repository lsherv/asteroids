import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():

    pygame.init()
    print(f'''
    Starting asteroids!
    Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    asteroidfield = AsteroidField()
    
    dt = 0 

    while pygame.display.get_init():
        #gameloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if player.collision_detect(obj):
                print('Game Over!')
                sys.exit()

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)        

        #player.update(dt)
        #player.draw(screen)
        
        pygame.display.flip()
        #60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
