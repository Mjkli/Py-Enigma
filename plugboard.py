
# plugboard should map a character to another character.
# A -> E
# E -> A
# This is mapped before the rotors and After the rotors
# dictionary = hashtable
class TwoWayDict(dict):
    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2

def setBoard():
    board = TwoWayDict()
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    la = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    for i in range(0,25):
        board[al[i]] = la[i]

    return board




def customBoard():
    """
        Later iterations should have something like this as output for User:
        this will help them keep track of what needs connecting.
        Also
        A - 
        B - 
        C - 
        D -
        E - 
    """




pb = TwoWayDict()

pb = setBoard()

print(pb)

#print("Connecting Plugboard:")
#choice = input("Use preset settings (y/n) - ")

#if(choice == "y"):
#    pb = setBoard()
#else:
#    customBoard()


#print(pb)


