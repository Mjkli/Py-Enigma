# Re-creating My enigma encode project in Python

# build rotors
# build plugboard
# run file through

from plugboard import setBoard
from rotors import *

pb = {}

#print("Connecting Plugboard:")
pb = setBoard()
rotor1 = {}
rotor2 = {}
rotor3 = {}
reflector = {}
rotor1, rotor2, rotor3, reflector = setRotors()


rotor1 = rotateRotor(rotor1)







#choice = input("Use preset settings (y/n) - ")

#if(choice == "y"):
#    pb = setBoard()
#else:
#    customBoard()



