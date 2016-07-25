from __future__ import division
import pygame
import time
import random
pygame.init()
white=(255,255,255)
brown=(94,78,78)
light_red=(255,0,0)
blue4=(0,0,204)
black=(0,0,0)
yellow=(200,200,0)
yellow3=(255,255,102)
orange=(255,153,0)
green1=(10,128,0)
red=(200,0,0)
light_green=(0,255,0)
green=(85,107,47)
blue=(25,25,112)
yellow2=(204,204,0)
blue2=(0,178,238)
pale2=(240,230,140)
pale=(238,232,170)
blue3=(202,255,255)
dark_green=(0,102,0)
purple1=(171,130,255)
light_yellow=(255,255,0)
voilet=(60,180,220)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((800,600))
maroon=(188,0,0)
grass1=pygame.image.load('grass1.png')
back=pygame.image.load('back.jpg')
game_image=pygame.image.load('game.jpg')
grass2=pygame.image.load('grass2.png')
grass3=pygame.image.load('grass3.png')
grass4=pygame.image.load('grass4.png')
cloud=pygame.image.load('cloud2.png')
tank_image=pygame.image.load('tank.png')
intro_image=pygame.image.load('intro.jpg')
pygame.display.set_caption('Tanks')

fire_sound=pygame.mixer.Sound('fire2.wav')
explode_sound=pygame.mixer.Sound('explode2.wav')

clock=pygame.time.Clock()
mainTankX=display_width*0.9
mainTankY=display_height*0.9
tankWidth=40
tankHeight=20
turretWidth=5
ground_height=35
wheelWidth=5
smallfont=pygame.font.SysFont("Xacto Blade.ttf",25)
mediumfont=pygame.font.Font("Gagalin-Regular.otf",30)
largefont=pygame.font.Font("Gagalin-Regular.otf",80)
extralarge=pygame.font.SysFont("comicsansms",120)
def text_objects(text,color,size):
    if size=="small":
       textSurface=smallfont.render(text,True,color)
    elif size=="medium":
       textSurface=mediumfont.render(text,True,color)
    elif size=="large":
       textSurface=largefont.render(text,True,color)
    elif size=="extralarge":
       textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
     textSurf,textRect=text_objects(msg,color,size)
     textRect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
     gameDisplay.blit(textSurf,textRect)
def message_to_screen(msg,color,y_displace=0,size="small"):
     textSurface,textRect=text_objects(msg,color,size)
     textRect.center=(display_width/2),(display_height/2)+y_displace
     gameDisplay.blit(textSurface,textRect)
def tank(x,y,turPos):
    x=int(x)
    y=int(y)
    possibleTurrets=[(x-27,y-2),
                     (x-26,y-5),
                     (x-25,y-8),
                     (x-23,y-12),
                     (x-20,y-14),
                     (x-18,y-15),
                     (x-15,y-17),
                     (x-13,y-19),
                     (x-11,y-21)]
    
    


    
    pygame.draw.circle(gameDisplay,maroon,(x,y),int(tankHeight/2))
    pygame.draw.rect(gameDisplay,maroon,(x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(gameDisplay,maroon,(x,y),possibleTurrets[turPos],turretWidth)
    pygame.draw.circle(gameDisplay,red,(x-15,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,red,(x-10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,red,(x-5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,red,(x-0,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,red,(x+5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,red,(x+10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,red,(x+15,y+20),wheelWidth)
    return possibleTurrets[turPos]
def enemy_tank(x,y,turPos):
    x=int(x)
    y=int(y)
    possibleTurrets=[(x+27,y-2),
                     (x+26,y-5),
                     (x+25,y-8),
                     (x+23,y-12),
                     (x+20,y-14),
                     (x+18,y-15),
                     (x+15,y-17),
                     (x+13,y-19),
                     (x+11,y-21)]
    
    


    
    pygame.draw.circle(gameDisplay,pale,(x,y),int(tankHeight/2))
    pygame.draw.rect(gameDisplay,pale,(x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(gameDisplay,pale,(x,y),possibleTurrets[turPos],turretWidth)
    pygame.draw.circle(gameDisplay,pale2,(x-15,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,pale2,(x-10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,pale2,(x-5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,pale2,(x-0,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,pale2,(x+5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,pale2,(x+10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,pale2,(x+15,y+20),wheelWidth)
    return possibleTurrets[turPos]
        
def game_controls():
       gcont=True

       while gcont:
              for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       pygame.quit()
                       quit()
                       
                
              gameDisplay.fill(voilet)
 
             
              message_to_screen("Controls",light_green,-100,"large")
              message_to_screen("Fire:Spacebar",blue,20,"medium" )
              message_to_screen("Move turret:Up and Down arrows",blue,90,"medium" )
              message_to_screen("Move tank:Left and right arrows",blue,140,"medium" )
              message_to_screen("Increase Power:Press D",red,180,"medium")
              
             
              
              button("Play",150,500,100,50,green,light_green,action="play")
              button_back("Back",350,500,100,50,yellow,light_yellow,action="back")
              button("Quit",550,500,100,50,red,light_red,action="quit")
              pygame.display.update()
              
              clock.tick(15)

def button_back(text,x,y,width,height,inactive_color,active_color,action=None):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+width>cur[0]>x and y+height>cur[1]>y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="back":
                game_intro()
    else:
       pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height)
def button(text,x,y,width,height,inactive_color,active_color,action=None):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+width>cur[0]>x and y+height>cur[1]>y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="quit":
             pygame.quit()
             quit()
            if action=="controls":
               game_controls()
            if action=="play":
               gameLoop()
            
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height)
    
        
def pause():
       paused=True
       message_to_screen("Paused",blue2,-100,size="large")
       message_to_screen("Press C to continue and Q to quit",black,25)
       pygame.display.update()
       while paused:
              for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_c:
                            paused=False
                     elif event.key==pygame.K_q:
                            pygame.quit()
                            quit()
              #gameDisplay.fill(white)
              
              clock.tick(5)
def barrier(xlocation,randomHeight,barrierWidth):

    pygame.draw.rect(gameDisplay,brown,[xlocation,display_height-randomHeight,barrierWidth,randomHeight])

def explosion(x,y,size=50):
    pygame.mixer.Sound.play(explode_sound)
    explode=True
    while explode:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        startPoint=x,y
        colorChoices=[red,yellow2,yellow3,orange,yellow]
        magnitude=1
        while magnitude<size:
            exploding_bit_x=x+random.randrange(-1*magnitude,magnitude)
            exploding_bit_y=y+random.randrange(-1*magnitude,magnitude)
            pygame.draw.circle(gameDisplay,colorChoices[random.randrange(0,4)],(exploding_bit_x,exploding_bit_y),20)
            magnitude+=1
            pygame.display.update()
            clock.tick(150)
        explode=False
            
def fireShell2(xy,tankX,tankY,currentTurPos,gun_power,xlocation,barrierWidth,randomHeight,enemytankx,enemytanky):
    pygame.mixer.Sound.play(fire_sound)
    enemy_damage=0
    fire=True
    startingShell=list(xy)
    while fire:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()
               quit()
        pygame.draw.circle(gameDisplay,blue4,(startingShell[0],startingShell[1]),5)
       
        startingShell[0]-=(12-currentTurPos)*2
        gun_power2=float(gun_power/50)
        startingShell[1]+=int((((startingShell[0]-xy[0])*0.015/gun_power2)**2-(currentTurPos+currentTurPos/(12-currentTurPos))))
        if startingShell[1]>display_height-ground_height:
   
           hit_x=int((startingShell[0]*display_height-ground_height)/startingShell[1])
           hit_y=int(display_height-ground_height)
           
           explosion(hit_x,hit_y)
           if enemytankx+10>hit_x>enemytankx-10:
              #print("Critical hit")
              
              enemy_damage=25
           elif enemytankx+15>hit_x>enemytankx-15:
              #print("Hard hit")
              enemy_damage=18
           elif enemytankx+25>hit_x>enemytankx-25:
               #print("Medium Hit")
               enemy_damage=10
           elif enemytankx+35>hit_x>enemytankx-35:
               #print("Slight Hit")
               enemy_damage=5
            
           fire=False
        check_x_1=startingShell[0]<=xlocation+barrierWidth
        check_x_2=startingShell[0]>=xlocation
        check_y_1=startingShell[1]<=display_height
        check_y_2=startingShell[1]>=display_height-randomHeight
        if check_x_1 and check_x_2 and check_y_1 and check_y_2:

           hit_x=int(startingShell[0])
           hit_y=int(startingShell[1])
        
           explosion(hit_x,hit_y)
           fire=False
        pygame.display.update()
        clock.tick(60)
        
    return enemy_damage

def enemy_fireShell2(xy,tankX,tankY,currentTurPos,gun_power,xlocation,barrierWidth,randomHeight,ptankx,ptanky):
    pygame.mixer.Sound.play(fire_sound)
    damage=0
    currentPower=1
    power_found=False
    while not power_found:
        currentPower+=5
        if currentPower>100:
            power_found=True

        fire=True
        startingShell=list(xy)
        while fire:
            for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   pygame.quit()
                   quit()
            #pygame.draw.circle(gameDisplay,green,(startingShell[0],startingShell[1]),5)
           
            startingShell[0]+=(12-currentTurPos)*2
            gun_power2=float(currentPower/50)
            startingShell[1]+=int((((startingShell[0]-xy[0])*0.015/gun_power2)**2-(currentTurPos+currentTurPos/(12-currentTurPos))))
            if startingShell[1]>display_height-ground_height:
               hit_x=int((startingShell[0]*display_height-ground_height)/startingShell[1])
               hit_y=int(display_height-ground_height)
               #explosion(hit_x,hit_y)
               if ptankx+15>hit_x>ptankx-15:
                   #print("target acquired")
                   power_found=True 
               fire=False
            check_x_1=startingShell[0]<=xlocation+barrierWidth
            check_x_2=startingShell[0]>=xlocation
            check_y_1=startingShell[1]<=display_height
            check_y_2=startingShell[1]>=display_height-randomHeight
            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
               hit_x=int(startingShell[0])
               hit_y=int(startingShell[1])
               #explosion(hit_x,hit_y)
               fire=False


    fire=True
    startingShell=list(xy)
    while fire:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()
               quit()
        pygame.draw.circle(gameDisplay,green,(startingShell[0],startingShell[1]),5)
       
        startingShell[0]+=(12-currentTurPos)*2
        gun_power3=random.randrange(int(currentPower*0.90),int(currentPower*1.20))
        gun_power2=float(gun_power3/50)
        startingShell[1]+=int((((startingShell[0]-xy[0])*0.015/gun_power2)**2-(currentTurPos+currentTurPos/(12-currentTurPos))))
        if startingShell[1]>display_height-ground_height:
           hit_x=int((startingShell[0]*display_height-ground_height)/startingShell[1])
           hit_y=int(display_height-ground_height)
           explosion(hit_x,hit_y)
           if ptankx+15>hit_x>ptankx-15:
              #print("mujhe lagi  zada zor se")
              damage=25
           elif ptankx+15>hit_x>ptankx-15:
              #print("mujhe lagi zor se")
              damage=18
           elif ptankx+25>hit_x>ptankx-25:
              #print("mujhe zada ni lagi")
              damage=10
           elif ptankx+35>hit_x>ptankx-35:
              #print("mujhe zara si lagi")
              damage=5
           fire=False
        check_x_1=startingShell[0]<=xlocation+barrierWidth
        check_x_2=startingShell[0]>=xlocation
        check_y_1=startingShell[1]<=display_height
        check_y_2=startingShell[1]>=display_height-randomHeight
        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
           hit_x=int(startingShell[0])
           hit_y=int(startingShell[1])
           explosion(hit_x,hit_y)
           fire=False
        pygame.display.update()
        clock.tick(60)
    return damage;

def power(level):
    text=mediumfont.render("Power:"+str(level)+"%",True,white)
    gameDisplay.blit(text,[display_width/2-50,0])
def game_over():
       game_over=True

       while game_over:
              for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       pygame.quit()
                       quit()
              gameDisplay.blit(game_image,[15,10])
 
             
              message_to_screen("Game Over",green,-80,"large")
              message_to_screen("You lose:(",blue,-20,"medium" )
              
             
              
              button("Play again",150,500,100,50,green,light_green,action="play")
              button("Controls",350,500,100,50,yellow,light_yellow,action="controls")
              button("Quit",550,500,100,50,red,light_red,action="quit")
              
              


              








              pygame.display.update()
              
              clock.tick(15)

def game_win():
       win=True

       while win:
              for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       pygame.quit()
                       quit()
              gameDisplay.fill(white)
 
             
              message_to_screen("You win",green,-100,"large")
              message_to_screen("Destroyed:(",blue,-30,"medium" )
              
             
              
              button("Play again",150,500,100,50,green,light_green,action="play")
              button("Controls",350,500,100,50,yellow,light_yellow,action="controls")
              button("Quit",550,500,100,50,red,light_red,action="quit")
              
              


              








              pygame.display.update()
              
              clock.tick(15)

    
def game_intro():
       
       intro=True

       while intro:
              for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       pygame.quit()
                       quit()
                       
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key==pygame.K_c:
                        intro=False
              gameDisplay.blit(intro_image,[0,0])
              gameDisplay.blit(tank_image,[0,290])
 
             
              message_to_screen("Welcome to Tanks",green,-180,"large")
              message_to_screen("Destroy the enemy tank before it destroys you:)",blue,-50,"medium" )
              
             
              
              button("Play",150,500,100,50,green,light_green,action="play")
              button("Controls",350,500,100,50,yellow,light_yellow,action="controls")
              button("Quit",550,500,100,50,red,light_red,action="quit")
              
              


              








              pygame.display.update()
              
              clock.tick(15)
def health_bars(player_health,enemy_health):
    
    if player_health>75:
        player_health_color=dark_green
    elif player_health>50:
        player_health_color=light_yellow
    else:
        player_health_color=red
        
    if enemy_health>75:
        enemy_health_color=dark_green
    elif enemy_health>50:
        enemy_health_color=light_yellow
    else:
        enemy_health_color=red

    pygame.draw.rect(gameDisplay,player_health_color,(680,25,player_health,25))
    pygame.draw.rect(gameDisplay,enemy_health_color,(20,25,enemy_health,25))
    
    
    
def gameLoop():
    xlocation=(display_width/2)+random.randint(-0.2*display_width,0.2*display_width)
    barrierWidth=50
    randomHeight=random.randrange(display_height*0.1,display_height*0.6)
    gameExit=False
    gameOver=False
    FPS=15
    player_health=100
    enemy_health=100
    mainTankX=display_width*0.9
    mainTankY=display_height*0.9
    tankMove=0
    currentTurPos=0
    changeTur=0
    enemyTankX=display_width*0.1
    enemyTankY=display_height*0.9
    enemyTankMove=0
    




    
    fire_power=50
    power_change=0
   
    while not gameExit:
       
       if gameOver==True:
            message_to_screen("Game over",purple1,y_displace=-50,size="extralarge")
            message_to_screen("Press C to play again and Q to quit",blue3,50,size="medium")
            pygame.display.update()
       while gameOver==True:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       gameOver=False
                       gameExit=True
                       
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
    

        
       for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                   tankMove=-5
                elif event.key==pygame.K_RIGHT:
                   tankMove=+5
                elif event.key==pygame.K_UP:
                   changeTur=1
                elif event.key==pygame.K_DOWN:
                   changeTur=-1
                elif event.key==pygame.K_p:
                    pause()
                elif event.key==pygame.K_SPACE:
                    #fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power)
                    damage1=fireShell2(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,barrierWidth,randomHeight,enemyTankX,enemyTankY)
                    enemy_health-=damage1;
                    possibleMovement=['f','r']
                    moveIndex=random.randrange(0,2)
                    for x in range(random.randrange(0,10)):
                        if display_width*0.3>enemyTankX>display_width*0.03:
                            if possibleMovement[moveIndex]=="f":
                                enemyTankX+=5
                            elif possibleMovement[moveIndex]=="r":
                                enemyTankX-=5
            
                                gameDisplay.fill(blue)
                                health_bars(player_health,enemy_health)
                                gun=tank(mainTankX,mainTankY,currentTurPos)
                                enemy_gun=enemy_tank(enemyTankX,enemyTankY,8)
                                fire_power+=power_change
                                power(fire_power)
                                   
                                barrier(xlocation,randomHeight,barrierWidth)
                                
                                gameDisplay.fill(light_green,rect=[0,display_height-ground_height,display_width,ground_height])
                                gameDisplay.blit(cloud,[0,50])
                                gameDisplay.blit(grass1,[0,510])
                                gameDisplay.blit(grass4,[300,522])
                                gameDisplay.blit(grass3,[450,520])
                                gameDisplay.blit(grass2,[700,520]) 
                                
                                pygame.display.update()
                                clock.tick(FPS)
                        
                     


                    
                    damage=enemy_fireShell2(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,barrierWidth,randomHeight,mainTankX,mainTankY)
                    player_health-=damage;
                    
                elif event.key==pygame.K_a:
                    power_change-=1
                elif event.key==pygame.K_d:
                    power_change+=1
                    
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    tankMove=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    changeTur=0
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    power_change=0
       
       mainTankX+=tankMove

       currentTurPos+=changeTur
       if(currentTurPos>8):
           currentTurPos=8
       elif currentTurPos<0:
           currentTurPos=0
       if mainTankX-(tankWidth/2)<xlocation+barrierWidth:
            mainTankX+=5
            
       gameDisplay.fill(blue)
       health_bars(player_health,enemy_health)
       gun=tank(mainTankX,mainTankY,currentTurPos)
       enemy_gun=enemy_tank(enemyTankX,enemyTankY,8)
       fire_power+=power_change
       power(fire_power)
       
       barrier(xlocation,randomHeight,barrierWidth)
       gameDisplay.fill(light_green,rect=[0,display_height-ground_height,display_width,ground_height])
       gameDisplay.blit(cloud,[0,0])
       gameDisplay.blit(grass1,[0,510])
       gameDisplay.blit(grass4,[300,522])
       gameDisplay.blit(grass3,[450,520])
       gameDisplay.blit(grass2,[700,520])
       pygame.display.update()
       if player_health<1:
           game_over()
       elif enemy_health<1:
           game_win()
       clock.tick(FPS)
    
    pygame.quit()
    quit()
game_intro()
gameLoop()

 

       
