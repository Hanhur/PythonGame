import pygame

# Inicializace pygame
pygame.init()

# Vytvoreni obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_green = (0, 100, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Barav pozadi
screen.fill(black)

# Tvary
#  Cara
pygame.draw.line(screen, white, (0, 0), (width // 2, height // 2), 1)

# Kruznice
pygame.draw.circle(screen, red, (width // 2, height // 2), 100, 1)

# Kruh
pygame.draw.circle(screen, yellow, (width // 2, height // 2), 90, 0)

# Ctverec, Obdelnik
pygame.draw.rect(screen, blue, (width // 2 - 50, height // 2 - 50, 100, 100))

# Hlavni herni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Update
    pygame.display.update()

# Ukonceni pygame
pygame.quit()
# 6