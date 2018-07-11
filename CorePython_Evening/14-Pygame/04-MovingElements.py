import pygame
import random

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

color_list = [red, green, blue, yellow]

color = random.choice(color_list)

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

rect_x = 0
rect_y = 0
move_x = 3
move_y = 3

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()


    screen.fill(white)

    # pygame.draw.rect(screen, red, (rect_x,rect_y,50,50))
    pygame.draw.circle(screen, color, (rect_x, rect_y), 50)

    rect_x += move_x
    rect_y += move_y

    if rect_x > width - 50:
        move_x = -3
        color = random.choice(color_list)
        FPS += 5
    elif rect_y > height - 50:
        move_y = -3
        FPS += 5
        color = random.choice(color_list)
    elif rect_x < 50:
        move_x = 3
        FPS += 5
        color = random.choice(color_list)
    elif rect_y < 50:
        move_y = 3
        FPS += 5
        color = random.choice(color_list)

    pygame.display.update()
    clock.tick(FPS)
