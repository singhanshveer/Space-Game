import pygame
# Initializing the game
pygame.init()
# Creating the screen
screen = pygame.display.set_mode((800, 600))
# Setting Title and icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("images/title_logo.png")
pygame.display.set_icon(icon)
# Player
playerImg = pygame.image.load("images/player.png")
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    playerX += 0.01
    for event in pygame.event.get():
        # check if the 'X' button is pressed
        if event.type == pygame.QUIT:
            running = False
    # filling the color into the background
    # you can choose any rgb value of your choice
    # Updating the display
    player(playerX, playerY)
    pygame.display.update()
