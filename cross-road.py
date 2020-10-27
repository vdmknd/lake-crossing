from random import *
import sys
import os
import pygame
pygame.init()

screen = pygame.display.set_mode((700,700))

boats = []
boats_gone = 0
delta_B = 1
delta_D = 1
level = 1
emergency = False


image_address1 = os.path.join('images','boat.png')
boat_img = pygame.image.load(image_address1).convert_alpha()
image_address2 = os.path.join('images','duck.png')
duck_img = pygame.image.load(image_address2).convert_alpha()
image_address3 = os.path.join('images','revboat.png')
revboat_img = pygame.image.load(image_address3).convert_alpha()

class Duck():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((35,35))
        self.rect = self.image.get_rect()
        self.x = 320
        self.y = 620
    def draw(self):
        screen.blit(duck_img,(self.x,self.y))
    def move(self):
        if not emergency:
            self.y-=0.05*delta_D
        else:
            self.x+=boatspeed
        self.rect.y = self.y
        self.rect.x = self.x
class Boat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70,20))
        self.rect = self.image.get_rect()
        self.x = 770
        self.y = randint(20,600)
        self.direction = -1
        self.speed = random()/2*level
    def draw(self):
        screen.blit(boat_img,(self.x,self.y))
    def move(self):
        self.x+=self.speed*self.direction*delta_B
        self.rect.x = self.x
        self.rect.y = self.y
class ReversedBoat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70,20))
        self.rect = self.image.get_rect()
        self.x = -70
        self.y = randint(20,600)
        self.direction = 1
        self.speed = random()/2*level
    def draw(self):
        screen.blit(revboat_img,(self.x,self.y))
    def move(self):
        self.x+=self.speed*self.direction*delta_B
        self.rect.x = self.x
        self.rect.y = self.y
duck = Duck()

def add_boat():
    if randint(1,2)==1:
        boat = Boat()
    else:
        boat = ReversedBoat()
    boats.append(boat)  
for i in range(6):
    add_boat()
    
while True:
    if level==2:
        image_address1 = os.path.join('images','ship.png')
        boat_img = pygame.image.load(image_address1).convert_alpha()
        image_address3 = os.path.join('images','revship.png')
        revboat_img = pygame.image.load(image_address3).convert_alpha()
        screen.fill((0,104,189))
    if level==1:
        screen.fill((135,206,250))
    
    for i in boats:
        if i.direction==1 and i.x>=770 or i.direction==-1 and i.x<=-70:
            boats.remove(i)
            delta_B+=0.01
            add_boat()
            if randint(1,10//level)==1:
                add_boat()
        if duck.x>=i.x-50 and duck.x<=i.x+50 and duck.y>=i.y-20 and duck.y<=i.y+20:
            emergency = True
            boatspeed = i.speed*delta_B*i.direction
        i.draw()
        i.move()
        i.rect.x = i.x
        i.rect.y = i.y
    if duck.x<0 or duck.x>700:
        pygame.quit()
        sys.exit()
    if duck.y<0 and level==1:
        level = 2
        duck.y = 700
        delta_d = 3
        boats = []
        for i in range(11):
            add_boat()
    if duck.y<0 and level==2:
        pygame.quit()
        sys.exit()
    duck.draw()
    duck.move()
    duck.rect.x = duck.x
    duck.rect.y = duck.y
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not emergency:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    duck.y+=20
                if event.key==pygame.K_UP:
                    duck.y-=20
                if event.key==pygame.K_RIGHT:
                    duck.x+=20
                if event.key==pygame.K_LEFT:
                    duck.x-=20
                
    pygame.display.flip()