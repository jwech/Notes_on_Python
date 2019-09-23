import pygame
import sys
from settings import Settings
import game_functions as g_funcs
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
from aliens import Alien
from game_stats import GameStats
from button import Button


def run_game():
    '''Space ship game'''
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Spaceship Game")
    ship = Ship(screen, ai_settings)
    stats = GameStats(ai_settings)
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings, screen)
    play_button = Button(ai_settings, screen, 'Play')

    g_funcs.create_aliens_fleet(ai_settings, screen, alien, aliens, ship)

    while True:
        # Check keyboar d and mouse events
        g_funcs.check_events(ai_settings, screen, stats, play_button, alien, aliens, bullets, ship)

        if stats.game_active:
            # Update ship's position
            ship.update()
            # Update bullets
            g_funcs.update_bullets(ai_settings, screen, ship, alien, aliens, bullets)
            # Update aliens
            g_funcs.update_aliens(ai_settings, stats, screen, alien, aliens, bullets, ship)
        # Update screen
        g_funcs.update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button)
        
        
run_game()

