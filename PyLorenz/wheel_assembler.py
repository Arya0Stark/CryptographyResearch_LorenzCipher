#####################################################################
# Author: Ben Slatter
# Name: wheel_assembler.py
# Description: Creates the instances of the wheels.
#####################################################################

import wheel

class wheel_assembler():
	
	#Wheel number			1	2	3	4	5	6	7	8	9	10	11	12
	#Number of cams (pins)	43	47	51	53	59	37	61	41	31	29	26	23
	
	PSI_RANGE, CHI_RANGE = 253,351
	PSI1_RANGE,PSI2_RANGE,PSI3_RANGE,PSI4_RANGE,PSI5_RANGE = 43,90,141,194,253
	M37_RANGE,M61_RANGE = 37,98
	CHI1_RANGE,CHI2_RANGE,CHI3_RANGE,CHI4_RANGE,CHI5_RANGE = 41,72,91,117,140
	psi_wheels = []
	chi_wheels = []
	m_wheels   = []
	
	# Assembles the psi wheels from the provided pin settings
	def assemble_psi_wheels(self, pin_settings):
		
		psi1Settings, psi2Settings, psi3Settings, psi4Settings, psi5Settings = [],[],[],[],[]
		
		for i in range(self.PSI1_RANGE):
			psi1Settings.append(pin_settings[i])
		psi1 = wheel.wheel(psi1Settings,0,"Psi1")
		self.psi_wheels.append(psi1)
		
		for i in range(self.PSI1_RANGE,self.PSI2_RANGE):
			psi2Settings.append(pin_settings[i])
		psi2 = wheel.wheel(psi2Settings,0,"Psi2")
		self.psi_wheels.append(psi2)
		
		for i in range(self.PSI2_RANGE,self.PSI3_RANGE):
			psi3Settings.append(pin_settings[i])
		psi3 = wheel.wheel(psi3Settings,0,"Psi3")
		self.psi_wheels.append(psi3)
		
		for i in range(self.PSI3_RANGE,self.PSI4_RANGE):
			psi4Settings.append(pin_settings[i])
		psi4 = wheel.wheel(psi4Settings,0,"Psi4")
		self.psi_wheels.append(psi4)
		
		for i in range(self.PSI4_RANGE,self.PSI5_RANGE):
			psi5Settings.append(pin_settings[i])
		psi5 = wheel.wheel(psi5Settings,0,"Psi5")
		self.psi_wheels.append(psi5)
		
		return self.psi_wheels
	
	# Assembles the chi wheels from the provided pin settings	
	def assemble_chi_wheels(self, pin_settings):
		
		chi1Settings, chi2Settings, chi3Settings, chi4Settings, chi5Settings = [],[],[],[],[]	
		
		for i in range(self.CHI1_RANGE):
			chi1Settings.append(pin_settings[i])
		chi1 = wheel.wheel(chi1Settings,0,"Chi1")
		self.chi_wheels.append(chi1)
		
		for i in range(self.CHI1_RANGE,self.CHI2_RANGE):
			chi2Settings.append(pin_settings[i])
		chi2 = wheel.wheel(chi2Settings,0,"Chi2")
		self.chi_wheels.append(chi2)
		
		for i in range(self.CHI2_RANGE,self.CHI3_RANGE):
			chi3Settings.append(pin_settings[i])
		chi3 = wheel.wheel(chi3Settings,0,"Chi3")
		self.chi_wheels.append(chi3)
		
		for i in range(self.CHI3_RANGE,self.CHI4_RANGE):
			chi4Settings.append(pin_settings[i])
		chi4 = wheel.wheel(chi4Settings,0,"Chi4")
		self.chi_wheels.append(chi4)
		
		for i in range(self.CHI4_RANGE,self.CHI5_RANGE):
			chi5Settings.append(pin_settings[i])
		chi5 = wheel.wheel(chi5Settings,0,"Chi5")
		self.chi_wheels.append(chi5)
		
		return self.chi_wheels
	
	# Assembles the m37 and m61 wheels from the provided pin settings		
	def assemble_m_wheels(self, pin_settings):

		m37Settings, m61Settings = [],[]
		
		for i in range(self.M37_RANGE):
			m37Settings.append(pin_settings[i])
		m37 = wheel.mwheel(m37Settings,0,"M37")
		self.m_wheels.append(m37)
		
		for i in range(self.M37_RANGE,self.M61_RANGE):
			m61Settings.append(pin_settings[i])
		m61 = wheel.mwheel(m61Settings,0,"M61")	
		self.m_wheels.append(m61)

		return self.m_wheels
	