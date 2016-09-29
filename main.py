import wheel
import wheel_assembler
import block
import teleprinter
import encryption_engine
import menu

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
#####################################################################

# To Add:
	# Weekday pin settings
	# Read from/write to file
	# Comment code
	# Spurious characters?

##################################################### Program Variables #####################################################
PINSETTINGS_FILEPATH = "pinsettings.dat"
M37_INDEX,M61_INDEX = 0,1
PSI_RANGE, CHI_RANGE = 253,351
MENU_ENCRYPT,MENU_ENCRYPT_VERBOSE,MENU_CHANGE_POS,MENU_EXIT = '1',"1-V",'2','3'

##################################################### Program Starts Here #####################################################
menu = menu.menu()
show_menu = True

# Read in pin setting from file
pinsettings = open(PINSETTINGS_FILEPATH, 'r')
pins = pinsettings.read()

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
	if((menu_option == MENU_ENCRYPT) or (menu_option == MENU_ENCRYPT_VERBOSE)):
		if(menu_option == MENU_ENCRYPT_VERBOSE):
			tele.print_output(engine.encrypt(tele.read_input().upper(),True))
		else:
			tele.print_output(engine.encrypt(tele.read_input().upper()))
		
	elif(menu_option == MENU_CHANGE_POS):
		# This needs to be tidied, potential default mode if only changing a few?
		print("Changing Psi Block Starting Positions:")
		psi_block.change_block_position_settings()
		print("\nChanging Chi Block Starting Positions:")
		chi_block.change_block_position_settings()
		print("\nChanging M Wheels Starting Position:")
		m_wheels[M37_INDEX].change_start_pos()
		m_wheels[M61_INDEX].change_start_pos()
		
	elif(menu_option == MENU_EXIT or menu_option == 'EXIT'):
		show_menu = False # Not sure if both are needed?
		menu.menu_exit()

##################################################### End #####################################################
