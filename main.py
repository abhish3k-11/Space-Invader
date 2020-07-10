import pygame
import math
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
enemyX = random.randint(0, 735)
enemyY = random.randint(45, 150)
enemyX_change = 2
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 6
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(((enemyX-bulletX)**2) + ((enemyY-bulletY)**2))
    if distance < 27:
        return True
    else:
        return False


score = 0

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
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # get the current position of spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    if enemyY >= 600:
        enemyY = 45

    enemyX += enemyX_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fired":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(45, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
