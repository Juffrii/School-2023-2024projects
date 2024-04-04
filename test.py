import sys

import pygame
from pygame.locals import *


class CodingHabbit:
    def __init__(self):
        self.text = ""
        self.file = ""
        self.cursor = (0, 0)  # переменная с кординатоми курсора в тексте

    def load_text(self, file_name):
        f = open(file_name)
        self.text = f.read()
        f.close()
        return True

    def render(self, sc):  # TODO рендер
        text = self.text.split("\n")  # отрисовка текста (текст кода - пока без подстветки и анализа синтаксиса
        my_font = pygame.font.SysFont(None, 30)
        for i in range(len(text)):
            text_surface = my_font.render(text[i], False, (255, 255, 255))
            sc.blit(text_surface, (0, i * 30))
        # отрисовка границ (прямоугольник без границ)
        # закраска текста за границей
        # чёнибудь ещё
        return True

    def drag_zone(self):  # TODO зона перетаскивание уменьшение увеличение размеров
        pass

    def do_key_operation(self):  # TODO работа с клавишами
        pass

    def syntactics_check(self):  # TODO late feature
        pass


pygame.init()
screen = pygame.display.set_mode((960, 540), HWSURFACE | DOUBLEBUF | RESIZABLE)
fake_screen = screen.copy()  # создание второго фальшивого экрана экрана

writing = CodingHabbit()
writing.load_text("test_file.txt")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

    fake_screen.fill('black')
    writing.render(fake_screen)  # очередь ренедра -> слева направо

    screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
    pygame.display.flip()
