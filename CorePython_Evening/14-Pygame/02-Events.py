import pygame

pygame.init()

white = 255,255,255

screen = pygame.display.set_mode((800, 500))

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN:
            print("Key Press event")

    screen.fill(white)

    pygame.display.update()
