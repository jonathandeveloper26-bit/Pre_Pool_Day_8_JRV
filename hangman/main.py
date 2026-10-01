# Task 3.1: Install the pygame package. Then create a 'hangman' folder.
# Answer: Done

# Task 3.2: At the root of your hangman folder, create a main.py program to:
# ✓ import and initialize the pygame package;
# ✓ set up apygame window having width = height = 600 px.
# Run your program, a window should briefly appear then disappear

import pygame
import os



# Task 3.3: Add a loop to your main.py in order to:
# ✓ keep running if nothing happens;
# ✓ look for some pygame events;
# ✓ close the window if the user clicks on its specific button.
# Run your program, the window should stay unless you manually close it.

# Task 3.4: Browse the web to find a nice background image.
# Download it inside an appropriate folder.
# Then, modify your main.py program to:
# ✓ load this background image inside the game;
# ✓ blit the loaded image to the window;
# ✓ display the window with the image.
# Run your program to check if you did it right

# Task 3.5: Inside your main.py, create a function that draws a stickman inside the game window
### Note to self, (0,0) is the top left corner
def draw_stickman(surface, x, y):
    # Head
    pygame.draw.circle(surface,"black", (x,y-10),10,width= 2)
    # Neck
    pygame.draw.line(surface,"black", (x, y),(x, y+15), width=2)
    # Shoulder
    pygame.draw.line(surface, "black", (x+25, y+15), (x-25, y+15), width=2)
    # left arm
    pygame.draw.line(surface, "black", (x+25, y+15),(x+35, y+40), width=2)
    # right arm
    pygame.draw.line(surface, "black", (x-25, y+15), (x-35, y+40), width=2)
    # torso/waist
    pygame.draw.line(surface, "black", (x, y+15), (x, y+45), width=2)
    # left leg
    pygame.draw.line(surface, "black", (x,y+45), (x+10, y+80), width=2)
    # right leg
    pygame.draw.line(surface, "black", (x, y+45), (x-10, y+80), width=2)    

pygame.init()
screen = pygame.display.set_mode((1280,720))
bg_image = pygame.image.load(os.path.abspath("/mnt/c/Users/Jonathan Vinton/Desktop/Epitech/Course_learning/Pre_Pool_Day_8_JRV/hangman/background_img.jpg"))
bg_image = pygame.transform.scale(bg_image,(1280,720))
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    screen.blit(bg_image,(0,0))
    draw_stickman(screen, 1280//2, 720//2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    
