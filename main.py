'''
YouTube video: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=10s - ended on 20:32
PyGame website: https://www.pygame.org/news
Icons: https://www.flaticon.com/
'''

import pygame

# Initialise the pygame
pygame.init()

##### SET UP GAME WINDOW
# Create a screen for our game - set the size for width, height - both in pixels
screen = pygame.display.set_mode((800, 600))

# Change title displayed in the game window
pygame.display.set_caption("space_invaders")

# Set the game icon
icon = pygame.image.load("images/spaceship_icon.png")
pygame.display.set_icon(icon)

#### END OF GAME WINDOW SETUP

# Player spaceship
player_img = pygame.image.load("images/player_spaceship.png")
player_x = 370 # x is width // 0 is the most left point of the screen // we're starting this a little less than 400 (half of full width) because we want the image to appear centred, for that, the image's left side/corner will need to be set before 400
player_y = 480 # y is height // 0 is the highest point of the screen

def player(x_position, y_position):
    screen.blit(player_img, (x_position, y_position)) # blit() is a method that draws something onto the screen - we want to draw our player spaceship on it. Arguments: blit(image, (x coordinates, y coordinates))

# An event is anything that's happening inside our game screen, e.g. closing the window, moving up/down using your arrow keys
# We need to keep the game screen window open unless the player closes it
# This is also going to be our main game loop! So everything will have to go into this loop - specifically the for loop going through game events
running = True
while running:
    # Set the RGB fill
    screen.fill((0, 0, 0)) #obviously we can set the background to something cooler
    
    # pygame.event.get() grabs all of the events that are happening in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checks if the event type is the player closing the game screen window
            running = False
            print("You've quit the game")
    
    

    #Add player - this needs to be drawn after screen.fill(), otherwise the screen will be filled over the player
    player(player_x, player_y)

    pygame.display.update() # whenever we want to update/add something new to the game window, we must add pygame.display.update() for the change to appear in our window! - be aware, this change is not immediate!

