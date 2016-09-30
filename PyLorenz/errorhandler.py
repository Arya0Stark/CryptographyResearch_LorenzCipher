#####################################################################
# Author: Ben Slatter
# Name: errorhandler.py
# Description:  Handles various potential errors in the program.
#####################################################################

class errorhandler():
	
	def pin_dir_err(self,DIR,ERROR_LOC):
		print("\nError, PINSETTINGS_FILEPATH cannot find the DIRECTORY at: " + DIR)
		print("Please correct the filepath in %s" % ERROR_LOC)
		exit(1)
	
	def pin_fnf_err(self,FILE,ERROR_LOC):
		print("\nError, PINSETTINGS_FILEPATH cannot find the file at: " + FILE)
		print("Please correct the filepath in %s" % ERROR_LOC)
		exit(1)
	
	def pin_file_len_err(self, FILE):
		print("\n The file uploaded was not the correct length, should contain 501 pin settings (all 1's and 0's), please check: " + FILE + " is correct.")
		exit(1)
	
	def pin_pos_range_err(self):
		print("Not a numeric value, or out of range for this wheel!")
	
	def menu_non_option_err(self):
		print("Not an option in the menu, try again.")