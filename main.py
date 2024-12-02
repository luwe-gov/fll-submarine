import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Submarine Creature")

# Colors
BLUE = (0, 0, 50)

# Load submarine sprite
submarine_image = pygame.image.load("submarine.png")
submarine_image = pygame.transform.scale(submarine_image, (100, 50))  # Resize

# Submarine position
submarine_x, submarine_y = 375, 300
submarine_speed = 5

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        submarine_x -= submarine_speed
    if keys[pygame.K_RIGHT]:
        submarine_x += submarine_speed
    if keys[pygame.K_UP]:
        submarine_y -= submarine_speed
    if keys[pygame.K_DOWN]:
        submarine_y += submarine_speed

    # Clear screen
    screen.fill(BLUE)

    # Draw submarine
    screen.blit(submarine_image, (submarine_x, submarine_y))

    # Update screen
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
