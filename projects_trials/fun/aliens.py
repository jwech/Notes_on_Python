from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('d:/p/projects_trials/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.x = float(self.rect.x)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        self.x += (self.ai_settings.fleet_speed_factor * 
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

