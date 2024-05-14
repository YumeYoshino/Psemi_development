import pygame as pg
from draw import draw_text

def game_main(screen, tmr, color):
    screen.fill(color["black"])
    draw_text(70, "始める", color["white"], screen, 30, 100)