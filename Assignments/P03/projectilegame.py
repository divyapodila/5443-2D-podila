# 2 player Samurai Game 
# Divya Podila
# M20315833

import pygame
from pygame import mixer
import math
import time


pygame.init()

# Defining variables initially
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Samurai GO SHOOT!!!!!!!!!')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('comicsansms.ttf', 24)
bg_img = pygame.image.load('C:/Users/divya/2Dgaming/Multiplayergame/All_images/Fight_Background.jpg').convert()
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
 
#Player1 on the screen
spriteload1 = pygame.image.load('C:/Users/divya/2Dgaming/Multiplayergame/All_images/startplayer1.png').convert()
spriteload1 = pygame.transform.scale(spriteload1,(180,180))
spriteload1.set_colorkey((0, 0, 0))
clock = pygame.time.Clock()

 #Player2 on the screen
spriteload2 = pygame.image.load('C:/Users/divya/2Dgaming/Multiplayergame/All_images/start_player2.png').convert()
spriteload2 = pygame.transform.scale(spriteload2,(180,180))
spriteload2.set_colorkey((0, 0, 0))
clock = pygame.time.Clock()

#Brick in between players
#Player1 on the screen
brickload = pygame.image.load('C:/Users/divya/2Dgaming/Multiplayergame/All_images/brick_image0000.jpg').convert()
brickload = pygame.transform.scale(brickload,(40,440))
spriteload1.set_colorkey((0, 0, 0))
clock = pygame.time.Clock()


pygame.mixer.set_num_channels(10)
#knifeimage load
sword_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/sword.png")

#killplayer image load
killplayer1_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/idied.png")

#killplayer image load
killplayer2_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/afterdeath_player2.png")

#Gameover imageload
gameover_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/gameover.png")

#victoryplayer1 image load
victory1_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/victoryplayer1.png")

#victoryplayer1 image load
victory2_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/victoryplayer2.png")

#gamestartplayer1movement
player1_img_up = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/sprite1_newest.png")

#gamestartplayer1movement
player2_img_up = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/player2_newese_new.png")

#throwplayer1movement
throwplayer1_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/throw_player1.png")

#throwplayer2movement
throwplayer2_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/throw_player2.png")

#wall hit 
wallhit_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/wallhit.png").convert()
wallhit_img = pygame.transform.scale(wallhit_img,(40,440))

#groundhit
groundhit_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/bomb_hit.png").convert()
groundhit_img = pygame.transform.scale(groundhit_img,(150,150))
groundhit_img.set_colorkey((0, 0, 0))

#before player dies
beforedie1_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/player1beforekill.png").convert()
beforedie1_img = pygame.transform.scale(beforedie1_img,(180,180))
beforedie1_img.set_colorkey((0, 0, 0))
beforedie2_img = pygame.image.load("C:/Users/divya/2Dgaming/Multiplayergame/All_images/player2beforekill.png").convert()
beforedie2_img = pygame.transform.scale(beforedie2_img,(180,180))
beforedie2_img.set_colorkey((0, 0, 0))
#defining color variables for board
score=0
colors = {
'bg' : (0,0,0)
}
lines = {
    'linecolor' : (255,255,255)
}

Player01 =''
Velocity01=''
Player02 =''
Velocity02=''
startpos1 =(110,500)
endpos1=(600,500)
startpos2 =(1095,510)
endpos2=(640,590)
width=2
radius1 = 485
radius2 = 455
theta=0

game_over = False
pygame.mixer.set_num_channels(10)

#env class
class Environment():
     def _init_(self):
        print("in init")

     def draw_board1():
        pygame.draw.rect(screen,colors['bg'], [0, 0, 200, 100], 0, 0)
        font = pygame.font.SysFont('comicsansms.ttf', 24)
        Player1_text = font.render(f'<<PLAYER 1>> {Player01}', True, 'RED')
        screen.blit(Player1_text, (40, 10))
        angle1_Text =font.render(f'Angle: {-theta}',True, 'white')
        screen.blit(angle1_Text, (10, 50))
        pass
    
     def draw_board2():
        pygame.draw.rect(screen,colors['bg'], [1000, 0, 200, 100], 0, 5)
        font = pygame.font.SysFont('comicsansms.ttf', 24)
        Player2_text = font.render(f'<<PLAYER 2>> {Player02}', True, 'RED')
        screen.blit(Player2_text, (1050, 10))
        angle2_Text =font.render(f'Angle: {-theta}', True, 'white')
        screen.blit(angle2_Text, (1010, 50))
        pass
        
     def toRadian(self,theta):
        return theta * math.pi / 180
 
     def toDegrees(self,theta):
        return theta * 180 / math.pi
     
     #draw aim1
     def drawline1(self,theta,startpos1):
        theta = self.toRadian(theta)
        x = startpos1[0] + radius1 * math.cos(theta)
        y = startpos1[1] + radius1 * math.sin(theta)
        pygame.draw.line(screen,lines['linecolor'],startpos1,(x,y),width)
        return theta
     
     #draw aim2
     def drawline2(self,theta,startpos2):
        theta = self.toRadian(theta)
        x = startpos2[0] - radius2 * math.cos(theta)
        y = startpos2[1] + radius2 * math.sin(theta)
        pygame.draw.line(screen,lines['linecolor'],startpos2,(x,y),width)
        return theta
     
     #throwknife
     def position_points(self,Xo,Yo,angle,intial_velocity):
        deltaT = 0.5
        gravity = 9.806
        Ynumerik = []
        Xnumerik = []
        Ttot = 0
        backwards = False
        voy= intial_velocity*math.sin(math.radians(angle))
        vox = intial_velocity*math.cos(math.radians(angle))
        
        if angle > 90:
            backwards = True
        while (Yo <= 580):
         
         ay = (-gravity)
         voy = voy + (ay*deltaT)
         if backwards == False:
            Xt = Xo + (vox*deltaT)
         else:
            Xt = Xo + (vox*deltaT)
         Yt = Yo - (voy*deltaT) 
         Yo = Yt
         Xo = Xt
         Ynumerik.append(Yo)
         Xnumerik.append(Xo)
         Ttot += deltaT
         if Ynumerik[-1] < 0:
            del Xnumerik[-1]
            del Ynumerik[-1]
        
        return Xnumerik,Ynumerik
      
            
        
env = Environment()
throw=False

#resetboard
def resetboard():
 screen.blit(bg_img,[0,0])
 screen.blit(player1_img_up,[10,470])
 screen.blit(player2_img_up,[1000,470])
 screen.blit(brickload,[600,365])
 Environment.draw_board1()


def resetboard11():
 screen.blit(bg_img,[0,0])
 screen.blit(player1_img_up,[10,470])
 screen.blit(player2_img_up,[1000,470])
 screen.blit(brickload,[600,365])
 Environment.draw_board2()
 
 
 #resetboardforthrow1
def resetboardthrow1():
 screen.blit(bg_img,[0,0])
 screen.blit(player2_img_up,[1000,470])
 screen.blit(brickload,[600,365])
 Environment.draw_board1()


#resetboardforthrow2
def resetboardthrow2():
 screen.blit(bg_img,[0,0])
 screen.blit(player1_img_up,[10,470])
 screen.blit(brickload,[600,365])
 Environment.draw_board2()

 #resetboardforplayer2
def resetboard2():
 screen.blit(bg_img,[0,0])
 screen.blit(spriteload1,[10,470])
 screen.blit(brickload,[600,365])
 Environment.draw_board1()

#resetboardafter player2dies
def resetboard3():
 screen.blit(bg_img,[0,0])
 screen.blit(spriteload1,[10,470])
 screen.blit(brickload,[600,365])
 screen.blit(killplayer2_img,[x,y])
 Environment.draw_board1()

#resetboardonesecondbeforekill
#resetboardafter player2dies
def resetboard5():
 screen.blit(bg_img,[0,0])
 screen.blit(spriteload1,[10,470])
 screen.blit(brickload,[600,365])
 Environment.draw_board1()
 screen.blit(beforedie2_img,[1000,470])
 pygame.display.flip()
 time.sleep(0.5)
 resetboard2()
 
 #resetboardafter player1dies
def resetboard6():
 screen.blit(bg_img,[0,0])
 screen.blit(spriteload2,[1000,470])
 screen.blit(brickload,[600,365])
 Environment.draw_board2()
 screen.blit(beforedie1_img,[10,470])
 pygame.display.flip()
 time.sleep(0.5)
 resetboard4()
 
 #player1_throw
def player1_throw():
 resetboardthrow1()
 screen.blit(throwplayer1_img,[10,470])
 pygame.display.flip()
 time.sleep(1)
 
#player2_throw
def player2_throw():
 resetboardthrow2()
 screen.blit(throwplayer2_img,[1000,470])
 pygame.display.flip()
 time.sleep(1)
    

#resetboardafter player1dies
def resetboard4():
 screen.blit(bg_img,[0,0])
 screen.blit(spriteload2,[1000,470])
 screen.blit(brickload,[600,365])
 screen.blit(killplayer1_img,[x,y])
 Environment.draw_board2()

def resetboard_wall1():
    screen.blit(bg_img,[0,0])
    screen.blit(player1_img_up,[10,470])
    screen.blit(player2_img_up,[1000,470])
    Environment.draw_board1()
    screen.blit(wallhit_img,[600,365])
    pygame.display.flip()
    time.sleep(0.5)
    resetboard()

def resetboard_wall2():
    screen.blit(bg_img,[0,0])
    screen.blit(player1_img_up,[10,470])
    screen.blit(player2_img_up,[1000,470])
    Environment.draw_board2()
    screen.blit(wallhit_img,[600,365])
    pygame.display.flip()
    time.sleep(0.5)
    resetboard()

def resetboard_ground(x1,y1):
    screen.blit(bg_img,[0,0])
    screen.blit(player1_img_up,[10,470])
    screen.blit(player2_img_up,[1000,470])
    Environment.draw_board1()
    screen.blit(brickload,[600,365])
    screen.blit(groundhit_img,[x1,y1])
    pygame.display.flip()
    time.sleep(0.5)
    resetboard()

def resetboard_ground2(x2,y2):
    screen.blit(bg_img,[0,0])
    screen.blit(player1_img_up,[10,470])
    screen.blit(player2_img_up,[1000,470])
    Environment.draw_board2()
    screen.blit(brickload,[600,365])
    screen.blit(groundhit_img,[x2,y2])
    pygame.display.flip()
    time.sleep(0.5)
    resetboard()

def victory1():
   screen.blit(victory1_img,[461,250])
   pygame.display.flip()
   time.sleep(2)
   resetboard3()
   screen.blit(gameover_img,[400,240])

def victory2():
   screen.blit(victory2_img,[461,250])
   pygame.display.flip()
   time.sleep(2)
   resetboard4() 
   screen.blit(gameover_img,[400,240]) 
   
def gameover():
   screen.blit(gameover_img,[310,310])
   pygame.display.flip()
   time.sleep(0.5)
   
#Main Game loop
run=True
clock=pygame.time.Clock()
#Background Music for Game
#Instantiate mixer
mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound("C:/Users/divya/2Dgaming/Multiplayergame/All_images/SamuraiSakeShowdown.mp3"))
player1_turn = True
resetboard()
pygame.draw.line(screen,lines['linecolor'],startpos1,endpos1,width)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over== True: 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    resetboard()
                    player1_turn= True
                    pygame.draw.line(screen,lines['linecolor'],startpos1,endpos1,width)

                    
        if(player1_turn == True):   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                 screen.blit(player1_img_up,[10,470])
                 resetboard()
                 if -90 < theta <= 0:
                    theta=theta-15
                    env.drawline1(theta,startpos1)
                    
                 else:
                    env.drawline1(0, startpos1) 
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                 resetboard()
                 if theta <= -15:
                    theta=theta+15
                    env.drawline1(theta, startpos1)  
                    
                 else:
                    env.drawline1(0, startpos1) 
        
        else:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    resetboard11()
                    if -90 < (theta) <= 0:
                        theta=(theta)-15
                        env.drawline2(theta,startpos2)
                       
                    else:
                        env.drawline2(0, startpos2) 
                
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        resetboard11()
                        if theta <= -15:
                           theta=(theta)+15
                           env.drawline2(theta,startpos2)  
                           
                        else:
                           env.drawline2(0,startpos2)
        
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_RETURN:
            walltouched,killplayer2,groundtouch, killplayer1 = False,False,False,False
            if(player1_turn== True):
                    
                    xlist,ylist = env.position_points(120,510,-theta,intial_velocity =95)
                    player1_throw()
                    for i in range(len(xlist)):
                       x,y = xlist[i],ylist[i]
                       
                       screen.blit(sword_img,[x,y])
                       
                       pygame.mixer.Channel(1).play(pygame.mixer.Sound("C:/Users/divya/2Dgaming/Multiplayergame/images/Sword_Hit.mp3"))
                    
                       pygame.display.flip()
                       time.sleep(0.04)
                       resetboard()
                       if x > 1190 or x < 16 or y > 790 or y < 16:
                            break
                        
                       if x >= 570 and x <= 620 and y >= 300:
                            walltouched = True
                            resetboard_wall1()
                            break
                       elif x>960 and x < 1200 and y>470: 
                            killplayer2 = True
                            pygame.mixer.Channel(2).play(pygame.mixer.Sound("C:/Users/divya/2Dgaming/Multiplayergame/All_images/mandies.mp3"))
                            resetboard2()
                            resetboard5()
                            screen.blit(killplayer2_img,[x,y])
                            victory1()
                            game_over=True
                            break
   
                       elif y==ylist[-1] and x<960:
                           
                            groundtouch=True
                            pygame.mixer.Channel(3).play(pygame.mixer.Sound("C:/Users/divya/2Dgaming/Multiplayergame/All_images/explode.mp3"))
                            resetboard_ground(x,y)    
                            break
                           
                    player1_turn = False  
                    if killplayer2 == False:
                        env.drawline2(0,startpos2)
                    theta=0
            else:
               
                pygame.display.update()
                xlist,ylist = env.position_points(1000,500,theta -180 ,intial_velocity =95)  
                player2_throw()       
                for i in range(len(xlist)):
                           x,y = xlist[i],ylist[i]
                           screen.blit(sword_img,[x,y])
                           mixer.init()
                           pygame.mixer.Channel(4).play(pygame.mixer.Sound("C:/Users/divya/2Dgaming/Multiplayergame/Sword_Hit.mp3"))
                        
                           pygame.display.flip()
                           time.sleep(0.04)
                           resetboard11()
                           if x > 1190 or x < 16 or y > 790 or y < 16:
                                break

                           if x >= 570 and x <= 620 and y >= 300:
                                walltouched = True
                                resetboard_wall2()
                                break
                           elif x > 5 and x < 140 and y > 470: 
                                print("rasd",1200 - radius1 - radius2 - 30)
                                killplayer1 = True
                                mixer.init()
                                pygame.mixer.Channel(5).play(pygame.mixer.Sound("C:/Users/divya/2Dgaming/Multiplayergame/All_images/mandies.mp3"))
                                
                                resetboard4()
                                resetboard6()
                                screen.blit(killplayer1_img,[x,y])
                                victory2()
                                
                                game_over=True

                                break
                           elif y==ylist[-1] and x<590:
                              
                                groundtouch=True
                                pygame.mixer.Channel(6).play(pygame.mixer.Sound("C:/Users/divya/2Dgaming/Multiplayergame/All_images/explode.mp3"))
                                #Set preferred volume
                                resetboard_ground2(x,y)
                                
                                break 
                
                player1_turn = True 
                 
                if killplayer1 == False:
                    env.drawline1(0,startpos1)
                theta=0
    pygame.display.update()
    pygame.display.flip()   
    clock.tick(60)           
pygame.quit()  

