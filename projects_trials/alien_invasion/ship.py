import pygame

class Ship:

    def __init__(self, ai_settings, screen):
        '''Initialize ship and set initial position'''
        self.screen = screen
        self.ai_settings = ai_settings
    
        # load ship image and abtain outside rectangle
        self.image = pygame.image.load('d:/p/projects_trials/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Place every ship at central bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Save floats in ship's center
        self.center = float(self.rect.centerx)

        # Movement marks
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''Move ship based on movement marks'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.ai_settings.ship_speed_factor
        # Update self.rect.centerx
        self.rect.centerx = self.center
    
    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        '''Draw ship at given position'''
        self.screen.blit(self.image, self.rect)