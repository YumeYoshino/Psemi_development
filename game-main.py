import pygame
from pygame.locals import QUIT, KEYDOWN, K_F1, K_F2, K_ESCAPE
import sys

tmr = 0

def main():
    global tmr

    pygame.init()
    pygame.display.set_caption("インシデント対応")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()

    while True:
        tmr += 1
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                if e.key == K_F1:
                    screen = pygame.display.set_mode((800,800), pygame.FULLSCREEN)
                if e.key == K_F2 or e.key == K_ESCAPE:
                    screen = pygame.display.set_mode((800,600))
        pygame.display.update()
        clock.tick(15)

if __name__ == "__main__":
    main()