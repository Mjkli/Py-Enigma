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
rotor1b = {}
rotor2 = {}
rotor2b = {}
rotor3 = {}
rotor3b = {}
reflector = {}
rotor1, rotor1b,rotor2, rotor2b,rotor3, rotor3b, reflector = setRotors()

#print(rotor1)
#print(rotor1b)

#file = open('test.txt','r')
file = open('encrypted2.txt','r')
#out = open('encrypted2.txt', 'w')
out = open('test.txt', 'a')

#char = "J"

rt = 1 # Keeps track of how many times a key has been pressed to rotate the rotors
while 1:
    char = file.read(1)
    if not char:
        break
    char = char.upper()
    #print(char)
    if(char.isalpha()):
        char = rotorRun(rotorRun(rotorRun(rotorRun(rotorRun(rotorRun(rotorRun(char,rotor1),rotor2),rotor3),reflector),rotor3b),rotor2b),rotor1b)
        out.write(str(char))
        rotateRotor(rotor1,rotor1b)
        #rotateRotor(rotor1b)
        #if(rt % 26 == 0):
            #rotateRotor(rotor2)
            #rotateRotor(rotor2b)
        #if(rt % 646 == 0):
            #rotateRotor(rotor3)
            #rotateRotor(rotor3b)
    rt += 1
#print(char)


file.close()
out.close()





#choice = input("Use preset settings (y/n) - ")

#if(choice == "y"):
#    pb = setBoard()
#else:
#    customBoard()



