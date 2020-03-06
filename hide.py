'''
Created on Sep 11, 2019

@author: kastu
'''

#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : Kasturi Nikharge knikharg
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys

visited = []
# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Search for a & if an F is sound in the row, & is pushed into a stack and popped out when F is encountered.
def check_for_building(array, current_pos):
    store_building = [];
    index=current_pos
    if(array[0:current_pos].__contains__('F')):
        while index:
            if array[index]=='&' or array[index]=='@':
                store_building.append('&')
            elif array[index]=='F' :
                if len(store_building) > 0:
                    store_building.pop()
            else:
                return False
        index -= 1
    store_building = [];
    for i in range(current_pos+1,len(array)):
        if(array[i]=='&') or array[index]=='@':
            store_building.append('&')
        elif(array[i]=='F'):
            if len(store_building) > 0:
                store_building.pop()
            else:
                return False
    return True
       
# To check if the (row,col) is a valid position to place an F 
def isValidPosition(board,row,col):
    current_row = board[row][0:len(board[0])]
    current_col=  [board[r][col] for r in range(0,len(board))]
    
    #check for a building in current row and col
    return True if check_for_building(current_row, col) and check_for_building(current_col, row) else False
           

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    # recreate board with copying initial rows and cols and then  F in current row,col position and copy rest of the board 
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]
    

def successors(board):
    # traverse the board and add F at (r,c) if it is a valid position and board on addition of F is not in visited 
    return [ add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' and isValidPosition(board, r, c) and add_friend(board, r, c) not in visited ]
      
# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 



# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    if(K > sum([ row.count('.') for row in initial_board ] )):
        return False
    while len(fringe) > 0:
        visited_path=fringe.pop()
        visited.append(visited_path)
        for s in successors( visited_path ):
            if is_goal(s):
                return(s)
            else:
                fringe.append(s)
    return False

# Main Function
if __name__ == "__main__":
    # Consider non-empty list
    IUB_map = [x for x in parse_map(sys.argv[1]) if x]
    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map) 
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")




