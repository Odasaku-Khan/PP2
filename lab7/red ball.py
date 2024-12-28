import pygame
import sys
pygame.init()
width,lenght = 600, 400
screen = pygame.display.set_mode((width,lenght))
pygame.display.set_caption("Ball")
white = (255, 255, 255)
red = (255, 0, 0)
R= 25
x_coor = 300
y_coor = 200
speed= 15
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_coor - speed - R >= 0:
                    y_coor -= speed
            elif event.key == pygame.K_DOWN:
                if y_coor + speed + R <= lenght:
                    y_coor += speed
            elif event.key == pygame.K_LEFT:
                if x_coor - speed - R >= 0:
                    x_coor -= speed
            elif event.key == pygame.K_RIGHT:
                if x_coor + speed + R <= width:
                    x_coor += speed
    screen.fill(white)
    pygame.draw.circle(screen, red, (x_coor, y_coor), R)
    pygame.display.flip()
    pygame.time.Clock().tick(120)
pygame.quit()
sys.exit()
