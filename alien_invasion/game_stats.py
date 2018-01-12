class GameStats():
	"""Track statistic for Alien Invasion"""
	def __init__(self, ai_settings):
		"""Initialize statistic"""
		self.ai_settings = ai_settings
		self.reset_stats()

		# High score should never be reset.
		self.high_score = 0

		#Start game is an inactive state
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistic that change during the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1