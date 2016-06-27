import pygame, sys, chars


pygame.init()
size = (320, 240)
screen = pygame.display.set_mode(size)

player = chars.Player()
badguys = [chars.Enemy(), chars.Enemy(), chars.Enemy()]
backgroundColor = (10, 10, 10)

keepPlaying = True
while keepPlaying == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keepPlaying = False
			pygame.quit()
			sys.exit()

	screen.fill(backgroundColor)
	player.update()
	player.draw(screen)
	for c in badguys:
		c.update()
		c.draw(screen)
	pygame.display.flip()

	pygame.time.wait( 1000 // 60 )
