import pygame
from settings import Settings
import game_functions as gf
from rain import Rain
from pygame.sprite import Group

def run_game():
    
    pygame.init()
    rain_settings = Settings()
    screen = pygame.display.set_mode((rain_settings.screen_width,
                                      rain_settings.screen_height))
    pygame.display.set_caption("Rain Drop Game")

    rain = Rain(rain_settings, screen)
    rains = Group()
    gf.create_fleet(rain_settings, screen, rains)

    # Start main loop
    while True:
        # Check keyboard and mouse events
        gf.check_events()

        # Update screen
        gf.update_screen(rain_settings, screen, rains)

        # Update rains
        gf.update_rains(rain_settings, rains)

        
run_game()