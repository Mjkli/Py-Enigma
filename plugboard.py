"""This file defines the plugboard funtions and calls"""
# plugboard should map a character to another character.
# A -> E
# E -> A
# This is mapped before the rotors and After the rotors
# dictionary = hashtable


class TwoWayDict(dict):
    """Class defines a two way dictionary."""
    def setitem(self, key, value):
        """Sets values in the Two way dictionary"""
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
        #"""Returns the number of connections"""
        return dict.__len__(self) / 2

    def get(self,key):
        if key in self:
            return self[key]
        return key


def set_board():
    """Sets up plugboard"""
    option = input("Would you like to customize the plug board? (Y/n)")
    if option == 'Y':
        return custom_board()

    board = TwoWayDict()
    alpha = "ABCDEFGHIJ"
    backwards_alpha = "ZYXWVUTSRQ"
    for i in range(0, 10):
        board[alpha[i]] = backwards_alpha[i]

    return board

def test_build():
    """Used to bypass user input for automatic builds."""
    board = TwoWayDict()
    alpha = "ABCDEFGHIJ"
    backwards_alpha = "ZYXWVUTSRQ"
    for i in range(0, 10):
        board[alpha[i]] = backwards_alpha[i]

    return board


def plugboard_run(char, board):
    """returns plugboard value"""
    return board.get(char)


def custom_board():
    """Sets up a custom board setting"""
    #
    #    Later iterations should have something like this as output for User:
    #    this will help them keep track of what needs connecting.
    #    Also
    #    A -
    #    B -
    #    C -
    #    D -
    #    E -
    #
    print("Connecting Plugboard:")
    print("10 cables comes standard with Enigma.")
    print("Input will be like: A <--> B")
    print("Input 1 to stop adding - Needs to be on Left Character")
    board = TwoWayDict()
    for _ in range(0,10):
        character_a = input("Enter left character: ")
        if character_a == '1':
            break
        character_b = input("Eneter right character: ")
        board.setitem(character_a.upper(),character_b.upper())

    return board
