import pygame
import random

pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

bg = pygame.image.load("images/background.png")
gunPointer = pygame.image.load("images/aim_pointer.png")
gunImage = pygame.image.load("images/gun_1.png")

zombie_1 = pygame.image.load("images/zombie_1.gif")
zombie_2 = pygame.image.load("images/zombie_2.png")
zombie_3 = pygame.image.load("images/zombie_3.png")

shot_sound = pygame.mixer.Sound("sounds/gunShot.wav")

zombieList = [zombie_1, zombie_2, zombie_3]
zombieImage = random.choice(zombieList)

zombie_x = random.randint(0,650)
zombie_y = random.randint(0,400)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            shot_sound.play(0)
            if rect_1.colliderect(rect_2):
                zombie_x = random.randint(0,650)
                zombie_y = random.randint(0,400)
                zombieImage = random.choice(zombieList)

    posX, posY = pygame.mouse.get_pos()

    rect_1 = pygame.Rect(posX-50, posY-50, gunPointer.get_width(), gunPointer.get_height())
    rect_2 = pygame.Rect(zombie_x, zombie_y, zombieImage.get_width(), zombieImage.get_height())

    screen.fill((255,255,255))
    screen.blit(bg, (0,0))
    screen.blit(zombieImage, (zombie_x, zombie_y))
    screen.blit(gunPointer, (posX-50, posY-50))
    screen.blit(gunImage, (posX, height - 300))

    pygame.display.update()
