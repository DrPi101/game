import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alfie Noakes' : Big Shooter")
    # Initialize  game and create screen object

    
    # Make an instance of Ship class called ship
    ship = Ship(ai_settings,screen)

    # Make a Group to store bullets in
    bullets = Group()
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        bullets.update()
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()

