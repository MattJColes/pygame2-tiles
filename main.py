from tiles import *
from spritesheet import Spritesheet


################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 270
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()

################################# LOAD PLAYER AND SPRITESHEET###################################
spritesheet = Spritesheet('spritesheet.png')
player_img = pygame.image.load('assets/sprites/paul-pixel.png')
player_rect = player_img.get_rect()

def player(playerX, playerY):


    window.blit(player_img, (playerX, playerY))


#################################### LOAD THE LEVEL #######################################
map = TileMap('assets/maps/level_1.csv', spritesheet)
playerX_change = 0
playerX, playerY = map.start_x, map.start_y

################################# GAME LOOP ##########################
while running:
    clock.tick(60)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5

    ################################# UPDATE/ Animate SPRITE #################################
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((0, 180, 240)) # Fills the entire screen with light blue
    map.draw_map(canvas)
    window.blit(canvas, (0,0))
    player(playerX, playerY)
    pygame.display.update()









