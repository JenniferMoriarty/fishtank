import pygame
import random
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

#----------------------------class snowflake------------------------------------------
class Snowflake:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
    def move(self):
        self.xpos += random.randrange(-2, 3)
        self.ypos += random.randrange(0, 3)
        if self.ypos >500:
            self.ypos = random.randrange(-200, 0)
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.xpos, self.ypos), 3) #draw flakes

#----------------------------------------------------------------------


#create a bunch of snowflakes
flakeBag = []
for i in range(500):
    flakeBag.append(Snowflake(random.randrange(0, 500), random.randrange(-500, 0)))


while(1): #omg game lup---------
    clock.tick(60) #FPS
    
    #physics section----
    
    #move flakes
    for i in range(len(flakeBag)):
        flakeBag[i].move()
         
                      

    #render section---
    screen.fill((0,0,0))
    
    for i in range(len(flakeBag)):
        flakeBag[i].draw()
 
    
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()
