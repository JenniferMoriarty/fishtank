import pygame
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock


#set up variables for flake 1 position
flake1x = 20
flake1y = -100 #start above the screen

#set up variables for flake 2 position
flake2x = 300
flake2y = -50

while(1): #omg game lup---------
    clock.tick(60) #FPS
    
    #physics section----
    
    #move flakes
    flake1y+=2 #this one moves faster
    flake2y+=1
    
    #reset flakes to top of screen
    if flake1y > 500:
        flake1y = -100
    if flake2y > 500:
        flake2y = -50
    
    
    
    #render section---
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (255, 255, 255), (flake1x, flake1y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake2x, flake2y), 3)
    
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()
