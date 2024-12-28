import pygame
import time
import random
snake_speed = 4
x = 700
y = 400
blue=pygame.Color(0,0,255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
pygame.init()
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((x, y))
fps = pygame.time.Clock()
snake_position = [random.randrange(1, (x//10)) * 10, random.randrange(1, (y//10)) * 10]  
snake_body = [snake_position]
fruit_position = [random.randrange(1, (x//10)) * 10, random.randrange(1, (y//10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
FRUIT_SPAWN_DURATION = 7000  
fruit_spawn_time = pygame.time.get_ticks()
def game_over():
    my_font = pygame.font.SysFont('arial black', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, black)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (x/2, y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    if snake_position[0] < 0 or snake_position[0] >= x or snake_position[1] < 0 or snake_position[1] >= y:
        game_over()  
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
    current_time = pygame.time.get_ticks()
    if current_time - fruit_spawn_time >= FRUIT_SPAWN_DURATION:
        fruit_spawn = False
    if not fruit_spawn:
        fruit_spawn_time = current_time
        fruit_position = [random.randrange(1, (x // 10)) * 10,random.randrange(1, (y // 10)) * 10]
    fruit_spawn = True
    game_window.fill(white)
    for pos in snake_body:
        pygame.draw.rect(game_window, green,pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    pygame.display.update()
    fps.tick(snake_speed)
