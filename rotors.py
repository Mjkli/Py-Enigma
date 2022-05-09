"""
Entry = ABCDEFGHIJKLMNOPQRSTUVWXYZ (rotor right side)
        ||||||||||||||||||||||||||
I     = EKMFLGDQVZNTOWYHXUSPAIBRCJ
II    = AJDKSIRUXBLHWTMCQGZNPYFVOE
III   = BDFHJLCPRTXVZNYEIWGAKMUSQO
IV    = ESOVPZJAYQUIRHXLNFTGKDCMWB
V     = VZBRGITYUPSDNHLXAWMJQOFECK
UKW-B = YRUHQSLDPXNGOKMIEBFZCWVJAT
"""


def set_rotors():
    """setup rotors"""

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r1_set = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    r2_set = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    r3_set = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    re_set = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    rotor1 = {}
    rotor1b = {}
    rotor2 = {}
    rotor2b = {}
    rotor3 = {}
    rotor3b = {}
    reflector = {}
    for i in range(0, 26):
        rotor1[alpha[i]] = r1_set[i]
        rotor1b[r1_set[i]] = alpha[i]
        rotor2[alpha[i]] = r2_set[i]
        rotor2b[r2_set[i]] = alpha[i]
        rotor3[alpha[i]] = r3_set[i]
        rotor3b[r3_set[i]] = alpha[i]
        reflector[alpha[i]] = re_set[i]

    return rotor1, rotor1b, rotor2, rotor2b, rotor3, rotor3b, reflector


def rotate_rotor(dic, dicb):
    """function rotates rotors"""
    forward = list(dic.keys())
    backward = list(dicb.keys())
    temp_key = dic[forward[0]]
    temp_value = forward[forward.__len__() - 1]

    for i in range(0, dic.__len__() - 1):
        dic[forward[i]] = dic[forward[i+1]]

    dic[temp_value] = temp_key
    temp_key = backward[0]
    temp_value = dicb[backward[dicb.__len__() - 1]]

    for i in range(dicb.__len__() - 1, 0, -1):
        dicb[backward[i]] = dicb[backward[i-1]]

    dicb[temp_key] = temp_value


def rotor_run(char, dic):
    """Gets value of rotor"""
    return dic.get(char)
