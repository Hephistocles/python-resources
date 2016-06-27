import pygame, sys, random

userans = input("Do you want to play with someone else?")
if userans == "yes":
    twoplayer = True
else:
    twoplayer = False

pygame.init()
size = (1000, 600)
screen = pygame.display.set_mode(size)

image = pygame.image.load("bat2.png")
player2 = pygame.image.load("bat1.png")
ball = pygame.image.load("ball.png")
power1_image = pygame.image.load("speedup.png")

rect = pygame.Rect(50, size[1]/2 - 56, 26, 112)
rect2 = pygame.Rect(size[0] - 76, size[1]/2 - 56, 26, 112)
ballrect = pygame.Rect(size[0]/2 - 8, size[1]/2 - 8, 16, 16)
power1_rect1 = pygame.Rect(-100,-100,32,32)
power1_rect2 = pygame.Rect(-100,-100,32,32)

power1_y1 = 0
power1_y2 = 0

bg_colour = (230,230,230)
leftspeed = 9
rightspeed = 9

ballspeedy = 10
ballspeedx = 10

scoreleft = 0
scoreright = 0

# draw score
font = pygame.font.Font("ka1.ttf", 200)

lefttext, righttext, lefttextrect, righttextrect = None, None, None, None

def updateScore():
    global lefttext, righttext, lefttextrect, righttextrect
    lefttext = font.render(str(scoreleft), 1, (100,100,100))
    righttext = font.render(str(scoreright), 1, (100,100,100))
    lefttextrect = lefttext.get_rect()
    righttextrect = righttext.get_rect()
    lefttextrect.centerx = size[0]/4
    righttextrect.centerx = 3 * size[0]/4
    lefttextrect.centery = size[1]/2
    righttextrect.centery = size[1]/2

def resetBall():
    ballrect.x,ballrect.y = size[0]/2 - 8, size[1]/2 - 8

updateScore()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print("The final score was left player = %d, right player: %d" % (scoreleft, scoreright))
            pygame.quit()
            sys.exit()

    # draw everything to the screen
    screen.fill(bg_colour)
    screen.blit(lefttext, lefttextrect)
    screen.blit(righttext, righttextrect)
    screen.blit(power1_image, power1_rect1)
    screen.blit(power1_image, power1_rect2)
    screen.blit(image, rect)
    screen.blit(player2, rect2)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    # bounce ball off paddles
    if rect.colliderect(ballrect) and ballspeedx < 0:
        ballspeedx = -ballspeedx + 0.5
    if rect2.colliderect(ballrect) and ballspeedx > 0:
        ballspeedx = -ballspeedx - 0.5
            
    # move right hand paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rect2.top > 0:
        rect2.move_ip(0, -rightspeed)
    if keys[pygame.K_DOWN] and rect2.bottom < size[1]:
        rect2.move_ip(0, rightspeed)

    # move left hand paddle
    if twoplayer == True:
        if keys[pygame.K_w] and rect.top > 0:
            rect.move_ip(0, -leftspeed)
        if keys[pygame.K_s] and rect.bottom < size[1]:
            rect.move_ip(0, leftspeed)
    else:
        if rect.bottom > ballrect.centery:
            rect.move_ip(0, -10)
        if rect.top < ballrect.centery:
            rect.move_ip(0, 10)

    # bounce ball off walls
    if ballrect.left<0:
        scoreright = scoreright + 1
        ballspeedx = - ballspeedx
        updateScore()
        resetBall()
    if ballrect.bottom > size[1]:
        ballspeedy = -ballspeedy

    if ballrect.right > size[0]:
        scoreleft = scoreleft + 1
        ballspeedx = - ballspeedx
        updateScore()
        resetBall()
    if ballrect.top<0:
        ballspeedy = -ballspeedy

    # actually moves the ball
    ballrect.move_ip(ballspeedx, ballspeedy)

    # powerups left
    if twoplayer == True:
        randnum = random.randint(1, 300)
        if randnum == 1:
            ypos = random.randint(1, size[1])
            power1_rect1.x = 50
            power1_rect1.y = ypos
        
        if rect.colliderect(power1_rect1):
            power1_rect1.x = -100
            power1_rect1.y = -100
            leftspeed = leftspeed + 5

    # powerups right
    randnum = random.randint(1, 300)
    if randnum == 1:
        ypos = random.randint(1, size[1])
        power1_rect2.x = size[0] - 82
        power1_rect2.y = ypos

    if rect2.colliderect(power1_rect2):
        power1_rect2.x = -100
        power1_rect2.y = -100
        rightspeed = rightspeed + 5
            
    # adjust frame rate
    pygame.time.wait(1000 // 30)

    if scoreleft >= 10 or scoreright >= 10:
        print("The final score was left player = %d, right player: %d" % (scoreleft, scoreright))
        pygame.quit()
        sys.exit()
