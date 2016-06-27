# My super game
import pygame, sys, random

class Enemy:
    def __init__(self, size):
        self.img = pygame.image.load("bubble" + size + ".png")
        self.rect = self.img.get_rect()
        self.size = size
        self.xspeed = 1
        self.accel = 0.1 + size/10
        self.yspeed = 
    def update(self):
        self.yspeed = self.yspeed + 0.2
        self.rect.move_ip(self.xspeed, self.yspeed)
        
        if self.rect.bottom > 480:
            self.yspeed = - self.yspeed
            self.rect.bottom = 479
        if self.rect.top < 0:
            self.yspeed = - self.yspeed
            self.rect.top = 1
        if self.rect.right > 640:
            self.xspeed = - self.xspeed
            self.rect.right = 639
        if self.rect.left < 0 :
            self.xspeed = - self.xspeed
            self.rect.left = 1
    def draw(self, screen):
        screen.blit(self.img, self.rect)
    def collide(self, rect):
        distx = self.rect.centerx - rect.centerx
        disty = self.rect.centery - rect.centery
        dist = (distx **2  + disty**2) ** 0.5
        return dist < self.rect.width/2

# initialisation phase
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
bg_colour = (255, 255, 255)
clock = pygame.time.Clock()
speed = 5
bullet_x = 0 
bullet_y = 0
    

# init images
ball_img = pygame.image.load("stand.png")
ball_rect = pygame.Rect(10, 10, 50, 64)
ball_rect.bottom = 480

bullet_img = pygame.image.load("bullet.png")
bullet_rect = pygame.Rect(-100, -100, 16, 16)

enemies = [Enemy(160)]

# main game loop
while True:

    # handle pygame events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

    # draw stuff
    screen.fill( bg_colour )
    screen.blit(ball_img, ball_rect)
    screen.blit(bullet_img, bullet_rect)
    for enemy in enemies:
        enemy.draw(screen)
    pygame.display.flip()

    # update game logic
    temp_bullet_x = 0
    temp_bullet_y = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_rect.left > 0:
        ball_rect.move_ip(-speed, 0)
        temp_bullet_x = temp_bullet_x - 10
    #if keys[pygame.K_UP] and ball_rect.top > 0:
    #    ball_rect.move_ip(0, -speed)
    #    temp_bullet_y = temp_bullet_y - 10
    if keys[pygame.K_RIGHT] and ball_rect.right < size[0]:
        ball_rect.move_ip(speed, 0)
        temp_bullet_x = temp_bullet_x + 10
    #if keys[pygame.K_DOWN] and ball_rect.bottom < size[1]:
    #    ball_rect.move_ip(0, speed)
    #    temp_bullet_y = temp_bullet_y + 10

    if keys[pygame.K_SPACE]:
        bullet_rect.centerx = ball_rect.centerx
        bullet_rect.centery = ball_rect.centery
        #bullet_x = temp_bullet_x
        #bullet_y = temp_bullet_y

    bullet_rect.move_ip(0, -15)  

    for enemy in enemies:
        enemy.update()

        if enemy.collide(ball_rect) :
            print("You lose")
            pygame.quit()
            sys.exit()
            
        if enemy.collide(bullet_rect):
            bullet_rect.x = -100
            bullet_x = 0
            bullet_y = 0

            enemies.remove(enemy)
            bulletspeed = 7
            if enemy.size > 20:
                newEnemy1 = Enemy(enemy.size//2)
                newEnemy1.xspeed = random.randrange(-bulletspeed, bulletspeed)
                newEnemy1.yspeed = random.randrange(-bulletspeed, bulletspeed)
                newEnemy1.rect.centerx = enemy.rect.centerx
                newEnemy1.rect.centery = enemy.rect.centery
                
                newEnemy2 = Enemy(enemy.size//2)
                newEnemy2.xspeed = random.randrange(-bulletspeed, bulletspeed)
                newEnemy2.yspeed = random.randrange(-bulletspeed, bulletspeed)
                newEnemy2.rect.centerx = enemy.rect.centerx
                newEnemy2.rect.centery = enemy.rect.centery

                enemies.append(newEnemy1)
                enemies.append(newEnemy2)

    clock.tick(30)
