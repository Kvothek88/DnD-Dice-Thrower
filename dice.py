import pygame
import random
import time
import os
  
# initializing the constructor
pygame.init()

pygame.display.set_caption('D&D Dice Throw')

# screen resolution
res = (720,720)
  
# opens up a window
screen = pygame.display.set_mode(res)

screen_normal = (127,127,127)
screen_light = (193,193,193) 
tx_color = (0,0,0)
box_color = (50,50,50)
white = (255,255,255)
dark_gray = (70,70,70)
light_gray = (200,200,200)
  
width = screen.get_width()
height = screen.get_height()

tinyfont = pygame.font.SysFont('adobegothicstdkalin',30)
smallfont = pygame.font.SysFont('adobegothicstdkalin',37)
middlefont = pygame.font.SysFont('adobegothicstdkalin',35)
  

minus = smallfont.render('-' , True , tx_color)
plus = smallfont.render('+' , True , tx_color)
count = 1

d4Img = pygame.image.load(os.path.join('images', 'd4.png'))
d6Img = pygame.image.load(os.path.join('images','d6.png'))
d8Img = pygame.image.load(os.path.join('images','d8.png'))
d10Img = pygame.image.load(os.path.join('images','d10.png'))
d12Img = pygame.image.load(os.path.join('images','d12.png'))
d20Img = pygame.image.load(os.path.join('images','d20.png'))
d100Img = pygame.image.load(os.path.join('images','d100.png'))

x2stir = pygame.mixer.Sound(os.path.join('sounds', 'x2stir.wav'))
x3stir = pygame.mixer.Sound(os.path.join('sounds', 'x3stir.wav'))
x4stir = pygame.mixer.Sound(os.path.join('sounds', 'x4stir.wav'))
x5stir = pygame.mixer.Sound(os.path.join('sounds', 'x5stir.wav'))
x1hit = pygame.mixer.Sound(os.path.join('sounds', 'x1hit.wav'))
x2hit = pygame.mixer.Sound(os.path.join('sounds', 'x2hit.wav'))
x3hit = pygame.mixer.Sound(os.path.join('sounds', 'x3hit.wav'))
x4hit = pygame.mixer.Sound(os.path.join('sounds', 'x4hit.wav'))
x5hit = pygame.mixer.Sound(os.path.join('sounds', 'x5hit.wav'))


def d4_dice(x,y):
    screen.blit(d4Img, (x,y))

def d6_dice(x,y):
    screen.blit(d6Img, (x,y))

def d8_dice(x,y):
    screen.blit(d8Img, (x,y))

def d10_dice(x,y):
    screen.blit(d10Img, (x,y))

def d12_dice(x,y):
    screen.blit(d12Img, (x,y))

def d20_dice(x,y):
    screen.blit(d20Img, (x,y))

def d100_dice(x,y):
    screen.blit(d100Img, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, tx_color)
    return textSurface, textSurface.get_rect()

def message_display(text,text2,text3,size):
    largeText = pygame.font.SysFont('adobegothicstdkalin',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextSurf2, TextRect2 = text_objects(text2, tinyfont)
    TextSurf3, TextRect3 = text_objects(text3, middlefont)
    offset = TextSurf.get_height()
    TextRect.center = ((width/2),(height/2))
    TextRect2.center = ((width/2),(height/2+offset))
    TextRect3.center = ((width/2),(height/2-offset))
    if len(size) <= 6:
        pygame.draw.rect(screen,dark_gray,[width/2-100,height/2-100,200,200])
    elif 6 < len(size) <= 9:
        pygame.draw.rect(screen,dark_gray,[width/2-(len(size)-6)*12-100,height/2-100,200+(len(size)-6)*24,200])
    else:
        pygame.draw.rect(screen,dark_gray,[width/2-(len(size)-6)*13-100,height/2-100,200+(len(size)-6)*26,200])
    screen.blit(TextSurf, TextRect)
    screen.blit(TextSurf2, TextRect2)
    screen.blit(TextSurf3, TextRect3)
    pygame.display.update()
    time.sleep(4)
    game_loop()



def d_random(qty,typ):
    total = 0
    results = []
    for roll in range(qty):
        dice = random.randint(1,typ)
        results += [dice]
        total += dice
    return total, results
                
def count_up():
    global count
    count += 1
    dice_count = smallfont.render(str(count) + "d" , True , tx_color)
    screen.blit(dice_count, (width-700+85,height-50+3))
    pygame.display.update()

def count_down():
    global count
    if count > 1:
        count -= 1
    dice_count = smallfont.render(str(count) + "d" , True , tx_color)
    screen.blit(dice_count, (width-700+85,height-50+3))
    pygame.display.update()


def game_loop():
    while True:

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()
              
            if ev.type == pygame.MOUSEBUTTONDOWN:
                
                if width-699 <= mouse[0] <= width-611 and height-650 <= mouse[1] <= height-562:
                    if count == 1:
                        x1hit.play()
                    elif count == 2:
                        x2hit.play()
                    elif count == 3:
                        x3hit.play()
                    elif count == 4:
                        x4hit.play()
                    else:
                        x5hit.play()
                    x,y = d_random(count,4)
                    print(x,y)     
                    message_display(str(x),str(y),str(count)+"d4",y)               
                if width-581 <= mouse[0] <= width-493 and height-650 <= mouse[1] <= height-562:
                    if count == 1:
                        x1hit.play()
                    elif count == 2:
                        x2hit.play()
                    elif count == 3:
                        x3hit.play()
                    elif count == 4:
                        x4hit.play()
                    else:
                        x5hit.play()
                    x,y = d_random(count,6)
                    print(x,y)
                    message_display(str(x),str(y),str(count)+"d6",y)
                if width-463 <= mouse[0] <= width-375 and height-650 <= mouse[1] <= height-562:
                    if count == 1:
                        x1hit.play()
                    elif count == 2:
                        x2hit.play()
                    elif count == 3:
                        x3hit.play()
                    elif count == 4:
                        x4hit.play()
                    else:
                        x5hit.play()
                    x,y = d_random(count,8)
                    print(x,y)
                    message_display(str(x),str(y),str(count)+"d8",y)
                if width-345 <= mouse[0] <= width-257 and height-650 <= mouse[1] <= height-562:
                    if count == 1:
                        x1hit.play()
                    elif count == 2:
                        x2hit.play()
                    elif count == 3:
                        x3hit.play()
                    elif count == 4:
                        x4hit.play()
                    else:
                        x5hit.play()
                    x,y = d_random(count,10)
                    print(x,y)
                    message_display(str(x),str(y),str(count)+"d10",y)
                if width-227 <= mouse[0] <= width-139 and height-650 <= mouse[1] <= height-562:
                    if count == 1:
                        x1hit.play()
                    elif count == 2:
                        x2hit.play()
                    elif count == 3:
                        x3hit.play()
                    elif count == 4:
                        x4hit.play()
                    else:
                        x5hit.play()
                    x,y = d_random(count,12)
                    print(x,y)
                    message_display(str(x),str(y),str(count)+"d12",y)
                if width-109 <= mouse[0] <= width-21 and height-650 <= mouse[1] <= height-562:
                    x1hit.play()
                    x,y = d_random(count,20)
                    print(x,y)
                    message_display(str(x),str(y),str(count)+"d20",y)
                if width-699 <= mouse[0] <= width-611 and height-537 <= mouse[1] <= height-449:
                    x1hit.play()
                    x,y = d_random(count,100)
                    print(x,y)
                    message_display(str(x),str(y),str(count)+"d100",y)

                if width-526 <= mouse[0] <= width-502 and height-47 <= mouse[1] <= height-22:
                    count_up()
                    
                if width-698 <= mouse[0] <= width-674 and height-47 <= mouse[1] <= height-22:
                    count_down()
                    
        dice_count = smallfont.render(str(count) + "d" , True , tx_color)

        screen.fill((127,127,127))
        
    
        # if mouse is hovered on a button it
        # changes to lighter shade 
        #d4
        if width-699 <= mouse[0] <= width-611 and height-650 <= mouse[1] <= height-562:
            pygame.draw.rect(screen,screen_light,[width-699,height-650,88,88])
        else:
            pygame.draw.rect(screen,screen_normal,[width-699,height-650,88,88])
        #d6
        if width-581 <= mouse[0] <= width-493 and height-650 <= mouse[1] <= height-562:
            pygame.draw.rect(screen,screen_light,[width-581,height-650,88,88])  
        else:
            pygame.draw.rect(screen,screen_normal,[width-581,height-650,88,88])
        #d8
        if width-463 <= mouse[0] <= width-375 and height-650 <= mouse[1] <= height-562:
            pygame.draw.rect(screen,screen_light,[width-463,height-650,88,88]) 
        else:
            pygame.draw.rect(screen,screen_normal,[width-463,height-650,88,88])
        #d10
        if width-345 <= mouse[0] <= width-257 and height-650 <= mouse[1] <= height-562:
            pygame.draw.rect(screen,screen_light,[width-345,height-650,88,88]) 
        else:
            pygame.draw.rect(screen,screen_normal,[width-345,height-650,88,88])
        #d12
        if width-227 <= mouse[0] <= width-139 and height-650 <= mouse[1] <= height-562:
            pygame.draw.rect(screen,screen_light,[width-227,height-650,88,88]) 
        else:
            pygame.draw.rect(screen,screen_normal,[width-227,height-650,88,88])
        #d20
        if width-109 <= mouse[0] <= width-21 and height-650 <= mouse[1] <= height-562:
            pygame.draw.rect(screen,screen_light,[width-109,height-650,88,88])   
        else:
            pygame.draw.rect(screen,screen_normal,[width-109,height-650,88,88])
         #d100
        if width-699 <= mouse[0] <= width-611 and height-537 <= mouse[1] <= height-449:
            pygame.draw.rect(screen,screen_light,[width-699,height-537,88,88])
        else:
            pygame.draw.rect(screen,screen_normal,[width-699,height-537,88,88])


        d4_dice(width-692,height-643)
        d6_dice(width-575,height-644)
        d8_dice(width-457,height-644)
        d10_dice(width-341,height-644)
        d12_dice(width-225,height-648)
        d20_dice(width-109,height-650)
        d100_dice(width-695,height-533)

        #Dice number box
        pygame.draw.rect(screen,box_color,[width-700,height-50,200,30])

        if width-670 <= mouse[0] <= width-530 and height-50 <= mouse[1] <= height-20:
            if count == 1:
                pass
            elif count == 2:
                x2stir.play()
            elif count == 3:
                x3stir.play()
            elif count == 4:
                x4stir.play()
            else:
                x5stir.play()

        #Decrease button
        if width-698 <= mouse[0] <= width-674 and height-47 <= mouse[1] <= height-22:
            pygame.draw.rect(screen,light_gray,[width-698,height-47,24,24])
            
        else:
            pygame.draw.rect(screen,white,[width-698,height-47,24,24])      

        #Increase button
        if width-526 <= mouse[0] <= width-502 and height-47 <= mouse[1] <= height-22:
            pygame.draw.rect(screen,light_gray,[width-526,height-47,24,24])
            
        else:
            pygame.draw.rect(screen,white,[width-526,height-47,24,24])
        
        # superimposing the text onto the button
        screen.blit(minus , (width-698+7,height-52+3))
        screen.blit(plus , (width-526+5,height-53+3))
        screen.blit(dice_count, (width-700+85,height-50+3))
        pygame.display.update()

game_loop()
pygame.quit()
quit()
