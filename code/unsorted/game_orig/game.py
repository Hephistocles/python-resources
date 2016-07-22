# Phase 1
import pygame
pygame.init()
size = (320, 240)
screen = pygame.display.set_mode(size)

# Phase 3
image = pygame.image.load("ball.png")
rectangle = image.get_rect()
backgroundColor = (0, 0, 0)

# Phase 2
keepPlaying = True
while keepPlaying:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keepPlaying = False

	# Phase 3
	screen.fill(backgroundColor)
	screen.blit(image, rectangle)
	pygame.display.flip()

	# Phase 4
	# rectangle.move_ip(1, 1) # Goes too fast!

	# Phase 6
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		rectangle.move_ip(-1, 0)
	if keys[pygame.K_RIGHT]:
		rectangle.move_ip(1, 0)
	if keys[pygame.K_UP]:
		rectangle.move_ip(0, -1)
	if keys[pygame.K_DOWN]:
		rectangle.move_ip(0, 1)

	# Phase 5
	pygame.time.wait( 1000 // 50 )