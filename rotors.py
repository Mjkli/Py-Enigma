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

        for i in range(0,26):
                rotor1[alpha[i]] = r1_set[i]
                rotor1b[r1_set[i]] = alpha[i]
                rotor2[alpha[i]] = r2_set[i]
                rotor2b[r2_set[i]] = alpha[i]
                rotor3[alpha[i]] = r3_set[i]
                rotor3b[r3_set[i]] = alpha[i]
                reflector[alpha[i]] = re_set[i]
    
        return rotor1,rotor1b,rotor2,rotor2b,rotor3,rotor3b,reflector

def rotate_rotor(dic,dicb): 
        """function rotates rotors"""
        l = list(dic.keys())
        b = list(dicb.keys())
        temp = dic[l[0]]
        tempVal = l[l.__len__() - 1]
        
        
        for i in range(0,dic.__len__() - 1):
                dic[l[i]] = dic[l[i+1]]
        
        dic[tempVal] = temp


        tempkey = b[0]
        tempVal = dicb[b[dicb.__len__() - 1]]
 
        for i in range(dicb.__len__() - 1, 0, -1):
                dicb[b[i]] = dicb[b[i-1]]
                
                

        dicb[tempkey] = tempVal




def rotor_run(char,dic):
        """Gets value of rotor"""
        return dic.get(char)
                
