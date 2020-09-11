import pygame
from pygame.locals import (
    QUIT,
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_UP,
    Rect,
)


from consts import *
from button import ColorButton as CB


def display(rect=None):
    if rect:
        pygame.display.update(rect)
        return
    pygame.display.update()


def setup_cells(window):
    for i in range(0, WIDTH, CELLSIZE):
        for j in range(0, HEIGHT, CELLSIZE):
            pygame.draw.rect(window, WHITE, (i, j, CELLSIZE, CELLSIZE))

    middle = WIDTH // 2
    offset = 30 + CB.BUT_RADIUS
    xLocs = [middle + (offset * n) for n in range(-4, 5)]

    for i in range(len(xLocs)):
        CB(COLORS[i], xLocs[i], 10 + CB.BUT_RADIUS).draw(window)


def update_cell(window, color, x, y):
    rX, rY = int(x), int(y)
    pygame.draw.circle(window, color, (rX, rY), RADIUS)
    offset = CELLSIZE // 2
    return (rX - offset, rY - offset, CELLSIZE, CELLSIZE)


pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
setup_cells(win)

display()

update = None

current_color = BLACK

run = True
while run:
    for event in pygame.event.get():
        pressed = pygame.mouse.get_pressed()

        if event.type == QUIT:
            run = False

        if pressed[1]:
            setup_cells(win)
            pygame.display.update()

        elif pressed[0]:
            mouse = pygame.mouse.get_pos()
            if (color := CB.button_clicked(*mouse)) :
                current_color = color
            else:
                update = True
                rect = update_cell(win, current_color, *mouse)

    if update:
        display(Rect(*rect))
        update = False

pygame.quit()
