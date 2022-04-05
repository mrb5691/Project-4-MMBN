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
    def Sanimate(self):
        self.is_shooting = True 

    def moveAni(self):
        if self.is_moving == True:
            self.current_sprite +=1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_moving = False
            self.image = self.sprites[self.current_sprite]

    def shootAni(self):
        if self.is_shooting == True:
            self.current_sprite +=1
            if self.current_sprite >= len(self.shoot_sprites):
                self.current_sprite = 0
                self.is_shooting = False
            self.image = self.shoot_sprites[self.current_sprite]

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

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.is_moving = False
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still2.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still3.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still4.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move1.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move2.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move3.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move2.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-move1.png"), (100,100)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)))
        self.shoot_sprites = []
        self.is_shooting = False
        self.shoot_sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)))
        self.shoot_sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-shoot2.png"), (100,100)))
        self.shoot_sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-shoot1.png"), (100,100)))
        self.shoot_sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-shoot2.png"), (100,100)))
        self.shoot_sprites.append(pygame.transform.scale(pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-still1.png"), (100,100)))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (200,400)
        self.health = 20
        

    def animate(self):
        self.is_moving = True  

    def Sanimate(self):
        self.is_shooting = True

    def moveAni(self):
        if self.is_moving == True:
            self.current_sprite +=1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_moving = False
            self.image = self.sprites[self.current_sprite]

    def shootAni(self):
        
        if self.is_shooting == True:
            self.current_sprite += 0.25
            if self.current_sprite >= len(self.shoot_sprites):
                self.current_sprite = 0
                self.is_shooting = False
            self.image = self.shoot_sprites[int(self.current_sprite)]
        else:
            self.image = self.sprites[self.current_sprite]
        return Bullet(self.rect.centerx,self.rect.centery)
        

    def move(self):
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_w:
                    if self.rect.top > 260:
                        self.animate()
                        self.rect.move_ip(0,-90)
                elif event.key == pygame.K_s:
                    if self.rect.top < 440:
                        self.animate()
                        self.rect.move_ip(0,90)
                elif event.key == pygame.K_a:
                    if self.rect.right > 115:
                        self.animate()
                        self.rect.move_ip(-135,0)
                elif event.key == pygame.K_d:
                    if self.rect.right < 385:
                        self.animate()
                        self.rect.move_ip(135,0)
                elif event.key == pygame.K_SPACE:
                    self.Sanimate()
                    bullet_group.add(self.shootAni())
        self.moveAni()
        self.shootAni()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("/Users/mitchellbennett/sei/unit4/Project4/Sprites/Megaman-bullet1.png")
        # self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def move(self):
        self.rect.x += 60
        if self.rect.x >= SCREEN_WIDTH +100:
            self.kill()


#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
bullet_group = pygame.sprite.Group()
 
#Adding a new User event 
DEAD = pygame.USEREVENT + 1

#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == DEAD:
            DISPLAYSURF.fill(RED)
            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()        
    
    DISPLAYSURF.blit(bg_img,(0,0))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        textsurface = FONT.render(str(entity.health), True, FONT_COLOR)
        textrect = textsurface.get_rect()
        entity.image.blit(textsurface, textrect)
        entity.move()
    for bullet in bullet_group:
        DISPLAYSURF.blit(bullet.image, bullet.rect)
        bullet.move()
    if pygame.sprite.spritecollideany(E1, bullet_group):
        if E1.health >= 1:
            E1.health -= 1
        elif E1.health < 1:
            DEAD     
         
    pygame.display.update()
    FramePerSec.tick(FPS)