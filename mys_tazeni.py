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
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Barav pozadi
screen.fill(black)

# Nastaveni fontu
custom_font = pygame.font.Font("fonts/Harry.ttf", 50)

# Font a text
custom_text = custom_font.render("Harry Potter Game", True, green)
custom_text_rect = custom_text.get_rect()
custom_text_rect.midtop = (width // 2, 5)

# Tvary
pygame.draw.line(screen, green, (0, 60), (width, 60), 2)

# Obrázek
potter_image = pygame.image.load("img/harryPotter.png")
potter_image_rect = potter_image.get_rect()
potter_image_rect.center = (width // 2, height // 2)


# Hlavni herni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            potter_image_rect.centerx = event.pos[0]
            potter_image_rect.centery = event.pos[1]

    # Obnova obrazovky
    screen.fill((black))
    # Text
    screen.blit(custom_text, custom_text_rect)

    # Obrázky
    screen.blit(potter_image, potter_image_rect)

    # Update
    pygame.display.update()

# Ukonceni pygame
pygame.quit()
# 33