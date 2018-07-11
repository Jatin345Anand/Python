import pygame
import random

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.jpg")

rect_x = 0
rect_y = 0
move_x = 8
move_y = 8

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()

    screen.fill(white)

    # pygame.draw.rect(screen, red, (rect_x,rect_y,50,50))
    screen.blit(ball, (rect_x, rect_y))
    rect_x += move_x
    rect_y += move_y

    if rect_x > width - 225:
        move_x = -8
    elif rect_y > height - 225:
        move_y = -8
    elif rect_x < 0:
        move_x = 8
    elif rect_y < 0:
        move_y = 8

    pygame.display.update()
    clock.tick(FPS)
