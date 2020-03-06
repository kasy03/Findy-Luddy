#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : Kasturi Nikharge  knikharg
#
# Based on skeleton code by Z. Kachwala, 2019


import sys
import json
#defined to keep track of visited map
visited = [] 

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
    #positional argument direction added to the move to keep track of path
    moves=(((row+1,col),'S'), ((row-1,col),'N'), ((row,col-1),'W'), ((row,col+1),'E'))
    
    # Return only moves that are within the board and legal (i.e. on the sidewalk ".") and have not been visited before
    return [ move for move in moves if valid_index(move[0], len(map), len(map[0])) and (map[move[0][0]][move[0][1]] in ".@" ) and (move[0][0],move[0][1]) not in visited ]
     
# Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    fringe=[(you_loc,'',0)]
    while fringe:
        ((curr_move),path,curr_dist)=fringe.pop()
        visited.append(curr_move)
        for move in moves(IUB_map, *curr_move):
            if IUB_map[move[0][0]][move[0][1]]=="@":
                return curr_dist+1,path + move[1]
            else:
                # Path is appended from the move selected to the fringe
                fringe.append(((move[0][0],move[0][1]),path + move[1],curr_dist + 1))
    return 'Inf','' # When no path found return infinite path

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    # Consider non-empty list
    IUB_map = [x for x in IUB_map if x] 
    print("Shhhh... quiet while I navigate!")
    solution,curr_path = search1(IUB_map)
    print("Here's the solution I found:")
    print(solution) if solution=='Inf' else print(str(solution) + " " + curr_path)
    

# In[ ]:




