import pygame, sys

class AnimatedSprite:
	frames = []
	frameNum = 0

	def __init__(self, frames, rectangle):
		for f in frames:
			image = pygame.image.load(f)
			frames.append(image)
		self.rectangle = rectangle
		self.frames = frames

	def draw(self, screen):
		self.frameNum = self.frameNum % len(frames)
		screen.blit(self.frames[self.frameNum], self.rectangle)



pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
char = AnimatedSprite(["char1.png", "char2.png"], pygame.Rect(0,0,50,50))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			break
		elif event.type == pygame.MOUSEDOWN:
			print "mouse at (%d, %d)" % event.pos

	screen.fill(backgroundColor)

	# drawing
	char.draw(screen)

	pygame.display.flip()
	pygame.time.wait( 1000 // 60 )
