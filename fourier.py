import pygame as pg
import math

# Pygame window init
pg.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 120
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

# Variables
running = True
dt = 0
angle = 0
wave_y = []
origin_x = SCREEN_WIDTH//2

while running:
    # Display fps
    pg.display.set_caption("FPS : " + str(round(clock.get_fps(), 2)))
    
    # Detect events
    for event in pg.event.get():
        # Exit when closing the window
        if event.type == pg.QUIT:
            running = False
            
    # Reset screen before rendering
    screen.fill("black")
    
            
    # Compute
    # Coordinates of the first circle
    x = (SCREEN_WIDTH//2) - 350
    y = SCREEN_HEIGHT//2
    
    # Angle : speed at which each point is turning
    angle -= dt * math.pi * 2
    
    # 
    for i in range(0, 1000):
        # Store the previous value to render on screen the previous circles and lines of an iteration
        prevx = x
        prevy = y
        
        # Square wave
        n = 2*i + 1
        radius = 75 * (4 / (n * math.pi)) #(n >= 0)
        
        """
        # Saw tooth wave
        # (n >= 1)
        n = i
        radius = 75 * (2 / (n * math.pi)) * (-1)**n
        """
        
        # Increment the position to have it moving
        x += radius * math.cos(n * angle)
        y += radius * math.sin(n * angle)
        
        # Render on screen
        pg.draw.circle(screen, 'white', (prevx, prevy), radius, 1) # Outline
        pg.draw.line(screen, 'white', (x, y), (prevx, prevy))      # Line (center to dot)
        pg.draw.circle(screen, 'white', (x, y), 3)                 # Dot
    
    # Put the y-value in an array to have the full wave being rendered
    wave_y.insert(0, y)
    
    # Draw a line from the last point of the epicycle to the first point in the array
    pg.draw.line(screen, 'white', (x,y), (SCREEN_WIDTH//2, wave_y[0]))
    
    # Iterate through the array to render it
    if len(wave_y) > 1:
        wave_x = origin_x
        for i in range(1, len(wave_y)):
            # Draw lines between to points on the wave to have it smoother
            pt1 = (wave_x + i, wave_y[i])
            pt2 = (wave_x + i - 1, wave_y[i-1])
            pg.draw.line(screen, 'white', pt1, pt2, 2)
    
    # Remove the excess data we don't see on screen
    if len(wave_y) > 650:
        wave_y.pop()
    
    pg.display.flip()
    dt = clock.tick(120) / 1000
    
    # Reset the angle when a full cycle has been completed
    if abs(angle) >= 2 * math.pi:
        angle = 0
        
pg.quit

