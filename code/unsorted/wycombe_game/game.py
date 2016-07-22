import pygame
import sys, random

class Wall:
	rectangle = None
	def __init__(self, x, y):
		self.rectangle = image_wall.get_rect()
		self.rectangle.x = y
		self.rectangle.y = x

class Enemy:
	rectangle = None
	x_speed = 2
	y_speed = 2

	def __init__(self):
		self.rectangle = image_bad.get_rect()
		self.rectangle.x = random.randint(50, size[0] - 50 - self.rectangle.width)
		self.rectangle.y = random.randint(50, size[1] - 50 - self.rectangle.height)
		self.x_speed = random.randint(-3,3)
		self.y_speed = random.randint(-3,3)

	def move(self):
		canmoveup, canmovedown, canmoveleft, canmoveright = wall_collide(self.rectangle, self.x_speed, self.y_speed, True)

		if (self.x_speed < 0):
			if (canmoveleft):
				self.rectangle.move_ip(self.x_speed, 0)
			else:
				# force movement right
				self.x_speed = abs(self.x_speed)
		elif (self.x_speed > 0):
			if (canmoveright):
				self.rectangle.move_ip(self.x_speed, 0)
			else:
				# force movement left
				self.x_speed = -abs(self.x_speed)
		if (self.y_speed < 0):
			if (canmoveup):
				self.rectangle.move_ip(0, self.y_speed)
			else:
				# force movement up
				self.y_speed = abs(self.y_speed)
		elif (self.y_speed > 0):
			if (canmovedown):
				self.rectangle.move_ip(0, self.y_speed)
			else:
				# force movement down
				self.y_speed = -abs(self.y_speed)
		
		self.collide()

	def collide(self):
		if player_rectangle.colliderect(self.rectangle):
			dx = (self.rectangle.centerx - player_rectangle.centerx)
			dy = (self.rectangle.centery - player_rectangle.centery)
			d = dx**2 + dy**2
			if (d < 35**2):
				print("You died")
				pygame.quit()
				sys.exit()

def wall_collide(move_rect, xspeed, yspeed, delete=False):
	canmoveleft = True
	canmoveright = True
	canmoveup = True
	canmovedown = True
	walls_to_delete = []
	for wall in walls:
		if (canmoveleft and wall.rectangle.collidepoint(
				move_rect.left  - xspeed,
				move_rect.top   + 0) or
			wall.rectangle.collidepoint(
				move_rect.left   - xspeed,
				move_rect.bottom - 0)):
			canmoveleft = False
			if (delete):
				walls_to_delete.append(wall)

		if (canmoveright and wall.rectangle.collidepoint(
				move_rect.right + xspeed,
				move_rect.top   + 0) or
			wall.rectangle.collidepoint(
				move_rect.right  + xspeed,
				move_rect.bottom - 0)):
			canmoveright = False
			if (delete):
				walls_to_delete.append(wall)

		if (canmovedown and wall.rectangle.collidepoint(
				move_rect.left   + 0,
				move_rect.bottom + yspeed) or
			wall.rectangle.collidepoint(
				move_rect.right  - 0,
				move_rect.bottom + yspeed)):
			canmovedown = False
			if (delete):
				walls_to_delete.append(wall)

		if (canmoveleft and wall.rectangle.collidepoint(
				move_rect.left + 0,
				move_rect.top  - yspeed) or
			wall.rectangle.collidepoint(
				move_rect.right - 0,
				move_rect.top   - yspeed)):
			canmoveup = False
			if (delete):
				walls_to_delete.append(wall)
	
	# print(walls_to_delete)
	# for w in walls_to_delete:
	# 	if w in walls:
	# 		walls.remove(w)

	return canmoveup, canmovedown, canmoveleft, canmoveright

def arrow_keys(player_rectangle):
	keys = pygame.key.get_pressed()
	canmoveup, canmovedown, canmoveleft, canmoveright = wall_collide(player_rectangle,player_speed , player_speed)
	
	if (keys[pygame.K_LEFT] and canmoveleft):
		player_rectangle.move_ip(-player_speed, 0)
	if keys[pygame.K_RIGHT] and canmoveright:
		player_rectangle.move_ip(player_speed, 0)
	if keys[pygame.K_UP] and canmoveup:
		player_rectangle.move_ip(0, -player_speed)
	if keys[pygame.K_DOWN] and canmovedown:
		player_rectangle.move_ip(0, player_speed)

wall_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.init()
size = (50 * len(wall_map[0]), 50 * len(wall_map))
screen = pygame.display.set_mode(size)


image = pygame.image.load("ball.png")
image_bad = pygame.image.load("badguy.png")
image_wall = pygame.image.load("wall.png")
font = pygame.font.Font("docktrin.ttf", 100)


image_wall = pygame.transform.scale(image_wall, (50, 50))

player_rectangle = image.get_rect()
player_speed  = 5


walls = []
for i, row in enumerate(wall_map):
	for j, cell in enumerate(row):
		if cell == 1:
			# draw a wall
			wall = Wall(i * 50, j * 50)
			walls.append(wall)
		elif cell == 3:
			player_rectangle.x = j * 50
			player_rectangle.y = i * 50
	

enemies = [Enemy()]

time = 0
last_enemy_time = 0
frames_per_second = 60
background_color = (0,0,0)

# block_rectangle
# check whether the point to my left collides:
# if (not block_rectangle.collidepoint(player_rectangle.left, player_rectangle.centery))
	# allow to move..
	
while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			break
		if event.type == pygame.MOUSEBUTTONUP:
			x, y = pygame.mouse.get_pos()
			is_in_wall = False
			for wall in walls:
				if wall.rectangle.collidepoint(x, y):
					is_in_wall = True
			if (not is_in_wall):
				# create a new wall
				j = int(len(wall_map[0]) * x / size[0])
				i = int(len(wall_map) * y / size[1])
				wall = Wall(i * 50, j * 50)
				walls.append(wall)
				

	# move the enemies appropriately 
	for enemy in enemies:
		enemy.move()
	
	# create a new enemy every three seconds
	if (time - last_enemy_time > 6):
		enemies.append(Enemy())
		last_enemy_time = time

	arrow_keys(player_rectangle)

	# draw all images in appropriate places
	screen.fill(background_color)
	
	# draw text
	text_image = font.render("Score: %d" % time, 1, (255,255,255))
	text_rect = text_image.get_rect()
	text_rect.centerx = size[0]//2
	text_rect.centery = size[1]//2
	screen.blit(text_image, text_rect)

	# draw player
	screen.blit(image, player_rectangle)
	for wall in walls:
		screen.blit(image_wall, wall.rectangle)
	# draw enemies
	for enemy in enemies:
		screen.blit(image_bad, enemy.rectangle)


	pygame.display.flip()

	time = time + 1.0 / frames_per_second
	pygame.time.wait( 1000 // frames_per_second )