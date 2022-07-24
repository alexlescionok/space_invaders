'''
YouTube video: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=10s - ended on 20:32
PyGame website: https://www.pygame.org/news
Icons: https://www.flaticon.com/
'''

import pygame

# Initialise the pygame
pygame.init()

##### SET UP GAME WINDOW
# Create a screen for our game - set the size for height, width - both in pixels
screen = pygame.display.set_mode((800, 600))

# Change title displayed in the game window
pygame.display.set_caption("space_invaders")

# Set the game icon
icon = pygame.image.load("images/spaceship_icon.png")
pygame.display.set_icon(icon)

#### END OF GAME WINDOW SETUP


# An event is anything that's happening inside our game screen, e.g. closing the window, moving up/down using your arrow keys
# We need to keep the game screen window open unless the player closes it
# This is also going to be our main game loop! So everything will have to go into this loop - specifically the for loop going through game events
running = True
while running:
    # pygame.event.get() grabs all of the events that are happening in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checks if the event type is the player closing the game screen window
            running = False
            print("You've quit the game")
    
    # Set the RGB fill
    screen.fill((0, 0, 0)) #obviously we can set the background to something cooler
    pygame.display.update() # whenever we want to update/add something new to the game window, we must add pygame.display.update() for the change to appear in our window! - be aware, this change is not immediate!