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
out = open('encrypted.txt', 'w')


rt = 1 # Keeps track of how many times a key has been pressed to rotate the rotors
while 1:
    char = file.read(1)
    if not char:
        break
    char = char.upper()

    if(char.isalpha()):
        rotateRotor(rotor1)
        char = plugboardRun(rotorRun(rotorRun(rotorRun(rotorRun(rotorRun(rotorRun(rotorRun(plugboardRun(char,pb),rotor1),rotor2),rotor3),reflector),rotor3),rotor2),rotor1),pb)

    out.write(str(char))
    if(rt % 26 == 0):
        rotateRotor(rotor2)
    if(rt % 646 == 0):
        rotateRotor(rotor3)
    rt += 1



file.close()
out.close()





#choice = input("Use preset settings (y/n) - ")

#if(choice == "y"):
#    pb = setBoard()
#else:
#    customBoard()



