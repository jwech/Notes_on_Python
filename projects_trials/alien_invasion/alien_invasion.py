import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as g_funcs

def run_game():
    '''Initialize game and create a screen object'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
                (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # Start main loop
    while True:
        # monitor keyboard and mouse event
        g_funcs.check_events(ship)
        # Move ship
        ship.update()
        # Update screen
        g_funcs.update_screen(ai_settings, screen, ship)

run_game()
        