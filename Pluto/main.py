import pygame
import pygame_gui
from colors import *
import random

# Initialize Pygame
pygame.init()


# Set up the game window
WIDTH = 1600
HEIGHT = 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pluto: The Quest for Independence")


# Audio
pygame.mixer.music.load("Music\TitleMusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# UI
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

slider = pygame_gui.elements.UIHorizontalSlider(
    pygame.Rect(WIDTH // 2 - 350, 50, 700, 50),
    start_value=0.5,
    value_range=(0, 1)
)

#Text Stuff
title_font = pygame.font.SysFont("Arial", 60)
text_font = pygame.font.SysFont("Arial", 30)

title_text = title_font.render("Pluto: The Quest for Independence", True, WHITE)
instructions_text = text_font.render("Press SPACE to Start", True, WHITE)
instructions_text2 = text_font.render("(Press ESC for Options)", True, WHITE)




title_x = WIDTH / 2 - title_text.get_width() / 2
title_y = HEIGHT // 2 - title_text.get_height() // 2 - 50
instructions_x = WIDTH // 2 - instructions_text.get_width() // 2
instructions_y = HEIGHT // 2 - instructions_text.get_height() // 2 + 50


instructions_texta = text_font.render("Controls:", True, WHITE)
instructions_textb = text_font.render("WASD", True, WHITE)
instructions_textc = text_font.render("Attack: J", True, WHITE)
instructions_textd = text_font.render("Super (Only Available when most needed): K", True, WHITE)

instructions_xa = WIDTH // 2 - instructions_texta.get_width() // 2
instructions_xb = WIDTH // 2 - instructions_textb.get_width() // 2
instructions_xc = WIDTH // 2 - instructions_textc.get_width() // 2
instructions_xd = WIDTH // 2 - instructions_textd.get_width() // 2

x = 0
y = 1

p = 45
q = HEIGHT / 2
move1 = False
move2 = False
move3 = False
move4 = False

    # Health bar
max_health = 100
current_health = max_health
bar_width = 200
bar_height = 20
bar_x = (WIDTH - bar_width) // 4
bar_y = 50

max_health2 = 200
current_health2 = max_health2
bar_width2 = 250
bar_x2 = (WIDTH - bar_width) // 4 * 3
bar_y2 = 50

i = 1700
j = -100

k1 = -900
k2 = -600
k3 = -300
l1 = -100
l2 = -100
l3 = -100

o = 0

m = WIDTH - 100
n = HEIGHT // 2

#Game Loop
while True:

    #Volume Slider
    manager.update(pygame.time.get_ticks() / 1000.0)
    manager.draw_ui(window)

    while y % 2 == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                y += 1
            manager.process_events(event)

        manager.update(pygame.time.get_ticks() / 1000.0)

        window.fill((0, 0, 0))
        manager.draw_ui(window)

        pygame.mixer.music.set_volume(slider.get_current_value())

        # Update the window with the modified variable
        AudPerc = str(int(round(slider.get_current_value(), 2) * 100)) + "%"
        value_text = pygame.font.SysFont("Arial", 30).render(f"Value: {AudPerc}", True, WHITE)
        window.blit(value_text, (WIDTH // 2 - value_text.get_width() // 2, 100))

        window.blit(instructions_texta, (instructions_xa, instructions_y - 150))
        window.blit(instructions_textb, (instructions_xb, instructions_y - 100))
        window.blit(instructions_textc, (instructions_xc, instructions_y - 50))

        pygame.display.update()
        


    #Title Screen
    while x == 0 and y % 2 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                x += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                y += 1

        window.fill(BLACK)
        window.blit(pygame.image.load("Images\PlutoW.png").convert(), (WIDTH // 2 - 45, 650))
        window.blit(title_text, (title_x, title_y))
        window.blit(instructions_text, (instructions_x, instructions_y))
        window.blit(instructions_text2, (instructions_x, instructions_y + 75))

        pygame.display.update()
        
    

    #Game
    while x == 1 and y % 2 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #MOVEMENT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                move1 = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                y += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                move2 = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                move3 = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                move4 = True

            elif event.type == pygame.KEYUP and event.key == pygame.K_w:
                move1 = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                move2 = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                move3 = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                move4 = False

            elif move1 == True:
                q -= 15
            elif move2 == True:
                q += 15
            elif move3 == True:
                p -= 15
            elif move4 == True:
                p += 15

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_j and i > 1600:
                i = p + 25
                j = q + 15


        window.blit(pygame.image.load("Images\Back.png").convert(), (0, 0))
        window.blit(pygame.image.load("Images\Pluto45.png").convert(), (p, q))
        window.blit(pygame.image.load("Images\Charon.png").convert(), (i, j))
        window.blit(pygame.image.load("Images\eptune.png").convert(), (m, n))
        window.blit(pygame.image.load("Images\Ice1.png").convert(), (k1, l1))
        window.blit(pygame.image.load("Images\Ice2.png").convert(), (k2, l2))
        window.blit(pygame.image.load("Images\Ice3.png").convert(), (k3, l3))

        if n < 100:
            for l in range (15):
                n += 1
        elif n > 800:
            for l in range (15):
                n -= 1
        elif random.randint(0,100) >= 99:
            for l in range (5):
                n += 1
        elif random.randint(0,100) <= 1:
            for l in range (5):
                n -= 1
        else:
            for l in range (5):
                n += 0

        if abs(i - m) < 30 and abs(j - n) < 50:
            current_health2 -= 10
        elif abs(p - k1) < 30 and abs(q - l1) < 50:
            current_health -= 5
        elif abs(p - k2) < 30 and abs(q - l2) < 50:
            current_health -= 5
        elif abs(p - k3) < 30 and abs(q - l3) < 50:
            current_health -= 5


        #OUT OF BOUNDS
        if p <= 30:
            p = 30
        elif p >= 700:
            p = 700
        elif q >= 870:
            q = 870
        elif q <= 30:
            q = 30



        #P HP
        health_bar_width = int((current_health / max_health) * bar_width)
        pygame.draw.rect(window, RED, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(window, GREEN, (bar_x, bar_y, health_bar_width, bar_height))

        #ENEMY HP
        health_bar_width2 = int((current_health2 / max_health2) * bar_width2)
        pygame.draw.rect(window, RED, (bar_x2, bar_y2, bar_width2, bar_height))
        pygame.draw.rect(window, GREEN, (bar_x2, bar_y2, health_bar_width2, bar_height))


        if k1 < -1000:
            k1 = m
            l1 = n
        elif k2 < -5000:
            k2 = m
            l2 = n
        elif k3 < -10000:
            k3 = m
            l3 = n

        if i > 1700:
            i = 1700
        i += 10
        k1 -= 10
        k2 -= 10
        k3 -= 10


        while current_health2 <= 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    y += 1

            window.fill(BLACK)
            window.blit(pygame.image.load("Images\Pluto2.png").convert(), (WIDTH // 2 - 45, 650))
            window.blit(title_font.render("You WIN! Pluto can finally be a planet!", True, WHITE), (title_x, title_y))
            pygame.display.update()

        #Lose
        while current_health <= 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    y += 1

            window.fill(BLACK)
            window.blit(title_font.render("You lost!", True, WHITE), (title_x, title_y))
            pygame.display.update()

        pygame.display.update()

    
    




# Quit the game
pygame.mixer.music.stop()
pygame.quit()