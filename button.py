import pygame
from consts import *


class ColorButton:
    BUT_RADIUS = 20
    buttons = []

    def __init__(self, color: tuple, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y
        ColorButton.buttons.append(self)

    def __del__(self):
        pass

    def draw(self, window, font, fill: tuple):
        if self.color == BLACK:
            outline = WHITE
        else:
            outline = BLACK

        pygame.draw.circle(window, outline, (self.x, self.y), self.BUT_RADIUS + 2)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.BUT_RADIUS)
        if self.color == fill:
            if fill != BLACK:
                textcolor = BLACK
            else:
                textcolor = WHITE
            empty = font.render("E", True, textcolor)
            window.blit(empty, (self.x - 6, self.y - 6))

    @classmethod
    def button_clicked(cls, x, y):
        for button in cls.buttons:
            if (
                button.x - cls.BUT_RADIUS <= x <= button.x + cls.BUT_RADIUS
                and y <= (5 + cls.BUT_RADIUS) * 2
            ):
                return button.color

    @classmethod
    def del_buttons(cls):
        for button in cls.buttons:
            del button
        cls.buttons.clear()

