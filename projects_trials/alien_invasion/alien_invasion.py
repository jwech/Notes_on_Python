import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as g_funcs
from pygame.sprite import Group
from game_stats import GameStats

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

    # Create game stats
    stats = GameStats(ai_settings)

    # Start main loop
    while True:
        # monitor keyboard and mouse event
        g_funcs.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            # Move ship  
            ship.update()  
            # Update bullets
            g_funcs.update_bullets(ai_settings, screen, ship, bullets, aliens)
            # Update Aliens
            g_funcs.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)

         # Update screen
        g_funcs.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
         