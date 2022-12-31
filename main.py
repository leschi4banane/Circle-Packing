import pygame as pg
from pygame import gfxdraw
import random
import time
import math

def max_radius(x, y):
    # distance to x borders 
    max_x = 0
    if x > screen_size/2: max_x = screen_size/2-(x-screen_size/2)
    else: max_x = x
    # distance to y borders 
    max_y = 0
    if y > screen_size/2: max_y = screen_size/2-(y-screen_size/2)
    else: max_y = y
    # sets samller one as max radius
    max_rad = 0
    if max_x < max_y: max_rad = max_x
    else: max_rad = max_y

    for i in circles:
    # calculates distance between two points
        dist = math.hypot(i[0]-x, i[1]-y)
        if dist-i[2] < max_rad:
            max_rad = dist-i[2]

    return round(max_rad)

def check_inside(pos):
    for c in circles:
        distance = math.hypot(c[0]-pos[0], c[1]-pos[1])
        if distance < c[2]:
            return False      
    return True

    


pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

screen_size = screen.get_width()

tries = 1000
circles = []

run = True
change = True
while run:
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            change = True
            if event.key == pg.K_RIGHT:
                tries += 1
            if event.key == pg.K_LEFT:
                tries -= 1
    screen.fill((255,255,255))

    if change:
        pg.display.set_caption(f"tries : {tries}")
        for i in range(tries):
            cordinates = (random.randrange(screen_size), random.randrange(screen_size))
            radius = max_radius(cordinates[0], cordinates[1])
            #pg.draw.circle(screen, (255,0,0), cordinates, 1)
            if check_inside(cordinates):
                circles.append((cordinates[0], cordinates[1], radius))
                gfxdraw.aacircle(screen, cordinates[0], cordinates[1], radius, (0,0,0))
                gfxdraw.filled_circle(screen, cordinates[0], cordinates[1], radius, (0,0,0))
        pg.display.flip()
        change = False
        circles.clear()




