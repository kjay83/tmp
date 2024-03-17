import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


#initialize game
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
player = Player()

running = True
while(running):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    screen.fill((0,0,0))
    # print(player.rect)
    screen.blit(player.surf,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    # screen.blit(player.surf,player.rect)
    pygame.display.flip()

pygame.quit