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

def rotateRotor(dic):
        print(dic)
        l = list(dic.keys())
        temp = dic[l[0]]
        tempVal = l[l.__len__() - 1]
        
        
        for i in range(0,dic.__len__() - 1):
                   dic[l[i]] = dic[l[i+1]]
        
        dic[tempVal] = temp
        
                
                
