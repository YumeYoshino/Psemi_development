#今後実装予定

import pygame as pg
from draw import draw_text
def game_save(screen, tmr, color):

        screen.fill(color["black"])
        draw_text(70, "つづける", color["white"], screen, 30, 100)
        draw_text(70, "xxx", color["white"], screen, 30, 150)
        if tmr > 30:
            idx = 0
            tmr = 0


    