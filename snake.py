import pygame
import random

pygame.init()

# colors used in the game

pink = (215, 2, 112)
green = (0, 153, 0)
blue = (0, 56, 168)
yellow = (255, 255, 102)
red = (216, 34, 47)

dimensions = (600, 600)

# initial values

x = 300 # initial position of snake on x-axis
y = 300 # initial position of snake on y-axis

d = 20 # dimension of the "units" of the snake (in pixels)

snakeRay = [[x, y]]

dx = 0 # snake movement on x-axis
dy = 0 # snake movement on y-axis

foodX = round(random.randrange(0, 600 - d) / 20) * 20 # food position on x-axis
foodY = round(random.randrange(0, 600 - d) / 20) * 20 # food position on y-axis

font = pygame.font.SysFont('Cambria Math', 24)

screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption('Snake Game by Estevão J. P. B. de França')

screen.fill(blue)

clock = pygame.time.Clock()

# setting when you lose the game (!!! still need to create a "reset" button !!!)

def gameOver():
    fontGameOver = pygame.font.SysFont('Cambria Math', 30)
    textGameOver = fontGameOver.render('GAME OVER', True, red)
    screen.fill(blue)
    screen.blit(textGameOver, [245, 300])

# drawing the snake on screen

def snakeDraw():
    screen.fill(blue)
    for unit in snakeRay:
        pygame.draw.rect(screen, pink, [unit[0], unit[1], d, d])

# setting the keys that will be used to move the snake

def snakeMove(dx, dy, snakeRay):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx  = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    newX = snakeRay[-1][0] + dx
    newY = snakeRay[-1][1] + dy

    snakeRay.append([newX, newY])

    del snakeRay[0]

    return dx, dy, snakeRay

# making food appear randomly

def foodCheck(dx, dy, foodX, foodY, snakeRay):

    head = snakeRay[-1]

    newX = head[0] + dx
    newY = head[1] + dy

    if head[0] == foodX and head[1] == foodY:
        snakeRay.append([newX, newY])
        foodX = round(random.randrange(0, 600 - d) / 20) * 20
        foodY = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(screen, green, [foodX, foodY, d, d])

    return foodX, foodY, snakeRay

# limiting snake movement inside game screen

def wallCheck(snakeRay):
    head = snakeRay[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        gameOver()

# cheking if the snake hits itself

def snakeBiteCheck(snakeRay):
    head = snakeRay[-1]
    body = snakeRay.copy()

    del body[-1]
    for x, y in body:
        if x == head[0] and y == head[1]:
            gameOver()

# sets the game score (snake length)

def scoreUpdate(snakeRay):
    pts = str(len(snakeRay))
    score = font.render('Pontuation: ' + pts, True, yellow)
    screen.blit(score, [10, 10])

# running the game

while True:
    pygame.display.update()
    snakeDraw()
    dx, dy, snakeRay = snakeMove(dx, dy, snakeRay)
    foodX, foodY, snakeRay = foodCheck(
        dx, dy, foodX, foodY, snakeRay)
    wallCheck(snakeRay)
    snakeBiteCheck(snakeRay)
    scoreUpdate(snakeRay)


    clock.tick(10)
