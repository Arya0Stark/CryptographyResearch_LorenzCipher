#####################################################################
# Author: Ben Slatter
# Name: teleprinter.py
# Description: An object that takes input/prints output to/from the
#			   Lorenz.
#####################################################################

class teleprinter():
	
	# Reads the user's input from the console and returns it
	def read_input(self):
		input_string = input("Enter a string to be encrypted: ")
		return input_string
	
	# Prints whatever it is given to the console
	def print_output(self,output):
		print("\nResult: ", output)

