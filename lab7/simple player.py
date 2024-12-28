import pygame
import os
pygame.init()
width=400
lenght=400
screen=pygame.display.set_mode((width,lenght))
pygame.display.set_caption("Player")
folder="music"
music=[file for file in os.listdir(folder) if file.endswith(".mp3")]
trackinx=0
play=False
pygame.mixer.music.load(os.path.join(folder,music[trackinx]))
def playmus():
    global play
    pygame.mixer.music.play()
    play=True
def stopmus():
    global play
    pygame.mixer.music.stop()
    play=False
def next():
    global trackinx
    trackinx=(trackinx+1)%(len(music))
    pygame.mixer.music.load(os.path.join(folder, music[trackinx]))
    if play:
        playmus()
def previous():
    global trackinx
    trackinx=(trackinx-1)%(len(music))
    pygame.mixer.music.load(os.path.join(folder,music[trackinx]))
    if play:
        playmus()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if play:
                    stopmus()
                else:
                    playmus()
            elif event.key==pygame.K_RIGHT:
                next()
            elif event.key==pygame.K_LEFT:
                previous()
    pygame.display.flip()
pygame.quit()