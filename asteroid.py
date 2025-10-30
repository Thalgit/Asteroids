import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		
	def draw(self, screen):
		center = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(screen, "white", center, int(self.radius), 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		old_radius = self.radius
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		angle = random.uniform(20, 50)
		vector1 = self.velocity.rotate(angle)
		vector2 = self.velocity.rotate(-angle)
		new_radius = old_radius - ASTEROID_MIN_RADIUS
		asteroid1 = Asteroid(int(self.position.x), int(self.position.y), new_radius)
		asteroid2 = Asteroid(int(self.position.x), int(self.position.y), new_radius)
		asteroid1.velocity = vector1 * 1.2
		asteroid2.velocity = vector2 * 1.2