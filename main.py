import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        p.update(dt)
        p.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60.0) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
