import pygame, sys
from pygame.locals import *
import random, time
pygame.init()
fps = 60
FramePerSec = pygame.time.Clock()
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
width = 400
height = 600
speed = 5
score = 0
coinscore = 0
coinspawnchance = 0.01
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
coin_text = font_small.render("Coins: ", True, black)
background = pygame.image.load("AnimatedStreet.png")
coin_image = pygame.image.load("111.png")
coin_rect = coin_image.get_rect()
displaysurface = pygame.display.set_mode((400,600))
displaysurface.fill(white)
pygame.display.set_caption("Game")
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)
    def move(self):
        global coinscore
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              speed += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    displaysurface.blit(background, (0,0))
    scores = font_small.render("Score: " + str(score), True, black)
    coin_count = font_small.render(str(coinscore), True, black)
    displaysurface.blit(scores, (10,10))
    displaysurface.blit(coin_text, (300, 10))
    displaysurface.blit(coin_count, (370, 10))
    for entity in all_sprites:
        displaysurface.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        displaysurface.fill(red)
        displaysurface.blit(game_over, (30,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    if random.random() < coinspawnchance:
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)
    if pygame.sprite.spritecollide(P1, coins, True):
        coinscore += random.randint(1,5)
        speed += 1
    pygame.display.update()
    FramePerSec.tick(fps)
