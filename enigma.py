"""Re-creating My enigma encode project in Python"""

# build rotors
# build plugboard
# run file through

from plugboard import set_board, plugboard_run
from rotors import rotor_run, rotate_rotor, set_rotors

# print("Connecting Plugboard:")
pb = set_board()
rotor1, rotor1b, rotor2, rotor2b, rotor3, rotor3b, reflector = set_rotors()

with open("Unencrypted.txt", 'r', encoding='utf-8') as file, \
        open('encrypted.txt', 'w', encoding='utf-8') as out:
    # with open('encrypted.txt','r',encoding='utf-8') as file, open('test.txt','a',encoding='utf-8')

    # char = "J"

    KEYS = 1  # Keeps track of how many times a key has been pressed to rotate the rotors
    while 1:
        char = file.read(1)
        if not char:
            break
        char = char.upper()
        if char.isalpha():
            char = plugboard_run(rotor_run(rotor_run(rotor_run(
                   rotor_run(rotor_run(rotor_run(rotor_run(
                    plugboard_run(char, pb),
                    rotor1), rotor2), rotor3), reflector), rotor3b), rotor2b), rotor1b), pb)

        out.write(str(char))
        rotate_rotor(rotor1, rotor1b)
        if KEYS % 26 == 0:
            rotate_rotor(rotor2, rotor2b)
        if KEYS % 646 == 0:
            rotate_rotor(rotor3, rotor3b)
        KEYS += 1
