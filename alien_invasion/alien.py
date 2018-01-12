import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position """
		super(Alien,self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		#Load the alien image and set its rect attribute
		self.image = pygame.image.load('images/alien_model01.bmp')
		self.rect = self.image.get_rect()

		#Start each new alien near the top left of the screen
		self.rect.x = self.rect.left
		self.rect.y = self.rect.top

		#store the alien's exact position
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Return true if alien is at edge of screen """
		screen_rect = self.screen.get_rect()
		if(self.rect.right >= screen_rect.right):
			return True
		elif(self.rect.left <= 0):
			return True

	def update(self):
		""" Move the alien right or left """
		self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
		self.rect.x  = self.x


	def blitme(self):
		self.screen.blit(self.image, self.rect)
