import pygame
from pygame.locals import (
    QUIT,
    Rect,
)


from consts import *
from button import ColorButton as CB


pygame.init()

font = pygame.font.SysFont("chalkduster.ttf", 24)


def display(rect=None):
    if rect:
        pygame.display.update(rect)
        return
    pygame.display.update()


def setup_cells(window, fill=WHITE):
    CB.del_buttons()

    window.fill(fill)

    middle = WIDTH // 2
    offset = CB.BUT_RADIUS * 2 + 10
    xLocs = [middle + (offset * n) for n in range(-5, 6)]

    rad = CB.BUT_RADIUS + 10

    for i in range(len(xLocs)):
        CB(COLORS[i], xLocs[i], 10 + CB.BUT_RADIUS).draw(window, font, fill)

    if fill == BLACK:
        linecolor = WHITE
    else:
        linecolor = BLACK

    y = (12 + CB.BUT_RADIUS) * 2
    pygame.draw.line(window, linecolor, (0, 0), (WIDTH, 0), 2)
    pygame.draw.line(window, linecolor, (0, y), (WIDTH, y), 2)


def update_cell(window, color, x, y, size=RADIUS):
    rX, rY = int(x), int(y)
    if rY >= (14 + CB.BUT_RADIUS) * 2:
        pygame.draw.circle(window, color, (rX, rY), size)
        return (rX - size, rY - size, size * 2, size * 2)


win = pygame.display.set_mode((WIDTH, HEIGHT))
setup_cells(win)

display()

update = None
eraser = None

current_color = BLACK
current_fill = WHITE

rad = CB.BUT_RADIUS + 10

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
                if current_fill == color:
                    eraser = True
                else:
                    eraser = False
                    current_color = color
            elif eraser:
                rect = update_cell(win, current_fill, *mouse, size=ERASER)
                update = bool(rect)
            else:
                rect = update_cell(win, current_color, *mouse)
                update = bool(rect)

        elif pressed[2]:
            mouse = pygame.mouse.get_pos()
            if (color := CB.button_clicked(*mouse)) :
                current_fill = color
            else:
                setup_cells(win, current_fill)
                display()

    if update:
        display(Rect(*rect))
        update = False

pygame.quit()

