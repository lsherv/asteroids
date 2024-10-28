import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        super().__init__(x, y, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        current_position = self.position
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        velocity1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        veolicty2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)

        new_radius = old_radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(current_position.x, current_position.y, new_radius)
        new_asteroid1.velocity = velocity1 * 1.2

        new_asteroid2 = Asteroid(current_position.x, current_position.y, new_radius)
        new_asteroid2.velocity = veolicty2 * 1.2
