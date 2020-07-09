import time
import pygame
import random
from pygame.rect import *
from pygame.locals import *
pygame.init()


screen_height=500
screen_width=500
blue=(0,0,255)
red=(255,0,0)
l_green=(0,150,0)
l_red=(150,0,0)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)
running=True
cgreen=l_green
cred=l_red



def pause():
    pause=pygame.display.set_mode((500,500))
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                paused=False
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==K_c:
                    paused=False

        message_display("The game is paused",xy=(20,20),screen=pause,fonti=60)
        message_display("hit c to continue",xy=(20,85),screen=pause,fonti=60)
        pygame.display.update()


def message_display(text,xy,screen,fonti=115,color=blue):
    font=pygame.font.SysFont(None,fonti,10,)
    img=font.render(text,True,color)
    screen.blit(img,xy)

clock=pygame.time.Clock()


def things(screen,x,y,w,h,color):
    thing=pygame.draw.rect(screen,color,[x,y,w,h])
    return thing

def crash(screen):
    screen.fill(black)
    message_display("you crashed",xy=(20,20),screen=screen)
    pygame.display.update()
    time.sleep(2)
    main()

def _dodged(count,screen):
    
    font=pygame.font.SysFont("freesanbold.ttf",25)
    img=font.render("Dodged="+str(count),True,blue)
    img2=font.render("hit p to pause",True,red)
    screen.blit(img,(0,0))
    screen.blit(img2,(0,30))
    pygame.display.update()
    # time.sleep(10)


def main():
    screen=pygame.display.set_mode((screen_height,screen_width))
    x = 180
    y = 450
    x_change = 0
    running=True
    q=False
    screen.fill(white)
    t_startx=random.randrange(0,screen_width)
    t_starty=-600
    _speed=10
    _width=100
    _height=100
    dodged=0
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 5
        if pressed[pygame.K_RIGHT]: x += 5
        if pressed[pygame.K_p]:pause()
        screen.fill(black)
        x+=x_change
        r0=pygame.draw.rect(screen,blue,Rect(x,y,100,450))
        r1=pygame.draw.rect(screen,red,(0,0,500,500),5)
        if x<=0 or x>=screen_width-105:
            crash(screen)
        clock.tick(60)

        thing=things(screen,t_startx,t_starty,_width,_height,white)
        if thing.colliderect(r0):
              crash(screen)

        t_starty+=_speed

        #_speed+=int(_speed*1.2)
        if t_starty>screen_height:
            t_starty=0-_height
            t_startx = random.randrange(0, screen_width)
            dodged+=1
            _speed+=1
        _dodged(dodged,screen=screen)
        clock.tick(60)
        pygame.display.update()

def intro():
    screen=pygame.display.set_mode((screen_height,screen_width))
    pygame.display.set_caption("Dodge box")
    introscreen=pygame.display.set_mode((500,500))
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                
        click=pygame.mouse.get_pressed()


        mouse = pygame.mouse.get_pos()

        if (100)<mouse[0]<(200) and (400)<mouse[1]<(450):
            cgreen=green
            if click[0]==1:
                main()

        else:
            cgreen=l_green
        if (300)<mouse[0]<(400) and 400<mouse[1]<450:
            cred=red
            if click[0]==1:
                pygame.quit()
                
        else:
            cred=l_red
        rg=pygame.draw.rect(introscreen,cgreen,(100,400,100,50))
        pygame.draw.rect(introscreen,cred, (300, 400, 100, 50))
        message_display("Dodge box",color=red,xy=(20,20),screen=screen)
        message_display("Developed by:",(20,170),fonti=55,color=(67,84,239),screen=screen)
        message_display("T Prajwal Prabhu", (20, 240), fonti=55, color=(67, 84, 239),screen=screen)
        message_display("Start",(120,420),screen=introscreen,fonti=20)
        message_display("Quit", (320, 420), screen=introscreen, fonti=20)
        pygame.display.update()
        

