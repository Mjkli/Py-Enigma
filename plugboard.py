"""This file defines the plugboard funtions and calls"""
# plugboard should map a character to another character.
# A -> E
# E -> A
# This is mapped before the rotors and After the rotors
# dictionary = hashtable


class TwoWayDict(dict):
    """Class defines a two way dictionary."""
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


def set_board():
    """Sets up plugboard"""
    board = TwoWayDict()
    alpha = "ABCDEFGHIJ"
    backwards_alpha = "ZYXWVUTSRQ"
    for i in range(0, 10):
        board[alpha[i]] = backwards_alpha[i]

    return board
    #return board{'E': 'A', 'K': 'B', 'M': 'C', 'F': 'D', 'L': 'E', 'G': 'F', 'D': 'G', 'Q': 'H', 'V': 'I', 'Z': 'J', 'N': 'K', 'T': 'L', 'O': 'M', 'W': 'N', 'Y': 'O', 'H': 'P', 'X': 'Q', 'U': 'R', 'S': 'S', 'P': 'T', 'A': 'U', 'I': 'V', 'B': 'W', 'R': 'X', 'C': 'Y', 'J': 'Z'}


def plugboard_run(char, board):
    """returns plugboard value"""
    return board.get(char)


# def custom_board():
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
# print("Connecting Plugboard:")
# choice = input("Use preset settings (y/n) - ")

# if(choice == "y"):
#    pb = setBoard()
# else:
#    customBoard()


# print(pb)
