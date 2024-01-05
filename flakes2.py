import pygame
import random
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock


#set up empty lists to hold x and y positions of flakes
xPositions = []
yPositions = []

#use a for loop to push random values into the x and y position lists
for i in range(50):
    xPositions.append(random.randrange(0, 500))
    yPositions.append(random.randrange(-500, 0))



while(1): #omg game lup---------
    clock.tick(60) #FPS
    
    #physics section----
    
    #move flakes
    for i in range(50):
         yPositions[i]+=1 #move down
         if yPositions[i]>500: #reset position if you go off the screen
            yPositions[i]=random.randrange(-200, 0)
                      

    #render section---
    screen.fill((0,0,0))
    
    for i in range(50):
        pygame.draw.circle(screen, (255, 255, 255), (xPositions[i], yPositions[i]), 3) #draw flakes
 
    
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()
