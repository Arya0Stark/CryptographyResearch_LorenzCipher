#####################################################################
# Author: Ben Slatter
# Name: menu.py
# Description: Controls the menu of the program
#####################################################################
import collections

class menu():
	
	MENU_MESSAGE = "Select an option from the menu: "
	MENU_TITLE,MENU_WIDTH,TITLE_SPACES,MENU_ADJUST = "Lorenz Machine Simulator",46,10,3
	STAR,SPACE,STAR_SPACE,COLON_SPACE,D_NEWLINE,NEWLINE = "*"," ","* "," : ","\n\n","\n"
	BORDER_HOR = STAR * MENU_WIDTH
	MENU_OPTIONS = {
							'1':"Encrypt/Decrypt Input (-v for Verbose)",
							'2':"Encrypt/Decrypt From File",
							'3':"Encrypt/Decrypt To File",
							'4':"Encrypt/Decrypt From/To File",
							'5':"Set Wheel/Pin Positions (Default = 0)",
							'6':"Exit (Alternatively, type 'exit')"
						}
	MENU_OPTIONS = collections.OrderedDict(sorted(MENU_OPTIONS.items()))
	EXIT_MESSAGE = "Exiting Lorenz Simulator\n\n"
	
	# Assemble the title from the components above and print it to the console
	def print_title(self):
		print(self.D_NEWLINE + self.BORDER_HOR)
		print(self.STAR + (self.SPACE * self.TITLE_SPACES) + self.MENU_TITLE + (self.SPACE * self.TITLE_SPACES) + self.STAR)
		print(self.BORDER_HOR)
	
	# Assemble the menu from the components above and print it to the console
	def print_menu(self):
		print(self.NEWLINE + self.BORDER_HOR)
		for k,v in self.MENU_OPTIONS.items():
			optionlen = len(k + self.COLON_SPACE + v) + self.MENU_ADJUST
			print(self.STAR_SPACE + k + self.COLON_SPACE + v + self.SPACE * (self.MENU_WIDTH - optionlen) + self.STAR )
		print(self.BORDER_HOR)
		print(self.D_NEWLINE)
		return input(self.MENU_MESSAGE)
	
	# Exit the menu
	def menu_exit(self):
		print(self.EXIT_MESSAGE)
		exit(0)
		