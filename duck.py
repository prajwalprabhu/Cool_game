import random
import pygame
from pygame.locals import *
import time
pygame.init()
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
screen_HEIGHT=370
screen_WIDTH=500

clock=pygame.time.Clock()
x=0
timer=0
def pause():
    pause=pygame.display.set_mode((500,370))
    paused=True
    while paused:
        img = pygame.image.load("img\intro.png")
        pause.blit(img,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                paused=False
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==K_c:
                    paused=False


        message("The game is paused",(20,20),60,RED,pause)
        message("hit c to continue",(20,85),screen=pause,size=60,color=RED)
        pygame.display.update()
def message(text,pos,size,color,screen):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    # screen.fill((0,0,0))
    screen.blit(img, pos)
    # pygame.display.update()

def backgruound(img,screen):
    global x
    screen.blit(img,(x,0))
    x-=1
    screen.blit(img,(x+937,0))
    if x<-937:
        x=0
    pygame.display.update()
def main(screen):
    count=0
    running = True
    y = 250
    timer=0
    y1 = random.randrange(0, 400)
    x = random.randrange(120, 400)
    while running:
            # screen.fill((0,0,0))
            bird = pygame.image.load(r"img\bird2.png")
            background=pygame.image.load(r"img\background2.png")
            # screen.blit(background, (0, 0))
            backgruound(background,screen)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    pygame.quit()
                   
            # if event.type==KEYDOWN:
            #     if event.key==K_UP:
            #         y-=5
            pressed=pygame.key.get_pressed()
            if pressed[K_UP]:y-=5
            if pressed[K_DOWN]:y+=5
            if pressed[K_p]:pause()
            block=blocks(x,y1,screen)

            if y>=333:
               crashed(screen)
            x-=1

            mouse = pygame.mouse.get_pos()

            bird=screen.blit(bird,(20,y))
            if x<0:
                crashed(screen)
            if y<=0 or y==370:
                crashed(screen)
            if bird.colliderect(block):
                count+=1
                y1 = random.randrange(0, 400)
                x = random.randrange(120, 400)

            message("Count={}".format(count),(20,20),30,GREEN,screen)
            message("hit c to pause",(20,55),30,GREEN,screen)
            
            pygame.display.update()
            #clock.tick(60)

def crashed(screen):
    display=pygame.display.set_mode((500,370))
    crashed=True
    img = pygame.image.load(r"img\dbackground.png")
    display.blit(img, (0, 0))

    while crashed:
        for event in pygame.event.get():
            if event.type==QUIT:
                crashed=False
                pygame.quit()
                
        message("YOU LOST",(20,20),110,RED,screen)
        pygame.draw.rect(display,RED,(250,185,100,50))
        message("RETRY",(255,190),40,BLUE,screen)
        pygame.draw.rect(display,RED,(250,245,100,50))
        message("QUIT",(255,255),40,BLUE,screen)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if 250<mouse[0]<350 and 185<mouse[1]<235:
            if click[0]:
                main(screen)
        if 250<mouse[0]<350 and 245<mouse[1]<295:
            if click[0]:
                crashed=False
                pygame.quit()
                
        pygame.display.update()


def intro():
    start=True
    screen=pygame.display.set_mode((screen_WIDTH,screen_HEIGHT))
    intro=pygame.display.set_mode((500,370))
    pygame.display.set_caption("Duck game")
    while start:
        img = pygame.image.load("img\intro.png")
        intro.blit(img,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                start=False
                pygame.quit()
                
            # print(event)
        pygame.draw.rect(intro,BLUE,(85,300,100,50))
        message("START", (90, 310), 40, RED,screen)
        pygame.draw.rect(intro,RED,(330,300,100,50))
        message("QUIT",(335,310),40,BLUE,screen)

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 85<mouse[0]<185 and 300<mouse[1]<350:
            if click[0]:
                main(screen)

        if 330<mouse[0]<430 and 300<mouse[1]<350:
            if click[0]:
                start=False
                pygame.quit()
                
        pygame.display.update()

def blocks(x,y1,screen):

    pygame.draw.rect(screen, RED, (x, y1, 20, 20))
    block=pygame.draw.rect(screen, RED, (x, y1, 20, 20))

    return block
    pygame.display.update()






