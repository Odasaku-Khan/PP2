import pygame
import sys
pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Paint")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
gigant = 20
big = 15
mid = 10
small = 5
SHAPE_COLOR = blue
active_size = gigant
active_color = black
painting = []
def draw_menu():
    global gigant, big, mid, small
    screen.fill(white)
    pygame.draw.rect(screen, (128, 128, 128), [0, 0, w, 80])
    pygame.draw.line(screen, (100, 100, 100), (0, 80), (w, 80), 3)
    gigant_rect = pygame.draw.rect(screen, black, [10, 10, 50, 50])
    pygame.draw.circle(screen, white, (35, 35), 21)
    big_rect = pygame.draw.rect(screen, black, [70, 10, 50, 50])
    pygame.draw.circle(screen, white, (95, 35), 15)
    mid_rect = pygame.draw.rect(screen, black, [130, 10, 50, 50])
    pygame.draw.circle(screen, white, (155, 35), 10)
    small_rect = pygame.draw.rect(screen, black, [190, 10, 50, 50])
    pygame.draw.circle(screen, white, (215, 35), 5)
    square_rect = pygame.draw.rect(screen, black, [270, 10, 50, 50])
    pygame.draw.rect(screen, white, [280, 20, 30, 30])
    triangle_rect = pygame.draw.rect(screen, black, [330, 10, 50, 50])
    pygame.draw.polygon(screen, white, [(355, 35), (305, 10), (380, 10)])
    rhombus_rect = pygame.draw.rect(screen, black, [390, 10, 50, 50])
    pygame.draw.polygon(screen, white, [(415, 10), (390, 35), (440, 35), (465, 10)])
    brush_list = [gigant_rect, big_rect, mid_rect, small_rect, square_rect, triangle_rect, rhombus_rect]
    colors = [(blue, (w - 35, 10, 25, 25)), (red, (w - 35, 35, 25, 25)), 
              (green, (w - 60, 10, 25, 25)), (black, (w - 60, 35, 25, 25)), 
              (yellow, (w - 85, 10, 25, 25)), (white, (w - 85, 35, 25, 25))]
    for color in colors:
        pygame.draw.rect(screen, color[0], color[1])
    
    return brush_list, [color[1] for color in colors]
def draw_painting(paints):
    for paint in paints:
        pygame.draw.circle(screen, paint[0], paint[1], paint[2])
def draw_square(pos, size):
    x, y = pos
    rect = pygame.Rect(x - size // 2, y - size // 2, size, size)
    pygame.draw.rect(screen, SHAPE_COLOR, rect, 3)
def draw_triangle(pos, size):
    x, y = pos
    points = [(x, y - size // 2), (x - size // 2, y + size // 2), (x + size // 2, y + size // 2)]
    pygame.draw.polygon(screen, SHAPE_COLOR, points, 3)
def draw_rhombus(pos, size):
    x, y = pos
    points = [(x, y - size // 2), (x - size // 2, y), (x, y + size // 2), (x + size // 2, y)]
    pygame.draw.polygon(screen, SHAPE_COLOR, points, 3)
running = True
brushes = []
colors = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] < 80:
                for i, brush_rect in enumerate(brushes):
                    if brush_rect.collidepoint(event.pos):
                        active_size = [gigant, big, mid, small][i]
                for i, color_rect in enumerate(colors):
                    if color_rect.collidepoint(event.pos):
                        active_color = [blue, red, green, black, yellow, white][i]
            elif event.pos[1] > 80:
                if event.button == 1:
                    painting.append((active_color, event.pos, active_size))
                elif event.button == 3:
                    draw_square(event.pos, active_size * 2)
                elif event.button == 2:
                    draw_triangle(event.pos, active_size * 2)
                elif event.button == 4:
                    draw_rhombus(event.pos, active_size * 2)
    brushes, colors = draw_menu()
    draw_painting(painting)
    pygame.display.flip()
pygame.quit()
