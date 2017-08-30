try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame, sys
## Statement that allows users to acess pygame specific commands
from pygame.locals import *

pygame.init()

#Set the fps refresh variables
FPS = 30
clock = pygame.time.Clock()

#Set up the application box
size = (480, 320)
screen = pygame.display.set_mode(size)

RED = (255, 0, 0)  
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## Create rectangles that will detect direction
up_rect = pygame.Rect(300, 100, 50, 50)



def main():

    #Play the sound once when loading the program
    pygame.mixer.music.load("Ench.wav")
    pygame.mixer.music.play()

    musicTime = "no"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Android back key.
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_AC_BACK:
                break
            mouse_pos = pygame.mouse.get_pos()
            ## Check if the mouse_pos is within the rectangle
            if up_rect.collidepoint(mouse_pos):
                musicTime = "yes"


        screen.fill(BLACK)                
        ## draw the rectangles that will detect direction
        pygame.draw.rect(screen, GREEN, up_rect)

        if musicTime == "no":
            pass
        elif musicTime == "yes":
            pygame.mixer.music.load("Ench.wav")
            pygame.mixer.music.play()
            musicTime = "no"

        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
