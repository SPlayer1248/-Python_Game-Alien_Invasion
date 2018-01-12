import sys
from game_stats import GameStats
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
	#Initialize game and create a scree object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make play button
	play_button = Button(ai_settings,screen,"Play")

	# Create an instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)

	#Make a ship, group of bullet and group of aliens
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	#Create a fleet of aliens
	gf.create_fleet(ai_settings,screen, ship, aliens)

	#Start the main loop for the game
	while True:
		
		#Watch for keyboard and mouse event
		gf.check_events(ai_settings, screen, stats, sb, play_button,ship, aliens,bullets)
		if(stats.game_active == True):
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, play_button)


run_game()