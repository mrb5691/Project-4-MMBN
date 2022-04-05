from re import X
import pygame, sys
from pygame.locals import *
import random, time

#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FONT = pygame.font.SysFont('Arial', 20)
FONT_COLOR = pygame.Color('white')

 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("Megaman: Pygame Network")

bg_img = pygame.image.load('/Users/mitchellbennett/sei/unit4/Project4/Sprites/MMBNbattleground.png')
bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HEIGHT)) 