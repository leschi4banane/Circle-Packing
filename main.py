import pygame as pg
import random, math

# retrurns a color on the rainbow depending on a value between 0 and 1
def radius_to_rainbow(prog):
    step = (prog*1536 // 255) % 6
    pos = prog*1536 % 255
    if step == 0:
        return (255, pos, 0)
    if step == 1:
        return (255-pos, 255, 0)
    if step == 2:
        return (0, 255, pos)
    if step == 3:
        return (0, 255-pos, 255)
    if step == 4:
        return (pos, 0, 255)
    if step == 5:
        return (255, 0, 255-pos)

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

    for i in circles:
    # calculates distance between two points
        dist = math.hypot(i[0]-x, i[1]-y)
        if dist-i[2] < max_rad:
            max_rad = dist-i[2]
    # retruns value
    return max_rad

def check_inside(pos):
    # ckecks if the given point is in another circle
    # retuns True if the point is not in another circle
    for c in circles:
        # if the distance between the two points is smaller than the radius of the circle, than the point is in another circle
        distance = math.hypot(c[0]-pos[0], c[1]-pos[1])
        if distance < c[2]:
            return False      
    return True

# sets up pygame
pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()
# creates variable that stores screensize (only works if the windows is square)
screen_size = screen.get_width()

tries = 10_000
circles = []
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
    screen.fill((255,255,255))
    # if a change in the settings happened
    if change:
        # displays how many tries are slected in the caption
        pg.display.set_caption(f"tries : {tries}")
        for i in range(tries):
            # counts up the trie its on (used for color)
            try_count += 1
            # creates random positon in the window
            cordinates = (random.randrange(screen_size), random.randrange(screen_size))
            # calculates max radius depending on the window borders and all the other circles
            radius = max_radius(cordinates[0], cordinates[1])
            # gets color depending on the progressin of the tries
            color = radius_to_rainbow(try_count/tries)
            # if the random point is not in another circle
            if check_inside(cordinates):
                # appends the new circle into the list
                circles.append((cordinates[0], cordinates[1], radius))
                # draws circle
                pg.draw.circle(screen, color, cordinates, radius)

        change = False
        pg.display.flip()
        circles.clear()