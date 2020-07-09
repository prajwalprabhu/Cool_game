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
yellow=(255,255,0)
l_yellow=(150,150,0)

running=True
cgreen=l_green
cred=l_red
cyellow=l_yellow

clock=pygame.time.Clock()
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
def things(x,y,w,h,color,screen):
    thing=pygame.draw.rect(screen,color,[x,y,w,h])
    return thing
def things1(x,y,w,h,color,screen):
    thing=pygame.draw.rect(screen,color,[x,y,w,h])
    return thing
def things2(x,y,w,h,color,screen):
    thing=pygame.draw.rect(screen,color,[x,y,w,h])
    return thing
def crash(c,screen):
    screen.fill(black)
    message_display("you crashed",xy=(20,20),screen=screen)
    pygame.display.update()
    time.sleep(5)
    if c==1:
        main(screen)
    elif c==2:
        medium_main(screen)
    elif c==3:
        hard_main(screen)
def _dodged(count,screen):
    font=pygame.font.SysFont("freesanbold.ttf",25)
    img=font.render("Dodged="+str(count),True,blue)
    img2=font.render("hit p to pause",True,blue)
    screen.blit(img,(0,0))
    screen.blit(img2,(0,30))
    pygame.display.update()
    # time.sleep(10)
def hard_main(screen):
    x = 180
    y = 450
    x_change = 0
    running=True
    q=False
    screen.fill(white)
    t_startx=random.randrange(0,screen_width)
    t1_startx = random.randrange(0, screen_width)
    t2_startx = random.randrange(0, screen_width)
    t3_startx = random.randrange(0, screen_width)
    t_starty=-600
    t1_starty = -600
    t2_starty = -600
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
            crash(3,screen)
        clock.tick(60)

        thing=things(t_startx,t_starty,_width,_height,white,screen)
        thing1=things1(t1_startx,t_starty,_width,_height,blue,screen)
        thing2= things1(t2_startx, t_starty , _width, _height,yellow,screen)
        if thing.colliderect(r0):
              crash(3,screen)
        if thing1.colliderect(r0):
            crash(3,screen)
        if thing2.colliderect(r0):
            crash(3,screen)
        t_starty+=_speed
        #_speed+=int(_speed*1.2)
        if t_starty>screen_height:
            t_starty=0-_height
            t_startx = random.randrange(0, screen_width)
            dodged+=1
            _width+=1

        if t2_starty > screen_height:
            t2_starty = 0 - _height
            t2_startx = random.randrange(0, screen_width)
            dodged += 1
        if t1_starty > screen_height:
            t1_starty = 0 - _height
            t1_startx = random.randrange(0, screen_width)
            dodged += 1

        _dodged(dodged,screen)
        clock.tick(60)
        pygame.display.update()
def medium_main(screen):
    x = 180
    y = 450
    x_change = 0
    running=True
    q=False
    screen.fill(white)
    t_startx=random.randrange(0,screen_width)
    t1_startx = random.randrange(0, screen_width)
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
            crash(2,screen)
        clock.tick(60)

        thing=things(t_startx,t_starty,_width,_height,white,screen)
        thing1=things1(t1_startx,t_starty+5,_width,_height,blue,screen)
        if thing.colliderect(r0):
            crash(2,screen)
        if thing1.colliderect(r0):
            crash(2,screen)
        t_starty+=_speed
        #_speed+=int(_speed*1.2)
        if t_starty>screen_height:
            t_starty=0-_height
            t_startx = random.randrange(0, screen_width)
            dodged+=1
        _dodged(dodged,screen)
        clock.tick(60)
        pygame.display.update()
def main(screen):

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
            crash(1,screen)
        clock.tick(60)

        thing=things(t_startx,t_starty,_width,_height,white,screen)
        if thing.colliderect(r0):
              crash(1,screen)
        t_starty+=_speed
        #_speed+=int(_speed*1.2)
        if t_starty>screen_height:
            t_starty=0-_height
            t_startx = random.randrange(0, screen_width)
            dodged+=1
        _dodged(dodged,screen)
        clock.tick(60)
        pygame.display.update()
def select(screen):
    pygame.init()
    introscreen = pygame.display.set_mode((500, 500))
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
                pygame.quit()
                

        click = pygame.mouse.get_pressed()

        mouse = pygame.mouse.get_pos()

        if 100 < mouse[0] <200 and 400<mouse[1]<450:
            cgreen = green
            if click[0] == 1:
                main(screen)

        else:
            cgreen = l_green
        if 350 < mouse[0] < 450 and 400<mouse[1]<450:
            cred = red
            if click[0] == 1:
                hard_main(screen)

        else:
            cred = l_red


        if 225 < mouse[0] < 325 and 400<mouse[1]<450:
            cyellow=yellow
            if click[0] == 1:
                medium_main(screen)
        else:
            cyellow=l_yellow
        rg = pygame.draw.rect(introscreen, cgreen, (100, 400, 100, 50))
        pygame.draw.rect(introscreen, cred, (350, 400, 100, 50))
        pygame.draw.rect(introscreen, cyellow, (225, 400, 100, 50))
        message_display("Dodge box", color=red,xy=(20,20),screen=introscreen)
        message_display("Select Level", (20, 170), fonti=55, color=(67, 84, 239),screen=introscreen)
        # message_display("T Prajwal Prabhu", (20, 240), fonti=55, color=(67, 84, 239))
        message_display("Easy", (120, 420), introscreen, 20)
        message_display("Hard", (370, 420), introscreen, 20)
        message_display("Medium", (245, 420), introscreen, 20)
        pygame.display.update()
def start():
    running=True
    introscreen=pygame.display.set_mode((500,500))
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Dodge box 2.0")
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=True
                pygame.quit()
                

        click=pygame.mouse.get_pressed()


        mouse = pygame.mouse.get_pos()

        if 100<mouse[0]<200and 400<mouse[1]<450:
            cgreen=green
            if click[0]==1:
                introscreen.fill(black)

                select(screen)
                #quit()
        else:
            cgreen=l_green
        if 300<mouse[0]<400and 400<mouse[1]<450:
            cred=red
            if click[0]==1:
                pygame.quit()
              
        else:
            cred=l_red
        rg=pygame.draw.rect(introscreen,cgreen,(100,400,100,50))
        pygame.draw.rect(introscreen,cred, (300, 400, 100, 50))

        message_display("Dodge box",color=red,screen=introscreen,xy=(20,20))
        message_display("Developed by:",(20,170),fonti=55,color=(67,84,239),screen=introscreen)
        message_display("T Prajwal Prabhu", (20, 240), fonti=55, color=(67, 84, 239),screen=introscreen)
        message_display("Start",(120,420),introscreen,20)
        message_display("Quit", (320, 420), introscreen, 20)
        pygame.display.update()

