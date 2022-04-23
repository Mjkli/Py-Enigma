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
def setRotors():

        al = "ABCDEFGHIJKLMNPOQRSTUVWXYZ"
        r1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        r2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        r3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        re = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

        rotor1 = {}
        rotor2 = {}
        rotor3 = {}
        reflector = {}
        for i in range(0,26):
                rotor1[al[i]] = r1[i]
                rotor2[al[i]] = r2[i]
                rotor3[al[i]] = r3[i]
                reflector[al[i]] = re[i]
    
        return rotor1,rotor2,rotor3,reflector

