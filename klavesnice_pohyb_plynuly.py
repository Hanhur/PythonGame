import pygame
# https://iconarchive.com/
# Inicializace pygame
pygame.init()

# Vytvoreni obrazovky
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Zakladni nastaveni
distance = 10
fps = 60
clock = pygame.time.Clock()

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

    # w - nahoru, s - dolů, a - vlevo, d - vpravo
    # Vypis vsech klaves
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and potter_image_rect.top > 0:
        potter_image_rect.y -= distance
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and potter_image_rect.bottom < height:
        potter_image_rect.y += distance
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and potter_image_rect.left > 0:
        potter_image_rect.x -= distance
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and potter_image_rect.right < width:
        potter_image_rect.x += distance

    # Vyplneni obrazovky cernou barnou
    screen.fill((0, 0, 0,))

    # Text
    screen.blit(custom_text, custom_text_rect)

    # Obrázky
    screen.blit(potter_image, potter_image_rect)

    # Update
    pygame.display.update()

    # tikání hodin
    clock.tick(fps)

# Ukonceni pygame
pygame.quit()
# 6