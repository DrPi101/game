import sys
import pygame
from bullet import Bullet



def check_keydown_events(event, ai_settings, screen, ship, bullets):


            if event.key == pygame.K_SPACE:
               new_bullet = Bullet(ai_settings, screen, ship)
               bullets.add(new_bullet)

                
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

def check_keyup_events(event, ship):

            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
            
def update_screen(ai_settings, screen, ship, bullets):
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
