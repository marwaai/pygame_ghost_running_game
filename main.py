# ------------------------------
# 👻 Ghost Chase Game (main.py)
# ------------------------------
# A simple survival game built with Pygame.
# You control a red ghost with arrow keys,
# while another ghost moves randomly on screen.
# Goal: survive as long as possible without colliding!
# ------------------------------

import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Game window setup
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("ball")
clock = pygame.time.Clock()
running = True

# Font setup (for score and Game Over message)
font = pygame.font.SysFont(None, 60)

# ------------------------------
# Player setup
# ------------------------------
x, y = 100, 400          # Initial player position
speed = 5                # Player movement speed

# Load player ghost image
char_image = pygame.image.load("imgbin-red-ghost-ghost-Zgt5TWj00u3pRWBEAC0VQMefL.jpg").convert_alpha()
char_image = pygame.transform.scale(char_image, (50, 50))  
rect = char_image.get_rect()
rect.center = (x, y)

# Score counter
count = 0

# ------------------------------
# Enemy ghost setup
# ------------------------------
char_image2 = pygame.image.load("pacman-logo-red-ghost-from-pac-man-EuiTpYRu_t.jpg").convert_alpha()
char_image2 = pygame.transform.scale(char_image2, (50, 50))  
rect2 = char_image2.get_rect()
rect2.center = (100, 200)

# Initial ghost movement speed
ghost_speed_x = 2
ghost_speed_y = 2

# ------------------------------
# Main game loop
# ------------------------------
while running:
    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keep player inside boundaries
    if rect.left == 10:
        x += 10
    if rect.right == 590:
        x -= 10
    if rect.bottom == 590:
        y -= 10
    if rect.top == 10:
        y += 10

    # Player controls (arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    # Enemy ghost moves automatically
    rect.center = (x, y)
    rect2.center = (rect2.centerx + ghost_speed_x, rect2.centery + ghost_speed_y)

    # Bounce enemy ghost off screen edges
    x2, y2 = rect2.center
    if x2 < 0 or x2 > 600 - rect2.width:
        ghost_speed_x *= -1
    if y2 < 0 or y2 > 600 - rect2.height:
        ghost_speed_y *= -1
        # Randomize direction when bouncing
        ghost_speed_x = random.choice([-3, -2, -1, 1, 3, 5, 7, 8])
        ghost_speed_y = random.choice([-3, -2, -1, 1, 2, 3, 5, 7, 8])

    # Update positions
    rect.center = (x, y)
    rect2.center = (x2, y2)
    count += 1

    # Collision check → Game Over
    if rect2.colliderect(rect):
        text = font.render("Game Over  Score:" + str(count), True, (255, 0, 0))         
        screen.blit(text, (50, 250))
        pygame.display.update()
        pygame.time.delay(1000)
        count = 0
        continue

    # --- Drawing section ---
    screen.fill((0, 0, 0))             # Background black
    screen.blit(char_image, rect)      # Draw player ghost
    screen.blit(char_image2, rect2)    # Draw enemy ghost

    # Refresh display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
