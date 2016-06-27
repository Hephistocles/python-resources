import pygame, sys, math

class AnimatedSprite:
	frames = []
	frameNum = 0.0

	def __init__(self, frames, rectangle, rate):
		for f in frames:
			image = pygame.image.load(f)
			self.frames.append(image)
		self.rectangle = rectangle
		self.rate = float(rate)

	def frame(self):
		self.frameNum = (1/self.rate + self.frameNum)% len(self.frames)
		return self.frames[int(self.frameNum)]


class Player:
	speed = 2.0
	accel = 0.1
	maxSpeed = 10.0
	jumpSpeed = 14.0
	gravity = 0.6
	width = 50
	height = 64
	dir = 0

	def __init__(self, x, y):
		self.startX = x * 70
		self.startY = y * 70
		self.spawn()
		self.sprites = {
			"walk": AnimatedSprite(["walk%04d.png"%(i+1) for i in range(10)], self.spriteRect, 2),
			"stand": pygame.image.load("stand.png"),
			"standright": pygame.image.load("side.png"),
			"jump": pygame.image.load("jump.png")
		}
		self.sprites["standleft"] = pygame.transform.flip(self.sprites["standright"], True, False)
	
	def spawn(self):
		self.mode = "jump"
		self.xvel = 0.0
		self.yvel = 0.0
		# self.dir = 0
		self.spriteRect = pygame.Rect(self.startX, self.startY, self.width, self.height)
		self.rect = pygame.Rect(self.startX+10, self.startY+20, self.width-20, self.height-20)

	def keyboard(self, keys):
		if self.mode == "walk" or self.mode == "stand":
			vel = 0
			if keys[pygame.K_LEFT]:
				vel -= 1
			if keys[pygame.K_RIGHT]:
				vel += 1

			if vel > 0:
				self.dir = 1
				if self.xvel > 0:
					self.xvel = min(self.xvel + self.accel, self.maxSpeed)
				else:
					self.xvel = self.speed
			elif vel < 0:
				self.dir = -1
				if self.xvel < 0:
					self.xvel = max(self.xvel - self.accel, -self.maxSpeed)
				else:
					self.xvel = -self.speed

			if vel == 0:
				self.mode = "stand"
				self.xvel = 0
			else:
				self.mode = "walk"

			if keys[pygame.K_UP]:
				self.mode = "jump"
				self.yvel = -self.jumpSpeed

	def die(self):
		print("died")
		self.spawn()
	
	def update(self, grid):
		# work out which grid cells we overlap with
		cols = [(self.rect.left+1) // 70, (self.rect.right-1) // 70]
		rows = [(self.rect.top+1) // 70, (self.rect.bottom-1) // 70]
		
		cols[0] = max(0, cols[0])
		rows[0] = max(0, rows[0])
		cols[1] = min(cols[1], len(grid[0]) - 1)
		rows[1] = max(0, min(rows[1], len(grid) - 1))

		# check if we've fallen off the world
		if rows[0] >= len(grid) or cols[0] >= len(grid[0]) or cols[1] < 0:
			return self.die()

		# work out where the nearest obstacles are in each direction
		obstacles = {"left":None, "right":None, "up":None, "down":None}
		for row in rows:
			for col in range(cols[0], -1, -1):
				if grid[row][col] == 1:
					if obstacles["left"] == None:
						obstacles["left"] = (col + 1) * 70
					else:
						obstacles["left"] = max((col + 1) * 70, obstacles["left"])
					break
			for col in range(cols[1], len(grid[0])):
				if grid[row][col] == 1:
					if obstacles["right"] == None:
						obstacles["right"] = col * 70 
					else:
						obstacles["right"] = min(col * 70 , obstacles["right"])
					break
		for col in cols:
			for row in range(rows[0], -1, -1):
				if grid[row][col] == 1:
					if obstacles["up"] == None:
						obstacles["up"] = (row + 1) * 70
					else:
						obstacles["up"] = max((row + 1) * 70, obstacles["up"])
					break
			for row in range(rows[1], len(grid)):
				if grid[row][col] == 1:
					if obstacles["down"] == None:
						obstacles["down"] = row * 70
					else:
						obstacles["down"] = min(row * 70, obstacles["down"])
					break

		# fall if we're walking and there's nothing beneath us
		if self.mode == "walk" or self.mode == "stand":
			if obstacles["down"] == None or obstacles["down"] - self.rect.bottom > 0:
				self.mode = "jump"

		# work out ideally how far we should be moving
		dx, dy = 0, 0
		if self.mode == "walk":
			dx = self.xvel

		if self.mode == "jump":
			self.yvel += self.gravity
			dx = self.xvel
			dy = self.yvel

		# horizontal movement
		if dx<0:
			if obstacles["left"] != None:
				if dx <  obstacles["left"] - self.rect.left:
					dx = obstacles["left"] - self.rect.left
					self.xvel = -self.speed
					# self.mode = "stand"
		elif dx>0:
			if obstacles["right"] != None:
				if dx >  obstacles["right"] - self.rect.right:
					dx = obstacles["right"] - self.rect.right
					self.xvel = self.speed
					# self.mode = "stand"
					 
		# vertical movement		
		if dy<0:
			if obstacles["up"] != None:
				if dy <  obstacles["up"] - self.rect.top:
					dy = obstacles["up"] - self.rect.top
					self.yvel = 0
		elif dy>0:
			if obstacles["down"] != None:
				if dy >  obstacles["down"] - self.rect.bottom:
					dy =  obstacles["down"] - self.rect.bottom
					self.yvel = 0
					self.mode = "stand"

		# finally actually move the allowed amount
		self.rect.x += dx
		self.rect.y += dy

	def getSprite(self):
		if self.mode == "walk":
			img = self.sprites["walk"].frame()
			if self.dir < 0:
				img = pygame.transform.flip(img, True, False)
		elif self.mode == "stand":
			if self.dir < 0:
				img = self.sprites["standleft"]
			elif self.dir > 0:
				img = self.sprites["standright"]
			else:
				img = self.sprites["stand"]
		elif self.mode == "jump":
			img = self.sprites["jump"]
			if self.dir < 0:
				img = pygame.transform.flip(img, True, False)

		self.spriteRect.x = self.rect.x - 10
		self.spriteRect.y = self.rect.y - 20
		# img = pygame.transform.scale(img, (spriteRect.width, spriteRect.height))
		return (img, self.spriteRect)
		
def drawWorld(screen, bgs, blocks, char, grid):
	offX, offY = screen.get_width()/2, screen.get_height() - 100
	sprite = char.getSprite()

	bgrect = pygame.Rect(offX-256, offY-256, 512, 512)
	screen.blit(bgs[0], bgrect)

	offX -= sprite[1].centerx
	offY -= sprite[1].centery

	# background layers
	parallax = 4
	base = sprite[1].centerx // (512*parallax)
	screen.blit(bgs[1], bgrect.move(base * 512  - sprite[1].centerx/parallax, -170 + offY/parallax))
	screen.blit(bgs[1], bgrect.move(base * 512  + 512 - sprite[1].centerx/parallax, -170 + offY/parallax))

	parallax = 2
	base = sprite[1].centerx // (512*parallax)
	screen.blit(bgs[3], bgrect.move(base * 512 - sprite[1].centerx/parallax, -120 + offY/parallax))
	screen.blit(bgs[3], bgrect.move(base * 512 + 512 - (sprite[1].centerx/parallax), -120 + offY/parallax))
	
	# platforms
	for block in blocks:
		screen.blit(blockImg, block.move(offX, offY))

	# character
	screen.blit(sprite[0], sprite[1].move(offX, offY))


pygame.init()
grid = [[ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
		[ 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
		[ 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
		[ 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
		[ 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
		[ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]]
blockImg = pygame.image.load("ground.png")
bgs = [ pygame.image.load("bg_layer1.png"), \
		pygame.image.load("bg_layer2.png"), \
		pygame.image.load("bg_layer3.png"), \
		pygame.image.load("bg_layer4.png")]
blocks = []
for y, line in enumerate(grid):
	for x, cell in enumerate(line):
		if cell==1:
			blocks.append(pygame.Rect(x * 70, y * 70, 70, 70))
		if cell==2:
			char = Player(x, y)

size = (490, 350)
screen = pygame.display.set_mode(size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			break

	keys = pygame.key.get_pressed()


	screen.fill((0,0,0))

	# drawing
	char.keyboard(keys)
	char.update(grid)

	drawWorld(screen, bgs, blocks, char, grid)

	pygame.display.flip()
	pygame.time.wait( 1000 // 60 )
