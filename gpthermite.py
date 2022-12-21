#python
#create software 
#create software to draw cubic hermite graphs
#user can click on a gui plane to determine points and tangents
#program will draw cubic hermite graph

import pygame
import math

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()

# Define some variables
points = []
tangents = []

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.MOUSEBUTTONDOWN:
            # User pressed down on a mouse button
            pos = pygame.mouse.get_pos()
            points.append(pos)
            print ("Point:", pos)
            textPrint.print(screen, "Point: " + str(pos))

        if event.type == pygame.MOUSEMOTION:
            # User moved the mouse
            pos = pygame.mouse.get_pos()
            tangents.append(pos)
            print ("Tangent:", pos)
            textPrint.print(screen, "Tangent: " + str(pos))
        
    
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Draw a graph
    for point in points:
        pygame.draw.circle(screen, BLACK, point, 5)
    for tangent in tangents:
        pygame.draw.circle(screen, BLACK, tangent, 5)

    # Draw cubic hermite graph
    if len(points) >= 2:
        try:
            x1, y1 = points[0]
            x2, y2 = points[1]
            xa, ya = tangents[0]
            xb, yb = tangents[1]
            for x in range(x1, x2+1):
                t = (x-x1) / (x2-x1)
                f_t = (2*t**3 - 3*t**2 + 1)
                m_t = (t**3 - 2*t**2 + t)
                g_t = (-2*t**3 + 3*t**2)
                n_t = (t**3 - t**2)
                y = f_t*y1 + m_t*(x2-x1)*ya + g_t*y2 + n_t*(x2-x1)*yb
                pygame.draw.circle(screen, BLACK, (x, int(y)), 2)
        except:
            pass
    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()