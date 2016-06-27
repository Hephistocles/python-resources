import pygame, sys, random

pygame.init()
size = (1000, 600)
screen = pygame.display.set_mode(size)

ball_imgs = [
    pygame.image.load("bubble0.png").convert(),
    pygame.image.load("bubble1.png").convert(),
    pygame.image.load("bubble2.png").convert(),
    pygame.image.load("bubble3.png").convert(),
    pygame.image.load("bubble4.png").convert(),
]
ball_rects = [
    
]

while True:
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (50,50,50), (500, 300), 128)
    pygame.display.flip()
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
