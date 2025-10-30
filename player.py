from circleshape import *
from constants import *
from shots import *
import pygame

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_cd = 0
		
	#player lijkt driehoek, is stiekem cirkel

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	# draaien en bewegen en ook schieten

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			if self.shoot_cd <= 0:
				self.shoot()
				self.shoot_cd = PLAYER_SHOOT_COOLDOWN
		self.shoot_cd -= dt

	# pewpewpew

	def shoot(self):
		bullet = Shot(int(self.position.x), int(self.position.y), SHOT_RADIUS)
		velocity = pygame.Vector2(0, 1)
		velocity = velocity.rotate(self.rotation)
		bullet.velocity = velocity * PLAYER_SHOOT_SPEED

