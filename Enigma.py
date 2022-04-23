# Re-creating My enigma encode project in Python

# build rotors
# build plugboard
# run file through

from plugboard import *
from rotors import *

pb = {}

#print("Connecting Plugboard:")
pb = setBoard()
rotor1 = {}
rotor2 = {}
rotor3 = {}
reflector = {}
rotor1, rotor2, rotor3, reflector = setRotors()


file = open('Unencrypted.txt','r')



while 1:
    char = file.read(1)
    if not char:
        break
    char = char.upper()

    if(char.isalpha()):
        print(plugboardRun(char,pb))






file.close()





#choice = input("Use preset settings (y/n) - ")

#if(choice == "y"):
#    pb = setBoard()
#else:
#    customBoard()



