import pygame

pygame.init()

white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((800, 500))

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()


    screen.fill(white)

    pygame.draw.rect(screen, red, (10,20,50,50))

    pygame.draw.circle(screen, red, (100,100), 50)

    pygame.display.update()
