import pygame, random, time, os, sys
from pygame.locals import *
from images import *

# Required constants
x = 0
y = 0
width = 800
height = 800
position = 365
bgcolour = (255, 255, 0)

# Setting up the game screen
screen = pygame.display.set_mode((width, height))

cars = [car1, car2, car3, car4, car5, car6, car7, truck]
random_car = random.choice(cars)
trees = [tree, tree1, tree2]
random_tree = random.choice(trees)
random_tree2 = random.choice(trees[0:2])

pygame.init()
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Road rage!!!")

# Defining some fonts
font = pygame.font.SysFont(None, 40)
font1 = pygame.font.SysFont('monospace', 30)
font2 = pygame.font.SysFont('monospace', 25)
font3 = pygame.font.SysFont(None, 70)
font4 = pygame.font.SysFont('monospace', 40)

# Reading the stored high score from a file.
read = open("highscore.txt", 'r')
topScore = float(read.readline())
read.close()
# Initializing music.
pygame.mixer.init()
swish = pygame.mixer.Sound("soundfiles/swish.ogg")


# Function to create buttons on screen.
def buttons(xpos, ypos, colour, text, width, height):
    pygame.draw.rect(screen, colour, (xpos, ypos, width, height))
    msg = font.render(text, 1, (0, 0, 0))
    screen.blit(msg, (xpos + 25, ypos + 12))


# Function to display the start screen.
def start():
    pygame.mixer.music.load("soundfiles/menumusic.mp3")
    pygame.mixer.music.play(-1)
    while (1):
        screen.blit(bgimage, (0, 0))
        screen.blit(roadrage, (0, 150))
        label = font.render("Press 'Enter' or click below to start.", 1, (255, 255, 0))
        screen.blit(label, (130, 470))
        buttons(270, 530, (229, 158, 36), "LETS GO!!", 200, 60)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (270 < mouse[0] < 470 and 530 < mouse[1] < 590):
            buttons(270, 530, (220, 160, 220), "LETS GO!!", 200, 60)
            if click[0] == 1:
                return 1
        pygame.display.update()
        command = pygame.event.poll()
        if (command.type == pygame.KEYDOWN):
            if (command.key == pygame.K_RETURN):
                return 1
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()


# Function to display game over screen.
def gameover():
    while (1):
        screen.blit(bgimage, (0, 0))
        screen.blit(roadrage, (0, 150))
        label = font3.render("GAME OVER", 1, (255, 255, 0))
        screen.blit(label, (250, 380))
        label2 = font4.render("PLAY AGAIN ???", 1, (255, 165, 0))
        screen.blit(label2, (230, 450))
        buttons(250, 500, (0, 150, 0), "YES", 100, 50)
        buttons(420, 500, (150, 0, 0), "QUIT", 100, 50)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (250 < mouse[0] < 350 and 500 < mouse[1] < 550):
            buttons(250, 500, (220, 160, 220), "YES", 100, 50)
            if click[0] == 1:
                return 1
        if (420 < mouse[0] < 520 and 500 < mouse[1] < 550):
            buttons(420, 500, (220, 160, 220), "QUIT", 100, 50)
            if click[0] == 1:
                pygame.quit()
                quit()
        pygame.display.update()
        command = pygame.event.poll()
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()
