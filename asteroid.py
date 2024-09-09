import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
        
    def draw(self,screen):
        pygame.draw.circle(screen,
                           ASTEROID_COLOR,
                           self.position,
                           self.radius,
                           2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_new_asteroids =random.uniform(20,50)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
    
        asteroid_1 = Asteroid(self.position.x,self.position.y,new_asteroid_radius)
        asteroid_2 = Asteroid(self.position.x,self.position.y,new_asteroid_radius)
        asteroid_1.velocity = self.velocity.rotate(angle_new_asteroids) * FASTER_BREAKOFF_ASTEROID_SPEED
        asteroid_2.velocity = self.velocity.rotate(-angle_new_asteroids)    