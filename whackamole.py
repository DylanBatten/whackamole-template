import pygame
import random

def draw_grid(screen):
    for i in range(1, 16):
        pygame.draw.line(screen, (0,0,0), (0, i*32), (640,i*32))

    for i in range(1, 20):
        pygame.draw.line(screen, (0,0,0), (i*32, 0), (i*32, 512))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    a, b = event.pos
                    a //= 32
                    b //= 32
                    if (a, b) == (x,y):
                        x = random.randrange(0,20)
                        y = random.randrange(0,16)
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft = (x*32, y*32)))
            pygame.display.flip()
            clock.tick(60)
            pygame.display.update()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
