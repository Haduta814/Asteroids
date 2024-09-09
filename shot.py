import pygame

from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        
    def draw(self,screen):
        pygame.draw.circle(screen,
                           SHOT_COLOR,
                           self.position,
                           self.radius,
                           DRAW_WIDTH)
    
    
    def update(self, dt):
        self.position += self.velocity * dt
        