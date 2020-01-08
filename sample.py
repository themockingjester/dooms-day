import pygame
import time
import random
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((1240,600))
    state=True
    pygame.display.set_caption('Dooms Day')
    car1=pygame.image.load('car1.png')
    mummy=pygame.image.load('mummy.png')
    #alien=pygame.image.load('alien.png')

#mumx=random.randint(400,700)
    icon=pygame.image.load('car.png')
    road=pygame.image.load('road.png')
    pygame.display.set_icon(icon)
    roadx=0   #road's x coordinate

    time1=random.randint(0,1)                   #time1 provides time at which muumy arrives
    #time2=random.randint(0,200)     
    roady=-120                                          #road's y coordinate

    car1x=400                                               #car x coordinate
    car1y=400                                               #car y coordnate
    ctr=0                                          #counter which is responsible for road and car vibration
    ctr2=0                                          
    #ctr3=0
    countx=0
    mumx=set()                                                  #it holds the x coordinates of all mummies arriving at a time
    mumy=list()                                           #it holds the y coordinates of all mummies arriving at a time
    while state:                                #loop which makes application running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state=False
            #if event.type==pygame.KEYDOWN:
                
              
            
        if ctr2==time1:     #condition for calling mummies after time(time1)
            #############
            
            zombie_num=random.randint(1,5) 
            print("number of zombie",zombie_num)
            for i in range(0,zombie_num):
                temp=random.randint(400,700)
                mumx.add(temp)
            zombie_num=len(mumx)
            for i in range(0,zombie_num):
                temp=random.randint(-5,-1)
                mumy.append(temp)
            mumx=list(mumx)
            print("mumx", mumx)
            print("mumy", mumy)
            
        if ctr2>time1:
            new=0
            allgreat=0
            for (i,j) in zip(mumy,mumx):
                for m in mumy:
                    if m>=550:   #condition which checks if all mummies y coordinate are greater then 550 if yes then it means all mummies reached to ground
                        allgreat+=1
                    else:
                        break
                if allgreat==len(mumy): #if muumies reached to ground 
                    time1=random.randint(0,10)#againg setting new time for another mummy team
                    ctr2=0    
                    mumx.clear()
                    mumy.clear()
                    mumx=set()
                if i<550:     #condition for calling mummies after time(time1)
                        screen.blit(mummy,(j,i))
                                   #counter for calling mummies
                        
                        mumy[new]+=5
                        pygame.display.update()
                
                new+=1
                


            #############
            
        
        
        if ctr%2==0:                #condition for road and car vibration
            roady+=5
            car1y+=5
        else:
            roady-=5
            car1y-=5
        keys=pygame.key.get_pressed()       #for pressing keys for a longer period
        if keys[pygame.K_LEFT]:      #for pressing left key for a longer period
                    car1x-=38
        if keys[pygame.K_RIGHT]:    #for calling right key for a longer period
                    car1x+=38
        screen.blit(road,(roadx,roady))
        if car1x<350:          #limits the range of car
            car1x+=38
        if car1x>750:
            car1x-=38
        
        screen.blit(car1,(car1x,car1y))
        pygame.display.update()
        ctr+=1           #counter for vibrating the road and vehicle
        ctr2+=1
        
        #ctr3+=1       #counter for calling aliens
        
    pygame.quit()
main()
    
