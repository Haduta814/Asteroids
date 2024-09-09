import pygame


from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0   
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots = pygame.sprite.Group()


    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    Shot.containers= (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(
    x = SCREEN_WIDTH / 2,
    y = SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt) 
        
        for obj in asteroids:
            if obj.detect_collision(player):
                print("Game over!")
                exit()
                
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()
        
        screen.fill((0,0,0))
        
        for obj in drawable: 
            obj.draw(screen)
        pygame.display.flip()
        
        #Limits FPS to FPS constant
        dt = game_clock.tick(FPS_CONSTANT) /1000



if __name__ =="__main__":
    main()

