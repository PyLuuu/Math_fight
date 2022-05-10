import pygame as pg
import PLSprite as PLS

pg.init()
largura, altura = (500, 400)
pg.display.set_mode((largura, altura))
pg.display.set_caption('Math Fight')
icon = pg.image.load('imagens\inimigos\Broly\pasivo\parado/broly1.bmp')
pg.display.set_icon(icon)
