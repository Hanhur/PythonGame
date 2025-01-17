import pygame

# Inicializace pygame
pygame.init()

# Vytvoreni obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Hlavni herni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False


# Ukonceni pygame
pygame.quit()
# 6