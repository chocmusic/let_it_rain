import pygame
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Make it Rain")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# BOUNCING BALL CLASS CODE  

class Raindrops(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_pos, y_pos, y_speed, drop_size):  
    # Attributes of the bouncing ball 
        self.x_pos = x_pos
        self.y_pos = y_pos  
        self.y_speed = y_speed 
        self.drop_size = drop_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def falling(self, screen, colors, screen_width, screen_height):

        drop_color = (random.randint(0, 10), random.randint(0, 10), 255) # This is outside because of variable scoping.
        self.y_pos = self.y_speed
        
        if y_pos <= -500 + self.drop_size:
            y_speed = 0
 
        self.y_pos += self.y_speed 

        pygame.draw.circle(screen, drop_color, [self.x_pos, self.y_pos], self.drop_size)
		
#here is a change for github

# -------- Main Program Loop -----------
rain = Raindrops(350,250,10,2)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    screen.fill(GREY)
    drop_color=WHITE
    rain.falling(screen,drop_color,SCREEN_WIDTH,SCREEN_HEIGHT)
   
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


