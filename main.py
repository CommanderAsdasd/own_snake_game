import pygame
import pygame.examples.aliens

# print(pygame.examples.aliens)


class Snake():
    def __init__(self):
        slef.size = 5

    def update(self):
        pass

def main():
    background_colour = (255,255,255)
    (width, height) = (300, 200)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial 1')
    screen.fill(background_colour)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
if __name__=='__main__':
    main()