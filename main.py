'''
YouTube video: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=10s
pygame website: https://www.pygame.org/news
'''

import pygame

# Initialise the pygame
pygame.init()

# Create a screen for our game - set the size for height, width - both in pixels
screen = pygame.display.set_mode((800, 600))

# An event is anything that's happening inside our game screen, e.g. closing the window, moving up/down using your arrow keys
# We need to keep the game screen window open unless the player closes it
# This is also going to be our main game loop! So everything will have to go into this loop - specifically the for loop going through game events
running = True
while running:
    # pygame.event.get() grabs all of the events that are happening in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checks if the event type is the player closing the game screen window
            running = False
            print("You've quite the game")