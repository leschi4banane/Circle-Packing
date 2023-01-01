import pygame as pg
import random, math

# retuns the max radius for a circle on a point
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

    for i in circles_r:
    # calculates distance between two points
        dist = math.hypot(i[0]-x, i[1]-y)
        if dist-i[2] < max_rad:
            max_rad = dist-i[2]
    # retruns value
    return math.ceil(max_rad)

def delete_inside_points(pos, rad):
    circles_p[:] = [i for i in circles_p if math.hypot(i[0]-pos[0], i[1]-pos[1]) > rad]

# sets up pygame
pg.init()
screen = pg.display.set_mode((800,800),pg.RESIZABLE)
clock = pg.time.Clock()
# creates variable that stores screensize (only works if the windows is square)
screen_size = screen.get_width()

tries = 10000
circles_p = []
circles_r = []
try_count = 0

# main loop
run = True
change = True
while run:
    # ckecks for quiting
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            change = True
    screen.fill((255,255,255))
    # if a change in the settings happened
    if change:
        # displays how many tries are selected in the caption
        pg.display.set_caption(f"tries : {tries}")
        for i in range(tries):
            random_cords = (random.randrange(screen_size), random.randrange(screen_size))
            circles_p.append(random_cords)
        for i in circles_p:
            radius = max_radius(i[0], i[1])
            circles_r.append((i[0], i[1], radius))

            pg.draw.circle(screen, (0,0,0), i, radius)
  
            delete_inside_points(i, radius)

            circles_r.append((i[0], i[1], radius))
            

        change = False
        pg.display.flip()
        circles_p.clear()
        circles_r.clear()
