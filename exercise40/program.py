

def es58(lista):
    '''Write the function es58(list) that takes as input
    - a list of strings whose characters are in the set {'N','E','S','O'}

    and destructively modifies it, returning the total number of
    characters present in the list (i.e. the sum of the number of
    characters of the strings in the input list).

    Each string represents a sequence of moves made by a robot on a
    grid: the robot can move from one cell to one of the adjacent
    cells in the 4 directions.  Each character of the string
    represents a move in one of the 4 directions: N stands for a move
    upwards, E for a move towards the right cell, S for one move
    downwards and O for one move towards the left cell.

    Each string in the list represents a path that, from the starting
    cell, makes the robot reaching a certain destination cell.

    At the end of the function each string in the list must be
    replaced by a number.  The number represents the minimum number of
    moves the robot needs to make to get from the starting cell to the
    destination cell, identified by the string.

    For example for list=[ 'NS', 'NEESS', 'NNOOO','NNEESSO'], the
    function returns the number 19 and the list becomes [0,3,5,1].

    '''
    #Enter your code here
