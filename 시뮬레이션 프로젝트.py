import pygame

# 게임 초기화
pygame.init()
screen=pygame.display.set_mode((480,640))

pygame.display.set_caption("재민")

a=True
while a:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            a=False


pygame.quit()