import pygame, sys
pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)

image = pygame.image.load("Soccer-Ball-icon.png")
enemy = pygame.image.load("enemyball.png")
rect = pygame.Rect(100, 100, 96, 96)
rect_enemy = pygame.Rect(50, 50, 50, 50)
bg_colour = (255, 255, 255)
speed = 10

enemy_speed_x = -12
enemy_speed_y = 8

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_colour)
    screen.blit(image, rect)
    screen.blit(enemy, rect_enemy)
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect.left > 0:
        rect.move_ip(-speed, 0)
    if keys[pygame.K_RIGHT] and rect.right < 400:
        rect.move_ip(speed, 0)
    if keys[pygame.K_UP] and rect.top > 0:
        rect.move_ip(0, -speed)
    if keys[pygame.K_DOWN] and rect.bottom < 400:
        rect.move_ip(0, speed)

    if rect_enemy.left < 0:
        enemy_speed_x = -enemy_speed_x
    if rect_enemy.bottom > 400:
        enemy_speed_y = -enemy_speed_y
    if rect_enemy.right > 400:
        enemy_speed_x = -enemy_speed_x
    if rect_enemy.top < 0:
        enemy_speed_y = -enemy_speed_y
        
    rect_enemy.move_ip(enemy_speed_x, enemy_speed_y)

    pygame.time.wait(1000 // 30)

