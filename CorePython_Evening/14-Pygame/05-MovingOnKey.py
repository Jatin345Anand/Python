import pygame
import random

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

rect_x = 0
rect_y = 0
move_x = 0
move_y = 0

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 3
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 3
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -3
                move_x = 0
            elif event.key == pygame.K_LEFT:
                move_x = -3
                move_y = 0

    screen.fill(white)

    pygame.draw.rect(screen, red, (rect_x,rect_y,50,50))

    rect_x += move_x
    rect_y += move_y

    if rect_x > width - 50:
        move_x = -3
    elif rect_y > height - 50:
        move_y = -3
    elif rect_x < 0:
        move_x = 3
    elif rect_y < 0:
        move_y = 3

    pygame.display.update()
    clock.tick(FPS)
