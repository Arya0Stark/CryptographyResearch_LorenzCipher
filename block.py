#####################################################################
# Author: Ben Slatter
# Name: block.py
# Description: An object to hold the 5 wheels of the Lorenz.
#####################################################################

class block():
	
	wheels = []
	NEW_POS_MESSAGE = " New Starting Position: "
	
	# Constructor
	def __init__(self, wheels_in):
		self.wheels = wheels_in
	
	# Rotate every wheel in the block
	def rotate_block(self):
		for wheel in self.wheels:
			wheel.rotate()
	
	# Get the 5 length code from reading the current value of each wheel
	def get_block_code(self):
		code = []
		for wheel in self.wheels:
			code.append(wheel.current_pin())
		return code

	# Change the current position of each wheel in the block
	def change_block_position_settings(self):
		for wheel in self.wheels:
			wheel.change_start_pos(input(wheel.get_wheel_id() + self.NEW_POS_MESSAGE))
	
	# Left-over from testing, provides info for each wheel in the block
	def print_block_info(self):
		for wheel in self.wheels:
			print(wheel.print_wheel_info())
			