import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as g_funcs
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

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

    play_button = Button(ai_settings, screen, 'Play')

    # Create fleet
    g_funcs.create_fleet(ai_settings, screen, aliens, ship)

    # Create game stats
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # Start main loop
    while True:
        # monitor keyboard and mouse event
        g_funcs.check_events(ai_settings, screen, aliens, ship, bullets, stats, play_button)

        if stats.game_active:
            # Move ship  
            ship.update()  
            # Update bullets
            g_funcs.update_bullets(ai_settings, sb, stats, screen, ship, bullets, aliens)
            # Update Aliens
            g_funcs.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)

         # Update screen
        g_funcs.update_screen(ai_settings, screen, sb, stats, ship, aliens, bullets, play_button)

run_game()
         