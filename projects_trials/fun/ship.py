import pygame

class Ship():

    def __init__(self, screen, ai_settings):
        '''Initialize ship attributes.'''
        self.screen = screen
        self.image = pygame.image.load('d:/p/projects_trials/alien_invasion/images/ship.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.height

        self.center = float(self.rect.centerx)
        self.level = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        # Show image
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.level -= self.ai_settings.speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.level += self.ai_settings.speed_factor
        
        self.rect.centerx = self.center
        self.rect.centery = self.level
    
    def center_ship(self):
        self.center = self.screen_rect.centerx
