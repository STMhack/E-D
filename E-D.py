import os
import time


class ED:
	def profile():

		os.system('clear')
		time.sleep(1)
		print ('\033[32m  _________	            __________')
		print ('\033[31m |  _______|	           |  ______  \ ')
		print ('\033[32m | |		           | |      \  \ ')
		print ('\033[31m | |_______     _______    | |	     |  |')
		print ('\033[32m |  _______|   |_______|   | |       |  |')
		print ('\033[31m | |		           | |       |  |')
		print ('\033[32m | |_______	           | |______/  /')
		print ('\033[31m |_________|	           |__________/')
		time.sleep(0.5)

	def choice():
		print ('\n\n')

		print ('\033[36m[1] Encrypt File')
		print ('\033[36m[2] Decrypt File')
		print ('\n')

		choice=int(input('\033[32m⟨$⟩ \033[31m '))
		base=int(input('\n\033[32mEnter Base[32/64]: \033[31m'))


		if choice == 1:
			ED.Encrypt(base)

		elif choice == 2:
			ED.Decrypt(base)

		else:
       			print ('\n\033[31mINVALID NUMBER')
	def Encrypt(Enc):
		print ('\n')
		print ('\033[33m[+] Encrypt Starting....\n')
		time.sleep(2)
		E_File=input('\033[32mEnter [Encrypt] File Path:\033[31m ')

		print ('\n\033[35m')
		os.system(f'base{Enc} {E_File}')


	def Decrypt(Dec):
		print ('\n')
		print ('\033[33m[+] Decrypt starting....\n')
		time.sleep(2)
		D_File=input('\033[32mEnter [Decrypt] File Path:\033[31m ')

		print ('\n\033[35m')
		os.system(f'base{Dec} -d {D_File}')

ED.profile()
ED.choice()
