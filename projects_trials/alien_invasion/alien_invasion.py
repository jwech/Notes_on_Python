import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as g_funcs
from pygame.sprite import Group

def run_game():
    '''Initialize game and create a screen object'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
                (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create fleet
    g_funcs.create_fleet(ai_settings, screen, aliens, ship)

    # Start main loop
    while True:
        # monitor keyboard and mouse event
        g_funcs.check_events(ai_settings, screen, ship, bullets)

        # Move ship  
        ship.update()

        # Update screen
        g_funcs.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Update bullets
        g_funcs.update_bullets(bullets)

        # Update Aliens
        g_funcs.update_aliens(ai_settings, aliens)

run_game()
         