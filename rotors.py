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

        al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        r2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        r3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        re = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

        rotor1 = {}
        rotor1b = {}
        rotor2 = {}
        rotor2b = {}
        rotor3 = {}
        rotor3b = {}
        reflector = {}

        for i in range(0,26):
                rotor1[al[i]] = r1[i]
                rotor1b[r1[i]] = al[i]
                rotor2[al[i]] = r2[i]
                rotor2b[r2[i]] = al[i]
                rotor3[al[i]] = r3[i]
                rotor3b[r3[i]] = al[i]
                reflector[al[i]] = re[i]
    
        return rotor1,rotor1b,rotor2,rotor2b,rotor3,rotor3b,reflector

def rotateRotor(dic,dicb): 
        l = list(dic.keys())
        b = list(dicb.keys())

        #print(b)
        
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




def rotorRun(char,dic):
        #print(dic.get(char))
        return dic.get(char)


        
#dic = {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q', 'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T', 'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H', 'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P', 'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R', 'Y': 'C', 'Z': 'J'}
#dicb = {'E': 'A', 'K': 'B', 'M': 'C', 'F': 'D', 'L': 'E', 'G': 'F', 'D': 'G', 'Q': 'H', 'V': 'I', 'Z': 'J', 'N': 'K', 'T': 'L', 'O': 'M', 'W': 'N', 'Y': 'O', 'H': 'P', 'X': 'Q', 'U': 'R', 'S': 'S', 'P': 'T', 'A': 'U', 'I': 'V', 'B': 'W', 'R': 'X', 'C': 'Y', 'J': 'Z'}
#rotateRotor(dic,dicb)
#print(dic)
#print(dicb)
                
