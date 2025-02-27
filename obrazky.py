import pygame
# https://iconarchive.com/
# Inicializace pygame
pygame.init()

# Vytvoreni obrazovky
width = 1000
height = 500
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

# Obrazky
harry_potter_image = pygame.image.load("img/harryPotter.png")
harry_potter_rect = harry_potter_image.get_rect()
harry_potter_rect.center = (width // 2, height // 2)

coin_image = pygame.image.load("img/Coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (width // 2, height // 2)

# Hlavni herni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Pridat obrazek
    screen.blit(harry_potter_image, harry_potter_rect)
    screen.blit(coin_image, coin_rect)

    # Update
    pygame.display.update()

# Ukonceni pygame
pygame.quit()
# 6