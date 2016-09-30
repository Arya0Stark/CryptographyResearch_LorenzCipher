#####################################################################
# Author: Ben Slatter
# Name: encryption_engine.py
# Description: The object where the encryption/decryption of codes
#  			   is performed. This object also controls the rotation
#			   of the wheels.
#####################################################################

import block

class encryption_engine():

	# Constructor
	def __init__(self, psi_block_in,chi_block_in,m_block_in):
		self.BAUDOT_LEN = 5
		M37_BLOCK_INDEX = 0
		M61_BLOCK_INDEX = 1
		self.psi_block  = psi_block_in
		self.chi_block  = chi_block_in
		self.m37 = m_block_in[M37_BLOCK_INDEX]
		self.m61 = m_block_in[M61_BLOCK_INDEX]
		
		# Baudot Conversion Dictionaries
		self.encryption_dict = {
			
		'A':"00011", 'B':"11001", 'C':"01110", 'D':"01001", 'E':"00001",
		'F':"01101", 'G':"11010", 'H':"10100", 'I':"00110", 'J':"01011",
		'K':"01111", 'L':"10010", 'M':"11100", 'N':"01100", 'O':"11000",
		'P':"10110", 'Q':"10111", 'R':"01010", 'S':"00101", 'T':"10000",
		'U':"00111", 'V':"11110", 'W':"10011", 'X':"11101", 'Y':"10101",
		'Z':"10001",
		
		' ':"00100", #Space
		',':"01000", #Carriage Return
		'-':"00010", #Line Feed
		'.':"11111", #Letter Shift
		'!':"11011", #Figure Shift
		'*':"00000"  #Null
			
		}
		
		self.reverse_dict = {
			
		"00011":'A', "11001":'B', "01110":'C', "01001":'D', "00001":'E',
		"01101":'F', "11010":'G', "10100":'H', "00110":'I', "01011":'J',
		"01111":'K', "10010":'L', "11100":'M', "01100":'N', "11000":'O',
		"10110":'P', "10111":'Q', "01010":'R', "00101":'S', "10000":'T',
		"00111":'U', "11110":'V', "10011":'W', "11101":'X', "10101":'Y',
		"10001":'Z',
		
		"00100":' ', #Space
		"01000":',', #Carriage Return
		"00010":'-', #Line Feed
		"11111":'.', #Letter Shift
		"11011":'!', #Figure Shift
		"00000":'*'  #Null
			
		}
	
	# Creates the encryption key the baudot code is ^ with. To do this,
	# the current pins from all 5 wheels in both blocks are ^ with each other.
	def create_key(self):
		psi_key = self.psi_block.get_block_code()
		chi_key = self.chi_block.get_block_code()
		enc_key = []
		#print("Psi Key: ", self.listReducer(psi_key))
		#print("Chi Key: ", self.listReducer(chi_key))
			
		for x in range(self.BAUDOT_LEN):
			enc_key.append(int(psi_key[x]) ^ int(chi_key[x]))
		return enc_key
	
	# Encrypts the given string by ^ the baudot code for each character
	# with a new key from the rotating wheels
	def encrypt(self,to_encrypt, verbose=False):
		encrypted = ""
		
		for char in to_encrypt:
			key = self.create_key()
			charcode = self.encryption_dict[char]
			if(verbose):
				print()
				print("CHAR      : " + char)
				print("CHAR CODE :", charcode)
				print("KEY       :", self.listReducer(key))
				print("NEW CODE  :", self.listReducer(self.xor(charcode,key)))
				print("NEW CHAR  : " + self.reverse_dict[self.listReducer(self.xor(charcode,key))])
			encrypted += self.reverse_dict[self.listReducer(self.xor(charcode,key))]
			self.rotate()			
		return encrypted	

	# Returns the ^ result of a ^ b
	def xor(self,a,b):
		result = []
		for x in range(self.BAUDOT_LEN):
			result.append(int(a[x]) ^ int(b[x]))
		return result
	
	# Performs the rotation algorithm on the wheels
	# Algorithm:
	# -Rotate Chi block every time
	# -If the current value of m37 = 1, rotate Psi block
	# -If the current value of m61 (before rotation!) = 1, rotate m37
	# -Rotate m61
	def rotate(self):
	 	self.chi_block.rotate_block()
	 	if(self.m37.current_pin == 1):
	 		self.psi_block.rotate_block()
	 	if(self.m61.current_pin == 1):
	 		self.m37.rotate()
	 	self.m61.rotate()

	# Reduces the contents of a list to a concatenated string (no spaces).
	# Used to turn the encrypted letter lists back into a string for the
	# dictionary to use.
	def listReducer(self, listToReduce):
		return "".join(str(x) for x in listToReduce)
	