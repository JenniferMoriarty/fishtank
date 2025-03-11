import pygame


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Farm Simulator")

# Colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (50, 50, 50)
BROWN = (80, 50, 0)

# Sidebar dimensions
sidebar_width = 150

# Plant classes
class Plant:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 15

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

#left side buttons for plants
cornx = 10
corny = 10
tomatox = 10
tomatoy = 50

# holds which plant we most recently clicked on
selected_plant = None

# Plant list
plants = []

def collision(bx, by, px, py): #bx, by is mouse, px, py is plant position
    print(bx, by, px, py)
    if bx > px and bx<px+30 and by>py and by<py+30: #simple bounding box collision
        return True
    else: 
        return False


running = True
while running: #game loop##########################################################

    #input/event section----------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT: #quit game if x is pressed
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN: #check if mouse clicked
            mouse_x, mouse_y = event.pos #grab position

            # Check if click is in the sidebar
            if mouse_x < sidebar_width:  # Sidebar range
                if collision(mouse_x, mouse_y, cornx, corny) == True:
                    selected_plant = YELLOW

                if collision(mouse_x, mouse_y, tomatox, tomatoy) == True:
                    selected_plant = RED
            
            #if not in sidebar, then plant something in field
            else:
                if selected_plant and mouse_x > sidebar_width:
                    # Plant the selected type in the field
                    plants.append(Plant(mouse_x, mouse_y, selected_plant))


    #render section--------------------------------------------------
    screen.fill(BROWN)  # Clear the screen

    pygame.draw.rect(screen, DARK_GRAY, (0, 0, sidebar_width, 600))  # Draw the sidebar

    pygame.draw.rect(screen, YELLOW, (cornx, corny, 30, 30))  # Corn button
    pygame.draw.rect(screen, RED, (tomatox, tomatoy, 30, 30))  # Tomato button

    # Draw all plants
    for plant in plants:
        plant.draw()

    pygame.display.flip()  # Update the display

pygame.quit()

