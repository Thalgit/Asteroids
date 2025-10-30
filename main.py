#import alle dingen
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shots import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
   
    clock = pygame.time.Clock()
    dt = 0
   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups maken

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    #containers ook

    AsteroidField.containers = (updatable,)

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable, drawable)

    Shot.containers = (updatable, drawable, shots)

    #player maken

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #veld maken

    field = AsteroidField()

    #raam sluit = stop en loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
    #60 fps

        dt = clock.tick(60) / 1000

        updatable.update(dt)

    #niet crashen

        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit("Game over!")

    #asteroids kapot schieten

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    break
                
    #graphics

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()      
        
if __name__ == "__main__":
    main()
