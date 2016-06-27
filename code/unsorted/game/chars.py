import pygame, random

class Character:
	def __init__(self, img):
		self.image = pygame.image.load(img)
		self.rectangle  = self.image.get_rect()
		self.speedX = 2
		self.speedY = 2

	def draw(self, screen):
		screen.blit(self.image, self.rectangle)

	def update(self):
		return

class Player(Character):
	def __init__(self):
		Character.__init__(self, "ball.png")
		self.x = 150
		self.y = 110
	
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.rectangle.x -= self.speedX
		if keys[pygame.K_RIGHT]:
			self.rectangle.x += self.speedX
		if keys[pygame.K_UP]:
			self.rectangle.y -= self.speedY
		if keys[pygame.K_DOWN]:
			self.rectangle.y += self.speedY

class Enemy(Character):
	def __init__(self):
		Character.__init__(self, "ball2.png")
		self.rectangle.x = random.randint(20, 300)
		self.rectangle.y = random.randint(20, 220)

	def update(self):
		if self.rectangle.x < 0 or self.rectangle.x > 320 - self.rectangle.width:
			self.speedX = -self.speedX
		if self.rectangle.y < 0 or self.rectangle.y > 240 - self.rectangle.height:
			self.speedY = -self.speedY
		self.rectangle.x += self.speedX
		self.rectangle.y += self.speedY