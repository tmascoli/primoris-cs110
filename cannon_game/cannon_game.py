import pygame
import sys
import math
import random
import time

screen = pygame.display.set_mode((700, 400))
clock = pygame.time.Clock()

# Initialize Constants
cannon_base_x = 50
cannon_base_y = 400
cannon_nose_x = 0
cannon_nose_y = 0
hypotenuse = 50
gravity = -9.8

# Initialize Variables
cannon_power = 50
cannon_angle = 45

# Create Enemy
import random
enemy_position_x = random.randint (50, 700)
enemy = pygame.Rect(enemy_position_x, 390, 50, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Decrease Cannon Power
                if cannon_power > 0:
                    cannon_power = cannon_power - 1
                pass
            elif event.key == pygame.K_RIGHT:
                # Increase Cannon Power
                if cannon_power < 100:
                    cannon_power = cannon_power + 1
                pass
            elif event.key == pygame.K_UP:
                # Move Cannon Up
                if cannon_angle < 90:
                    cannon_angle = cannon_angle + 1              
                pass
            elif event.key == pygame.K_DOWN:
                # Move Cannon Down
                if cannon_angle > 0:
                    cannon_angle = cannon_angle - 1                 
                    
                pass
            elif event.key == pygame.K_SPACE:
                print("A Projectile has been launched!")
                cannon_angle_radians = math.radians(cannon_angle)

                opposite = hypotenuse * math.sin(cannon_angle_radians)
                adjacent = hypotenuse * math.cos(cannon_angle_radians)

                cannon_nose_x = cannon_base_x + adjacent
                cannon_nose_y = cannon_base_y - opposite 

                velocity_x = cannon_power * math.cos(cannon_angle_radians)
                velocity_y = cannon_power * math.sin(cannon_angle_radians)

                # Time starts at zero
                t = 0.0

                # Bullet starts at the end of the cannon
                bullet_pos_x = cannon_nose_x
                bullet_pos_y = cannon_nose_y

                while bullet_pos_y <= 400:
                    bullet_dist = velocity_x*t
                    bullet_height = velocity_y*t + 0.5 * gravity * t**2

                    bullet_pos_x = cannon_nose_x + bullet_dist
                    bullet_pos_y = cannon_nose_y - bullet_height

                    pygame.draw.rect(screen, (255, 0, 0),
                                      (bullet_pos_x, bullet_pos_y, 5, 5), 0)

                    pygame.display.flip()
                    t += 0.01

                    time.sleep(0.002)

                # Make an explosion!
                    pygame.draw.circle(screen, (255, 0, 0),
                                    (int(bullet_pos_x), int(bullet_pos_y)),
                                    10, 0)
                pygame.display.flip()

                # Check for a hit
                explosion_rect = pygame.Rect(bullet_pos_x - 15, 395, 30, 10)

                if explosion_rect.colliderect(enemy):
                    print ('Winner!')

                    # We won so generate a new enemy
                    enemy_position_x = random.randint(350, 650)
                    enemy = pygame.Rect(enemy_position_x, 390, 50, 10)

                time.sleep(3)

    # Draw the power meter
    

    # Draw the cannon
    
    cannon_angle_radians = math.radians(cannon_angle)

    opposite = hypotenuse * math.sin(cannon_angle_radians)
    adjacent = hypotenuse * math.cos(cannon_angle_radians)

    pygame.draw.line(screen, (0, 0, 0),
                          (cannon_base_x, cannon_base_y),
                          (cannon_nose_x, cannon_nose_y), 30)
    
    cannon_nose_x = cannon_base_x + adjacent 
    cannon_nose_y = cannon_base_y - opposite 

    pygame.draw.line(screen, (0, 0, 255),
                      (cannon_base_x, cannon_base_y),
                      (cannon_nose_x, cannon_nose_y), 30)

    # Draw the enemy
    pygame.draw.rect(screen, (0, 255, 0), enemy)

    pygame.display.flip()

    clock.tick(20)