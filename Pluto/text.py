import pygame
from colors import *
from main import *

WIDTH = 1600
HEIGHT = 900

title_font = pygame.font.SysFont("Arial", 60)
text_font = pygame.font.SysFont("Arial", 30)

title_text = title_font.render("Pluto: The Quest for Independence", True, WHITE)
instructions_text = text_font.render("Press SPACE to Start", True, WHITE)

title_x = WIDTH / 2 - title_text.get_width() / 2
title_y = HEIGHT // 2 - title_text.get_height() // 2 - 50
instructions_x = WIDTH // 2 - instructions_text.get_width() // 2
instructions_y = HEIGHT // 2 - instructions_text.get_height() // 2 + 50