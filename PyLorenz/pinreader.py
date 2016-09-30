#####################################################################
# Author: Ben Slatter
# Name: pinreader.py
# Description: Pulls in the pin settings for that particular day.
#  			   Performs checks on the files/folders to ensure that
#			   they are correct before using them.
#####################################################################

import datetime
import os
import errorhandler

class pinreader():
	
	eh = errorhandler.errorhandler()
	FILE_LEN = 500
	pin_settings_day_file = {	
								"MONDAY"    : "pinsettings_mon.dat",
								"TUESDAY"   : "pinsettings_tue.dat",
								"WEDNESDAY" : "pinsettings_wed.dat",
								"THURSDAY"  : "pinsettings_thu.dat",
								"FRIDAY"    : "pinsettings_fri.dat",
								"SATURDAY"  : "pinsettings_sat.dat",
								"SUNDAY"    : "pinsettings_sun.dat"	
							}
	
	# Check that the directory that holds the pin settings exists
	def import_daily_pin_settings(self,PINSETTINGS_DIR):
		if(os.path.isdir(PINSETTINGS_DIR)):
			return self.import_day_pin_settings(PINSETTINGS_DIR)
		else:
			eh.pin_dir_err(PINSETTINGS_DIR,os.path.basename(__file__))
	
	# Pull in the file for the correct day
	def import_day_pin_settings(self, PINSETTINGS_DIR):
		date = datetime.datetime.now()
		return self.check_pin_settings(PINSETTINGS_DIR, self.pin_settings_day_file[date.strftime("%A").upper()])
		
	# Check that the pin settings dat file exists and is a file rather than a directory
	def check_pin_settings(self, PINSETTINGS_DIR, PINSETTINGS_FILEPATH):
		FILE = PINSETTINGS_DIR + "/" + PINSETTINGS_FILEPATH
		if(os.path.isfile(FILE) == False):
			eh.pin_fnf_err(FILE,os.path.basename(__file__))
		else:
			return self.import_pin_settings(FILE)
	
	# Import the pin settings from the dat file
	def import_pin_settings(self, FILE):
		pinsettings = open(FILE, 'r')
		pins = pinsettings.read().strip()
		# If there aren't enough pin settings. Does't matter if it's too big, as the first 501 will be used.
		if(len(pins) <= self.FILE_LEN):
			self.eh.pin_file_len_err(FILE)
		else:
			return pins
	