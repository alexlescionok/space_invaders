'''
YouTube video: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=10s - ended on 1:12:05
PyGame website: https://www.pygame.org/news
Icons: https://www.flaticon.com/
background: <a href='https://www.freepik.com/vectors/meteor'>Meteor vector created by vectorpouch - www.freepik.com</a>
'''

import pygame
import random

# Initialise the pygame
pygame.init()

##### GAME WINDOW SETUP
# Create a screen for our game - set the size for width, height - both in pixels
screen = pygame.display.set_mode((800, 600))

# Load in background
background = pygame.image.load("images/space_background1.png")

# Change title displayed in the game window
pygame.display.set_caption("space_invaders")

# Set the game icon
icon = pygame.image.load("images/spaceship_icon.png")
pygame.display.set_icon(icon)

#### END OF GAME WINDOW SETUP

#### PLAYER
player_img = pygame.image.load("images/player_spaceship.png")
player_x = 370 # x is width // 0 is the most left point of the screen // we're starting this a little less than 400 (half of full width) because we want the image to appear centred, for that, the image's left side/corner will need to be set before 400
player_y = 480 # y is height // 0 is the highest point of the screen

# Define the change as 0 to start - this will become a different value depending on player's actions
player_x_change = 0

def player(x_position, y_position):
    screen.blit(player_img, (x_position, y_position)) # blit() is a method that draws something onto the screen - we want to draw our player spaceship on it. Arguments: blit(image, (x coordinates, y coordinates))

#### END OF PLAYER

#### ENEMY
enemy_img = pygame.image.load("images/enemy_spaceship.png")
# set the value to random
enemy_x = random.randrange(0, 736) # x is width // 0 is the most left point of the screen
enemy_y = random.randrange(50, 416) # y is height // 0 is the highest point of the screen

#Define the change as 0 to start
enemy_x_change = 0.3
enemy_y_change = 30 # maybe we add random to this to increase the tension!!

def enemy(x_position, y_position):
    screen.blit(enemy_img, (x_position, y_position)) # blit() is a method that draws something onto the screen - we want to draw our player spaceship on it. Arguments: blit(image, (x coordinates, y coordinates))

#### END OF ENEMY

# An event is anything that's happening inside our game screen, e.g. closing the window, moving up/down using your arrow keys
# We need to keep the game screen window open unless the player closes it
# This is also going to be our main game loop! So everything will have to go into this loop - specifically the for loop going through game events
running = True
while running:
    # Set the RGB fill
    screen.fill((0, 0, 0)) #obviously we can set the background to something cooler

    # Set background image
    screen.blit(background, (0, 0))

    # pygame.event.get() grabs all of the events that are happening in the game
    # This for loop checks for events and reacts to them
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checks if the event type is the player closing the game screen window
            running = False
            print("You've quit the game")
        # check if the player has used key to move...
        # KEYDOWN is pressing on the key // KEYUP is releasing a pressed button
        if event.type == pygame.KEYDOWN: 
            # if player presses on the left key, move to the left (for as long as the left key is pressed)
            if event.key == pygame.K_LEFT:
                # decrease the value of player_x_change (we can add a negative number to decrease the number, e.g. 5 + -0.1 = 4.9)
                player_x_change = -0.2
            # if player presses on the right key, move to the left (for as long as the right key is pressed)
            elif event.key == pygame.K_RIGHT:
                # increase the value of player_x_change
                player_x_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # Don't change the value of player_x_change - we don't want the player to move any further once the left/right key is no longer pressed
                player_x_change = 0
    
    # Define new value of player_x following the for loop checking for events (left/right keystrokes)
    player_x += player_x_change
    
    # Stop the player from going beyond 800px and less than 0px - so that the player cannot leave the window
    if player_x > 736: #less than 800 to account for the spaceship size (64px)
        player_x = 736
    elif player_x < 0:
        player_x = 0


    #### ENEMY MOVEMENT
    enemy_x += enemy_x_change

    if enemy_x > 736: #less than 800 to account for the enemy size (64px)
        enemy_x_change = -0.2
        enemy_x += enemy_x_change
        enemy_y += enemy_y_change
    elif enemy_x < 0:
        enemy_x_change = 0.2
        enemy_x += enemy_x_change
        enemy_y += enemy_y_change

    #### END OF ENEMY MOVEMENT

    #Add player - this needs to be drawn after screen.fill(), otherwise the screen will be filled over the player
    player(player_x, player_y)
    #Add enemy
    enemy(enemy_x, enemy_y)

    pygame.display.update() # whenever we want to update/add something new to the game window, we must add pygame.display.update() for the change to appear in our window! - be aware, this change is not immediate!