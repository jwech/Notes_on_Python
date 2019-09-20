import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Represent single Alien class'''

    def __init__(self, ai_settings, screen):
        '''Initialize alien'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('./projects_trials/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)