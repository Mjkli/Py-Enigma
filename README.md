# Py-Enigma
Python program to Encrypt files using enigma.

Enigma is the machine used by the germans during WW2 to encrypt messages.
This python code follows the outline of how they did that.

First a letter is read in from a file.
The letter is converted to another letter in the plugboard.

Then the output from the plugboard is sent to the rotors where it is adjusted more.
The rotors rotate in 3 variations depending on how many keys are pressed.
first rotor every key
second rotor after full rotation from first rotor
3rd rotor after full rotation from second rotor
after the letter is outputed from the rotors then it is sent back to the plugboard to be moved again.
then the plugboard outputs the final letter.
