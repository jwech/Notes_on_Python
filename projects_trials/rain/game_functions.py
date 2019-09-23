import pygame
import sys
from rain import Rain

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(rain_settings, screen, rains):
    screen.fill(rain_settings.bg_color)
    rains.draw(screen)
    pygame.display.flip()

def create_rain(rain_settings, screen, number_x, number_y, rains):
    rain = Rain(rain_settings, screen)
    rain.x = rain.rect.width + 2*number_x*rain.rect.width
    rain.rect.x = rain.x
    rain.rect.y = rain.rect.height + 2*number_y*rain.rect.height
    rains.add(rain)    

def get_numbers_x(rain_settings, rain):
    available_space_x = rain_settings.screen_width - 2*rain.rect.width
    rain_numbers_x = int(available_space_x / (2*rain.rect.width))
    return rain_numbers_x

def get_numbers_y(rain_settings, rain):
    available_space_y = rain_settings.screen_height - 2*rain.rect.height
    rain_numbers_y = int(available_space_y / (2*rain.rect.height))
    return rain_numbers_y

def create_fleet(rain_settings, screen, rains):
    rain = Rain(rain_settings, screen)
    rain_numbers_x = get_numbers_x(rain_settings, rain)
    rain_numbers_y = get_numbers_y(rain_settings, rain)
    for number_y in range(rain_numbers_y):
        for number_x in range(rain_numbers_x):
            create_rain(rain_settings, screen, number_x, number_y, rains)

def check_fleet_edges(rain_settings, rains):
    for rain in rains.sprites():
        if rain.check_edges():
            change_fleet_direction(rain_settings, rains)
            break

def change_fleet_direction(rain_settings, rains):
    for rain in rains.sprites():
        rain.rect.y += rain_settings.fleet_drop_factor
    rain_settings.fleet_direction *= -1

def clean_fleet(rains):
    for rain in rains.sprites():
        if rain.check_bottom():
            rain.rect.y = 0

def update_rains(rain_settings, rains):
    check_fleet_edges(rain_settings, rains)
    clean_fleet(rains)
    rains.update()