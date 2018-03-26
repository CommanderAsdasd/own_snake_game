import pygame
from math import pi
from pygame.locals import *

#Globals
SCREENRECT     = Rect(0, 0, 640, 480)

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

class Snake():
    def __init__(self):
        self.size = 5
        self.speed = 10

    def move(self):
        pass

    

def main():
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None
    # img = load_image('player1.gif')
    # Player.images = [img, pygame.transform.flip(img, 1, 0)]
    # img = load_image('explosion1.gif')
    # Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    # Alien.images = load_images('alien1.gif', 'alien2.gif', 'alien3.gif')
    # Bomb.images = [load_image('bomb.gif')]
    # Shot.images = [load_image('shot.gif')]

    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)


    all = pygame.sprite.RenderUpdates()
    BLACK = (0,   0,   0)
    background_colour = (255,255,255)
    # (width, height) = (300, 200)

    # screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snakemosh')
    screen.fill(background_colour)
    pygame.draw.arc(screen, BLACK,[0, 75, 150, 125], 0, pi/2, 2)

    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
if __name__=='__main__':
    main()