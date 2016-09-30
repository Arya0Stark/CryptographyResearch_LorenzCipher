#####################################################################
# Author: Ben Slatter
# Name: teleprinter.py
# Description: An object that takes input/prints output to/from the
#			   Lorenz.
#####################################################################

import time
from tkinter import *
from tkinter.filedialog import askopenfilename

class teleprinter():
	
	OUTPUT_DIR = "C:\\Users\\slatterb\\Desktop"
	OUTPUT_FILENAME = "Lorenz_Output"
	NO_FILE_FOUND = 2222
	
	# Reads the user's input from the console and returns it
	def read_input(self):
		input_string = input("Enter a string to be encrypted: ")
		return input_string
	
	# Pulls the contents of a file into a string and returns it
	def read_input_file(self):
		root = Tk()
		root.withdraw()
		try:
			file_path = askopenfilename()
			file = open(file_path, 'r')
			file_contents = file.read()
			return file_contents
		except FileNotFoundError:
			return self.NO_FILE_FOUND
		root.destroy()
		
	# Prints whatever it is given to the console
	def print_output(self,output):
		print("\nResult: ", output)

	# Outputs whatever it is given to the output file
	def output_to_file(self,output):
		output_name = self.OUTPUT_DIR + "/" + self.gen_output_filename() + ".txt"
		self.print_output(output)
		file = open(output_name, 'a')
		file.write(output)
		print("Wrote output to: " + output_name)

	# Generates a filename following a naming convention
	def gen_output_filename(self):
		return self.OUTPUT_FILENAME + time.strftime('%d%m%Y')
	