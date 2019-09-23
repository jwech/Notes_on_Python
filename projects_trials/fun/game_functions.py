import pygame
import sys
from bullet import Bullet
from aliens import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()

def check_keyup_events(ship, event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_UP:
            ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False

def check_events(ai_settings, screen, stats, play_button,alien, aliens, bullets, ship):
    '''check keyboard and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y, alien, aliens, bullets, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

def check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y, alien, aliens, bullets, ship):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stat()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_aliens_fleet(ai_settings, screen, alien, aliens, ship)
        ship.center_ship()
        pygame.mouse.set_visible(False)

def update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button):
    '''update screen'''
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    screen.fill((ai_settings.bg_color))
    ship.blitme()
    if stats.game_active:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
    aliens.draw(screen)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, ship, alien, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left > ship.screen_rect.right:
            bullets.remove(bullet)
    check_bullets_aliens_collision(ai_settings, screen, alien, aliens, bullets, ship)

def check_bullets_aliens_collision(ai_settings, screen, alien, aliens, bullets, ship):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, False)
    if len(aliens) == 0:
        create_aliens_fleet(ai_settings, screen, alien, aliens, ship)
        bullets.empty()
        ship.center_ship()

def get_numbers_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def get_numbers_y(ai_settings, ship, alien_height):
    available_space_y = ai_settings.screen_height - 3*alien_height - ship.rect.height
    number_aliens_y = int(available_space_y / (2*alien_height))
    return number_aliens_y

def create_alien(ai_settings, screen, aliens, number_alien_x, number_alien_y):
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2*number_alien_x*alien.rect.width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*number_alien_y*alien.rect.height
    aliens.add(alien)

def create_aliens_fleet(ai_settings, screen, alien, aliens, ship):
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = get_numbers_x(ai_settings, alien_width)
    number_aliens_y = get_numbers_y(ai_settings, ship, alien_height)

    for number_alien_y in range(number_aliens_y):
        for number_alien_x in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, number_alien_x, number_alien_y)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    ai_settings.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed_factor

def update_aliens(ai_settings, stats, screen, alien, aliens, bullets, ship):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        hit_ship(ai_settings, stats, screen, alien, aliens, bullets, ship)
    check_aliens_bottom(ai_settings, stats, screen, alien, aliens, bullets, ship)

def hit_ship(ai_settings, stats, screen, alien, aliens, bullets, ship):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_aliens_fleet(ai_settings, screen, alien, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, alien, aliens, bullets, ship):
    for alien in aliens.sprites():
        if alien.rect.bottom >= ai_settings.screen_height:
            hit_ship(ai_settings, stats, screen, alien, aliens, bullets, ship)
            break
