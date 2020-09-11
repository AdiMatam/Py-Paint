import pygame


class ColorButton:
    BUT_RADIUS = 20
    buttons = []

    def __init__(self, color: tuple, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y
        ColorButton.buttons.append(self)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.BUT_RADIUS)

    @classmethod
    def button_clicked(cls, x, y):
        for button in cls.buttons:
            if (
                button.x - cls.BUT_RADIUS <= x <= button.x + cls.BUT_RADIUS
                and button.y - cls.BUT_RADIUS <= y <= button.y + cls.BUT_RADIUS
            ):
                return button.color
