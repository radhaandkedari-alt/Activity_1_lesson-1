import pygame 
import random

pygame.init()
SPRTIE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGORUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
GREEN = pygame.Color('green')
RED = pygame.Color('red')
Dark_GREEN = pygame.Color('darkgreen')

#sprite color
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        # Change color randomly
        self.rect.move_ip(self.velocity)