import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, stats, aliens, ship, bullets):
    '''Respond to key down'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, aliens, bullets, ship)

def check_keyup_events(event,ship):
    '''Respond to key up'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, aliens, ship, bullets, stats, play_button):
    '''Respond to keyboard and mouse'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button_clicked(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, aliens, ship, bullets)            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_button_clicked(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dymatic_settings()
        start_game(ai_settings,screen, stats, aliens, bullets, ship)        

def start_game(ai_settings, screen, stats, aliens, bullets, ship):
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()


def update_screen(ai_settings, screen, sb, stats, ship, aliens, bullets, play_button):
    '''Update drawing on screen and switch to new screen'''
    # Redraw screen every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    if stats.game_active:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
    # Visualize recent drawn screen
    if not stats.game_active:
        play_button.draw_button()
        pygame.mouse.set_visible(True)
    sb.show_score()
    pygame.display.flip()

def update_bullets(ai_settings, sb, stats, screen, ship, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # Check collsions
    # True means to delete the collided item
    check_bullet_alien_collisions(ai_settings, sb, stats, screen, ship, bullets, aliens)

def check_bullet_alien_collisions(ai_settings, sb, stats, screen, ship, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True) 
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)

def check_aliens_bottom(ai_settings, stats, screen, ship, bullets, aliens):
    for alien in aliens.sprites():
        if alien.rect.bottom >= ai_settings.screen_height:
            ship_hit(ai_settings, stats, screen, ship, bullets, aliens)
            break

def ship_hit(ai_settings, stats, screen, ship, bullets, aliens):
    '''React to ship hit'''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def get_number_aliens_y(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_aliens_y = int(available_space_y / (2*alien_height))
    return number_aliens_y

def create_alien(ai_settings, screen, aliens, alien_number_x, alien_number_y):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2*alien_width * alien_number_x
    alien.y = alien_height + 2*alien_height * alien_number_y
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    '''Create Alien fleet'''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_aliens_y = get_number_aliens_y(ai_settings, alien.rect.height, ship.rect.height)
    
    for alien_number_y in range(number_aliens_y):
        for alien_number_x in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number_x, alien_number_y)

def update_aliens(ai_settings, stats, screen, ship, bullets, aliens):
    check_fleet_edges(ai_settings, aliens)    
    aliens.update()

    # Check aliens and ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, bullets, aliens)
    check_aliens_bottom(ai_settings, stats, screen, ship, bullets, aliens)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
