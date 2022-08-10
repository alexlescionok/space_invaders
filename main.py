'''
YouTube video: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=10s - ended on 1:55:00
PyGame website: https://www.pygame.org/news
Icons: https://www.flaticon.com/
background: <a href='https://www.freepik.com/vectors/meteor'>Meteor vector created by vectorpouch - www.freepik.com</a>
bullet: <a href="https://www.flaticon.com/free-icons/bullet" title="bullet icons">Bullet icons created by Good Ware - Flaticon</a>
'''

'''
Next steps:
I think to make restart functionality work, we need to utilise classes - at the very least all the examples that I've seen where people talk about restarting, they use classes - once done we can troubleshoot things further.
The restart logic here makes complete sense: https://stackoverflow.com/questions/13984066/pygame-restart 
'''

from dis import dis
import pygame
import random
import math
from pygame import mixer # lets us handle music/audio in pygame

# Initialise the pygame
pygame.init()

##### GAME WINDOW SETUP
# assigning values to X and Y variable
x_window = 800
y_window = 600

# Create a screen for our game - set the size for width, height - both in pixels
screen = pygame.display.set_mode((x_window, y_window))

# Load in background
background = pygame.image.load("images/space_background1.png")

# Change title displayed in the game window
pygame.display.set_caption("space_invaders")

# Set the game icon
icon = pygame.image.load("images/spaceship_icon.png")
pygame.display.set_icon(icon)

# SET UP SCOREBOARD
# Define initial score
score = 0

green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)

# reference: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
# Define colours
def scoreboard():

    # Define the font, set the font size to 32; 'freesansbold' is a free font available in pygame
    # If you wanted to use a different font, you can download fonts, include that font in the folder sctructure and just reference it.
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Define the text to be displayed
    # True so we can display it on the screen
    # The first colour is for the text, the second colour is for the rectangle to fill around the text
    text = font.render(f"SCOREBOARD: {score}", True, green, blue)

    screen.blit(text, (10, 10))

# SET UP GAME OVER TEXT
def game_over_text():
    font = pygame.font.Font('freesansbold.ttf', 48)
    text = font.render(f"GAME OVER. FINAL SCORE: {score}", True, red, blue)
    # use get_rect and center to position text in the middle
    position = text.get_rect(center=(x_window / 2, y_window / 2))
    screen.blit(text, position)

# SET UP PLAY AGAIN TEXT
def play_again_text():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Press spacebar to play again", True, green)
    position = text.get_rect(center=(x_window / 2, y_window / 2 + 100))
    screen.blit(text, position)

#### END OF GAME WINDOW SETUP


#### GLOBALS

player_and_bullet_x_speed = 0.3
enemy_x_speed = 0.2
game_over = False

#### END OF GLOBALS

#### GAME MUSIC/SOUND EFFECTS
# mixer.music is used for longer tracks, e.g music
mixer.music.load("audio/background.wav")
mixer.music.play(-1) # -1 means play on loop

#### END OF GAME MUSIC/SOUND EFFECTS

#### PLAYER
player_img = pygame.image.load("images/player_spaceship.png")
player_x = 370 # x is width // 0 is the most left point of the screen // we're starting this a little less than 400 (half of full width) because we want the image to appear centred, for that, the image's left side/corner will need to be set before 400
player_y = 480 # y is height // 0 is the highest point of the screen

# Define the change as 0 to start - this will become a different value depending on player's actions
player_x_change = 0

def player(x_position, y_position):
    screen.blit(player_img, (x_position, y_position)) # blit() is a method that draws something onto the screen - we want to draw our player spaceship on it. Arguments: blit(image, (x coordinates, y coordinates))

#### END OF PLAYER

#### PLAYER BULLET
bullet_img = pygame.image.load("images/bullet.png")
bullet_x = 0 # x is width // 0 is the most left point of the screen - this will be controlled in a while loop
bullet_y = 480 # y is height // 0 is the highest point of the screen - keeping it at 480 because that's where the ship is

bullet_x_change = 0 # Define the change as 0 to start - this will become a different value depending on player's actions
bullet_y_change = 1 # a moderate speed for the bullet to move

# Define bullet state - when "ready", you can't see the bullet; when "fire", you can see the bullet moving
bullet_state = "ready"

def fire_bullet(x_position, y_position):
    global bullet_state # to grab global bullet_state variable
    bullet_state = "fire"
    screen.blit(bullet_img, (x_position + 16, y_position + 16))

#### END OF BULLET

#### BULLET COLLISION ####
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    # "distance" will store the distance between our bullet and our enemy
    # formula for this: https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint
    # we are grabbing the square root (math.sqrt) of enemy_x - bullet_x (the result of which is made to the power of 2 [math.pow(<some number(s)>, <power of something>)]) and enemy_y - bullet_y also to the power of 2
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    # print(distance)
    if distance < 26: # the lower the number the more it looks like the bullet has gone into the enemy
        return True

#### ENEMY
# Define lists which we will append the enemy variables to in order to create multiple enemies
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

# Set the number of enemies we want to have
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("images/enemy_spaceship.png"))
    # set the value to random
    enemy_x.append(random.randint(0, 736)) # x is width // 0 is the most left point of the screen
    enemy_y.append(random.randint(50, 200)) # y is height // 0 is the highest point of the screen

    #Define the change as 0 to start
    enemy_x_change.append(0.3)
    enemy_y_change.append(30) # maybe we add random to this to increase the tension!!

# the i argument at the end will tell screen blit how many times to draw the enemy image
def enemy(x_position, y_position, i):
    screen.blit(enemy_img[i], (x_position, y_position))

#### END OF ENEMY


#### MAIN FUNCTION ###########################

def main():
    # Set the RGB fill
    screen.fill((0, 0, 0)) #obviously we can set the background to something cooler

    # Set background image
    screen.blit(background, (0, 0))

    global player_x
    global player_y
    global player_x_change
    global bullet_y
    global bullet_state
    global score
    global game_over

    

    # Define new value of player_x following the for loop checking for events (left/right keystrokes)
    player_x += player_x_change
    
    # Stop the player from going beyond 800px and less than 0px - so that the player cannot leave the window
    if player_x > 736: #less than 800 to account for the spaceship size (64px)
        player_x = 736
    elif player_x < 0:
        player_x = 0

    #### ENEMY MOVEMENT
    for i in range(num_of_enemies):
        # GAME OVER CONDITION
        if enemy_y[i] > 200: # the point at which the enemy hits the spaceship
            for j in range(num_of_enemies):
                # move all enemies out of the window screen
                enemy_y[j] = 2000
                player_y = 2000
            # show game over text
            game_over = True
            game_over_text()
            play_again_text()
            
        
        # target the relevant index [i] in the num_of_enemies list - without this, the game won't know which enemy to affect as they all have different x and y coordinates
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] > 736: #less than 800 to account for the enemy size (64px)
            enemy_x_change[i] -= enemy_x_speed
            enemy_x[i] += enemy_x_change[i]
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] < 0:
            enemy_x_change[i] += enemy_x_speed
            enemy_x[i] += enemy_x_change[i]
            enemy_y[i] += enemy_y_change[i]

        #### BULLET COLLISION
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision: # if it is True
            # Add in sound effect for the enemy spaceship being hit
            # mixer.Sound is used for shorter sounds, e.g. sound effects
            explosion_sound = mixer.Sound("audio/explosion_sound.wav")
            explosion_sound.play() # didn't add -1 as an argument because we don't want the sound to play in a loop
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            # respawn the enemy at a random point
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 200)

        #### END OF BULLET COLLISION

        # DISPLAY ENEMY
        enemy(enemy_x[i], enemy_y[i], i)

    #### END OF ENEMY MOVEMENT

    #### BULLET MOVEMENT
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        # once the bullet gets past the top of the window, let me player fire again
        if bullet_y <= 0:
            bullet_y = 480
            # reset the state to "ready" so that it doesn't continue firing - although this could be an idea for an automatic weapon...
            bullet_state = "ready"

    #### END OF BULLET MOVEMENT

    # Add player - this needs to be drawn after screen.fill(), otherwise the screen will be filled over the player
    player(player_x, player_y)

    # Add scoreboard
    scoreboard()

#### END OF MAIN FUNCTION ###########################



# An event is anything that's happening inside our game screen, e.g. closing the window, moving up/down using your arrow keys
# We need to keep the game screen window open unless the player closes it
# This is also going to be our main game loop! So everything will have to go into this loop - specifically the for loop going through game events
running = True
while running:
    main()
    
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
                player_x_change -= player_and_bullet_x_speed
                bullet_x_change -= player_and_bullet_x_speed
            # if player presses on the right key, move to the left (for as long as the right key is pressed)
            if event.key == pygame.K_RIGHT:
                # increase the value of player_x_change
                player_x_change += player_and_bullet_x_speed
                bullet_x_change += player_and_bullet_x_speed
            # if the player presses on the spacebar AND the bullet_state is "ready", then allow the user to fire!
            # the bullet_state has to be "ready", because that is what it is set before the bullet is every fired and when the bullet_y has been reset back to 480 (check bullet movement - the state gets reverted back to "ready" after initially being "fire")
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                # Add in sound effect for the bullet being fired
                # mixer.Sound is used for shorter sounds, e.g. sound effects
                bullet_sound = mixer.Sound("audio/fire_sound.wav")
                bullet_sound.play() # didn't add -1 as an argument because we don't want the sound to play in a loop
                
                # define bullet_x to be the same as player_x - this along with bullet_x being passed as an argument in the bullet movement will ensure that the bullet uses the x_position of when it is fired, rather than follow the player spaceship
                bullet_x = player_x
                # trigger the fire_bullet function
                fire_bullet(bullet_x, bullet_y)
            if event.key == pygame.K_r and game_over == True:
                print("PRESSED R")
                main()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # Don't change the value of player_x_change - we don't want the player to move any further once the left/right key is no longer pressed
                player_x_change = 0
    
    
    # restarting reference: https://www.reddit.com/r/pygame/comments/n8vnn2/how_do_i_make_a_restart_button/
    # game is suuuuuper slow when if game_over block is in the for event in pygame.event.get(): loop / was previously in the while loop
        # if game_over == False:
        #     main()
        # if game_over == True:
            # if event.key == pygame.K_r:
            #     game_over = False
            #     main()


    pygame.display.update() # whenever we want to update/add something new to the game window, we must add pygame.display.update() for the change to appear in our window! - be aware, this change is not immediate!