#今後実装予定

import pygame as pg
from pygame.locals import *
import sys
#import yomikomi
from draw import draw_text, draw_button
from game import game_main
from save import game_save

color = {"white": (255, 255, 255), "black": (0, 0, 0), "blue": (0, 255, 255)}  # 色の指定
tmr = 0  # タイマー
idx = 0  # インデックス
# 0:タイトル, 1
def main(): 
    global tmr, idx

    pg.init()
    pg.display.set_caption("インシデント対応")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    button = [pg.Rect(110, 360, 120, 40),  # 始めるボタン
              pg.Rect(170, 410, 120, 40),  # 続けるボタン
              pg.Rect(240, 470, 120, 40)]  # やめるボタン
    words = ["はじめる", "つづける", "おわる"]

    # 背景画像の読み込み
    bg_image = pg.image.load("img/_high_rise_building_1.jpg").convert()
    bg_image = pg.transform.scale(bg_image, (800, 600))

    while True:
        tmr += 1
        for e in pg.event.get():
            if e.type == QUIT:
                pg.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                if e.key == K_F1:  # フルスクリーンにする
                    screen = pg.display.set_mode((800, 800), pg.FULLSCREEN)
                    bg_image = pg.transform.scale(bg_image, (800, 800))
                if e.key == K_F2 or e.key == K_ESCAPE:  # もとに戻す
                    screen = pg.display.set_mode((800, 600))
                    bg_image = pg.transform.scale(bg_image, (800, 600))
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                if idx == 0:
                    if button[0].collidepoint(e.pos): 
                        idx = 1
                        tmr = 0
                    if button[1].collidepoint(e.pos): 
                        idx = 2
                        tmr = 0
                    if button[2].collidepoint(e.pos): 
                        idx = 3
                        tmr = 0

        # 背景画像の描画
        screen.blit(bg_image, (0, 0))

        if idx == 0:  # タイトル画面メイン処理
            draw_text(70, "インシデント対応", color["black"], screen, 30, 100)
            draw_text(75, "RPG", color["black"], screen, 30, 220)

            for i in range(3):
                draw_button(screen, color["white"], button[i], 24, words[i], color["blue"])

        elif idx == 1:  # ゲーム本体処理
            game_main(screen, tmr, color)

        elif idx == 2:  # セーブ＆ロード処理
            game_save(screen, tmr, color)

        elif idx == 3:  # ゲーム終了処理
            sys.exit()  # プログラムを終了する

        pg.display.update()
        clock.tick(15)

if __name__ == "__main__":
    main()
