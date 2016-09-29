#####################################################################
# Author: Ben Slatter
# Name: wheel.py
# Description: An object that models the wheels of the Lorenz.
#####################################################################

class wheel():
	
	pins = []
	current_pos = 0
	NON_NUM_RANGE_ERR = "Not a numeric value, or out of range for this wheel!"
	
	# Constructor
	def __init__(self, pins_in,starting_pos,wheel_id):
		self.pins = pins_in
		self.current_pos = starting_pos
		self.wheel_id = wheel_id
	
	# "Rotate" the wheel	
	def rotate(self):
		self.current_pos = (self.current_pos + 1) % len(self.pins)
	
	# Return the value of the current pin
	def current_pin(self):
		return self.pins[self.current_pos]
	
	# Changes the starting position of the wheel before encryption begins	
	def change_start_pos(self,new_position):
		# Code to handle M Wheels updating their positions and not being in a block,
		# this function is called directly on the wheel
		if(new_position.isnumeric() and int(new_position) < len(self.pins)):
			self.current_pos = int(new_position)
		else:
			print(self.NON_NUM_RANGE_ERR)
	
	# Returns the wheel_id
	def get_wheel_id(self):
		return self.wheel_id
	
	# left-over from testing, prints out basic wheel information
		def print_wheel_info(self):
			print("Pins: ", self.pins)
			print("Current Position: ", self.current_pos)
	
class mwheel(wheel):
	
	# Polymorphic behaviour for the 'M' wheels	
	def change_start_pos(self):
	# Code to handle M Wheels updating their positions whilst not being in a block,
	# this function is called directly on the wheel
		new_position = input(self.get_wheel_id() + " New Starting Position: ")
		if(new_position.isnumeric() and int(new_position) < len(self.pins)):
			self.current_pos = int(new_position)
		else:
			print(self.NON_NUM_RANGE_ERR)