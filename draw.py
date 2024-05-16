#今後実装予定

import pygame as pg

def draw_text(siz, txt, col, bg, x, y):  # テキストの描画
    fnt = pg.font.Font("img/MPLUS.ttf", siz)  # フォント指定
    sur = fnt.render(txt, True, col)  # テキストの指定
    bg.blit(sur, [x, y])  # テキストの配置

def draw_button(bg, col_r, button, siz, txt, col_f):  # ボタンの描画
    pg.draw.rect(bg, col_r, button, border_radius=10)
    fnt = pg.font.Font("img/MPLUS.ttf", siz)  # フォント指定
    sur = fnt.render(txt, True, col_f)  # テキストの指定
    w = button[0] + button[2] / 2 - sur.get_width() / 2  # 幅
    h = button[1] + button[3] / 2 - sur.get_height() / 2  # 高さ
    bg.blit(sur, [w, h])  # テキストの配置
