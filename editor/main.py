import pygame
import sys
from pygame.locals import *

from directories import *


def draw_text(text, screen, x, y, x_end,
              y_end):  # размер букв - 7x8 строчные, 7x11 уходящие в низ(по типу "p" "g", 7x10 заглавные а так высота всей строчки 14п таблица 8 на 10
    pass  # TODO


# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-+[]{}\|;:'",.<>/?#

pygame.init()
width = 1920
height = 1007
Scene = pygame.display.set_mode((width, height), pygame.RESIZABLE)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            print("Все папки и файлы:", get_dirs())

    # =========================
    Scene.fill((0, 0, 0))
    pygame.draw.line(Scene, (255, 255, 255), (150, 0), (150, 750), 1)
    pygame.draw.line(Scene, (255, 255, 255), (0, 750), (1920, 750), 1)
    pygame.draw.line(Scene, (255, 255, 255), (760, 0), (760, 750), 1)
    pygame.draw.line(Scene, (255, 255, 255), (1720, 0), (1720, 750), 1)
    pygame.display.update()
    # =========================
