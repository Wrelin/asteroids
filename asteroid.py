import pygame
import circleshape
import random
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        b_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        angle = random.uniform(20, 50)
        a_asteroid.velocity = self.velocity.rotate(angle)
        b_asteroid.velocity = self.velocity.rotate(-angle)
