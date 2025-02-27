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

# Systemove fonty
# fonts = pygame.font.get_fonts()
# for one_font in fonts:
#     print(one_font)

# Nastaveni fontu
system_font = pygame.font.SysFont("kokila", 50)

# Font a text
system_text = system_font.render("Harry Potter", True, white, red)
system_text_rect = system_text.get_rect()
system_text_rect.center = (width // 2, height // 2)

# Hlavni herni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
    # Text
    screen.blit(system_text, system_text_rect)
    # Update
    pygame.display.update()

# Ukonceni pygame
pygame.quit()
# 6