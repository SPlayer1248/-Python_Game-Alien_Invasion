class Settings():
	"""A class to store all settings of Alien Invasion"""

	def __init__(self):
		"""Initialize the game's static settings."""
		#Screen setting
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (135,206,250)

		#Ship settings
		#self.ship_speed_factor = 1.5
		self.ship_limit = 3

		#Bullet settings
		#self.bullet_speed_factor = 4
		self.bullet_width = 10
		self.bullet_height = 25
		self.bullet_color = (255,255,0)
		self.bullets_allowed = 4

		#Alien settings
		#self.alien_speed_factor = 0.4
		self.fleet_drop_speed = 10

		#How quickly the game speeds up
		self.speedup_scale = 1.1
		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 4
		self.alien_speed_factor = 0.4

		#Fleet direction of 1 represents right; -1 repesent left
		self.fleet_direction = 1

		#Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale 
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points*self.score_scale)