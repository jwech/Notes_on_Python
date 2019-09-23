import pygame
from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self, rain_settings, screen):
        super().__init__()
        self.screen = screen
        self.rain_settings = rain_settings
        self.image = pygame.image.load('d:/p/projects_trials/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.height:
            return True
    
    def update(self):
        self.x += (self.rain_settings.fleet_speed_factor * 
                  self.rain_settings.fleet_direction)
        self.rect.x = self.x
