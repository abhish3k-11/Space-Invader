import pygame
import random

# initialize pygame
pygame.init()


# create the screen
screen = pygame.display.set_mode((800, 600))

# adding background image
bg = pygame.image.load('background.png')

# adding logo and title to window
pygame.display.set_caption("Space Invaders")
icon1 = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon1)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(45, 150)
enemyX_change = 3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game loop makes sure window doesn't close abruptly and keeps running
running = True
while running:
    # bg color implementation
    screen.fill((0, 0, 25))
    # background image
    screen.blit(bg, (0, 0))

    # for closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # for movement of spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0.0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movements
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    if enemyY >= 600:
        enemyY = 45

    enemyX += enemyX_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
