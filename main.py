import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

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

    AsteroidField.containers = (updatable,)

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable, drawable)

    #player maken

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #veld maken

    field = AsteroidField()

    #raam sluit = stop en loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        updatable.update(dt)

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()      
        
if __name__ == "__main__":
    main()
