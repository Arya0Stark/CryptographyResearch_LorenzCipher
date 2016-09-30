import wheel
import wheel_assembler
import block
import teleprinter
import encryption_engine
import errorhandler
import menu
import pinreader
import os

#####################################################################
# Author: Ben Slatter
# Description: A model of the Lorenz Machine used to encrypt/decrypt
#			   communications by the Germans in WWII.
#			   https://en.wikipedia.org/wiki/Lorenz_cipher
# Change Log: 28/09/16: Main code written
# 			  29/09/16: Menu added, comments added.
#						Moved menu functionality out to menu.py
#						Added mwheel polymorphism
#						Added wheel_assembler.py
#						Added verbose mode
#			  30/09/16: Added error handling and pin reading
#						Added read from file
#####################################################################

# To Add:
	# Read from/write to file
	# Check filepath()
	# Comment code
	# Error handling (own class maybe?)
		# Spurious characters?
		
##################################################### Program Variables #####################################################
PINSETTINGS_DIR = "pin_settings_day"
PINSETTINGS_FILEPATH = "pinsettings.dat"
M37_INDEX, M61_INDEX = 0,1
PSI_RANGE, CHI_RANGE = 253,351
M_ENC, M_ENC_V, M_ENC_F_FILE, M_ENC_F_FILE_V = '1',"1-V",'2',"2-V"
M_ENC_T_FILE, M_ENC_T_FILE_V, M_ENC_TF_FILE, M_ENC_TF_FILE_V = '3','3-V','4','4-V'
M_CHANGE_POS, M_EXIT = '5','6'
NO_FILE_FOUND = 2222

##################################################### Program Starts Here #####################################################
eh = errorhandler.errorhandler()
pr = pinreader.pinreader()
pins = pr.import_daily_pin_settings(PINSETTINGS_DIR)

menu = menu.menu()
show_menu = True

# Assemble the wheels from the pin settings (the pin settings are split, to avoid sending more than is necessary)
wa = wheel_assembler.wheel_assembler()
psi_wheels = wa.assemble_psi_wheels(pins[:PSI_RANGE])
chi_wheels = wa.assemble_chi_wheels(pins[CHI_RANGE:])
m_wheels   = wa.assemble_m_wheels(pins[PSI_RANGE:CHI_RANGE])

# Create the two blocks of wheels
psi_block = block.block(psi_wheels)
chi_block = block.block(chi_wheels)

# Set the encryption device up with the blocks and m wheels
engine = encryption_engine.encryption_engine(chi_block,psi_block,m_wheels)
# Take in the user input to encrypt/decrypt
tele = teleprinter.teleprinter()
menu.print_title()

# Start the menu / functionality here
while(show_menu):
	menu_option = ''.join(menu.print_menu().upper().split())
	print()
	
	# Is there a better way to do this somehow involving menu_options dictionary as a switch/case?
	# Standard Encryption/Decryption
	if((menu_option == M_ENC) or (menu_option == M_ENC_V)):
		
		if(menu_option == M_ENC_V):
			tele.print_output(engine.encrypt(tele.read_input().upper(),True))	
		else:
			tele.print_output(engine.encrypt(tele.read_input().upper()))
	
	# Standard Encryption/Decryption From File To Console
	elif((menu_option == M_ENC_F_FILE) or (menu_option == M_ENC_F_FILE_V)):
		
		file_contents = tele.read_input_file()
		if(menu_option == M_ENC_F_FILE_V):

			if(file_contents == NO_FILE_FOUND):
				eh.no_file_chosen_err()
			else:
				tele.output_to_file(engine.encrypt(file_contents.upper(),True))
		else:
			if(file_contents == NO_FILE_FOUND):
				eh.no_file_chosen_err()
			else:
				tele.print_output(engine.encrypt(file_contents.upper()))	
	
	# Standard Encryption/Decryption From Console To File
	elif((menu_option == M_ENC_T_FILE) or (menu_option == M_ENC_T_FILE_V)):
	
		if(menu_option == M_ENC_T_FILE_V):
			tele.output_to_file(engine.encrypt(tele.read_input().upper(),True))
		else:
			tele.output_to_file(engine.encrypt(tele.read_input().upper()))
			
	# Standard Encryption/Decryption From File To/From File
	elif((menu_option == M_ENC_TF_FILE) or (menu_option == M_ENC_TF_FILE_V)):
		
		file_contents = tele.read_input_file()
		if(menu_option == M_ENC_TF_FILE_V):
			
			if(file_contents == NO_FILE_FOUND):
				eh.no_file_chosen_err()
			else:
				tele.output_to_file(engine.encrypt(file_contents.upper()),True)

		else:
			if(file_contents == NO_FILE_FOUND):
				eh.no_file_chosen_err()
			else:
				tele.output_to_file(engine.encrypt(file_contents.upper()))

	# Change Pin Positions on Wheels
	elif(menu_option == M_CHANGE_POS):
		# This needs to be tidied, potential default mode if only changing a few?
		print("Changing Psi Block Starting Positions:")
		psi_block.change_block_position_settings()
		print("\nChanging Chi Block Starting Positions:")
		chi_block.change_block_position_settings()
		print("\nChanging M Wheels Starting Position:")
		m_wheels[M37_INDEX].change_start_pos()
		m_wheels[M61_INDEX].change_start_pos()
	
	# Exit Program	
	elif(menu_option == M_EXIT or menu_option == 'EXIT'):		
		show_menu = False # Not sure if both are needed?
		menu.menu_exit()

	# Non-Menu Item Entered
	else:		
		eh.menu_non_option_err()
		
##################################################### End #####################################################
