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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.is_moving = False
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still2.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still3.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still4.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move1.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move2.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move3.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move2.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move1.png"), (100,100)), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)), True, False))
        self.shoot_sprites = []
        self.is_shooting = False
        self.shoot_sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)), True, False))
        self.shoot_sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-shoot2.png"), (100,100)), True, False))
        self.shoot_sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-shoot1.png"), (100,100)), True, False))
        self.shoot_sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-shoot2.png"), (100,100)), True, False))
        self.shoot_sprites.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)), True, False))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (600,400)
        self.health = 5
        
    def animate(self):
        self.is_moving = True

    def move(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.update_delay:
            self.last_update = now
            action = random.randint(0,4)
            if action == 0:
                if self.rect.top > 260:
                    self.animate()
                    self.rect.move_ip(0,-90)
            elif action == 1:
                if self.rect.top < 440:
                    self.animate()
                    self.rect.move_ip(0,90)
            elif action == 2:
                if self.rect.right > 515:
                    self.animate()
                    self.rect.move_ip(-135,0)
            elif action == 3:
                if self.rect.right < 785:
                    self.animate()
                    self.rect.move_ip(135,0)
        self.moveAni()