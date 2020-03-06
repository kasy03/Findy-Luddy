

# Find Luddy
The approach used in this problem is that of a depth first search as we pop out the node which was just inserted. We start from "#" position and insert it into the fringe. Then pop out that node at the top of the fringe to find the possible moves from that node which are safe. All these nodes are then inserted into the fringe. If the next move popped out from the fringe leads you to the destination "@" then goal is reached.

# Code Changes
The existing code had some issues, firstly the IUB map on parsing was adding an empty row to the list, this was handled through traversing the map and only considering non-empty list.
The program often fails to find a solution because the nodes which has been visited already, the existing code was re-visiting those nodes leading to an infinite loop. This is handled using a visited array which stores the moves which have been visited. Thus, saving computation time.
In order to the save the path traversed, direction stringis added to the moves which is then appended to the fringe. So individual element in the fringe stores the distance travelled till the current node as well as the path traversed.


# Assumptions
For the code to execute, the map is required to have only one start position "#" and one destination "@"
A non-empty map is provided.

# Search Abstraction
Set of states : { IUB_map(row,col) where row length(IUB_map) and col € l length(IUB_map)[0] and IUB_map(row,col) = "."}

Initial state : { IUB_map(row,col)="#" }

Successor function : {IUB_map(row,col) where IUB_map(row,col) = "." and cost(curr_pos -&gt; IUB(row,col)) =1 }

Goal State: {IUB_map(row,col) where IUB_map(row,col) = "@"}

Cost : cost incurred to travel from one node to another is 1 given that the node is neighboring node.





# Hide-and-seek

Given an empty map, we must place K friends on the map, such that no friend can see each other i.e. an "&" is in between them. A friend can however see me ("#"). We start from position (0,0) and traverse till (r,c) where r is the number of rows and c is the number of columns. We check if the given position has an "F" in the row or column and if there does exist an "&" between them. All the "F" are placed in a similar fashion. And goal state is reached when all the friends are placed on the map such that they do not see each other.

# Code Changes

A non-empty map is traversed, we find the successors such that an "F" can be placed on the ".". So initially, we start with a set of successors, where a map as one "F". So after the first call to the successor function, the number of elements it returns m maps where m is equivalent to the sidewalks in the map.
An initial condition is checked, where the number of sidewalks (".") in the map is greater than the number of friends to be placed (K). This avoids additional computation and saves time.
An isValidPosition is written which check if the current row contains an "F". If it does then it calls another function check_for_building which checks if a building exists between the two friends.
The function check_for_building has input parameters, a 1D array which corresponds to either the current row or the current column and the current position (i). We traverse from i to the 0 as well from i to length(array). If an "&" is encountered. It is inserted into a stack which pops out an element when "F" is encountered. So if there exists a non-empty stack when we encounter an "F" then it a valid position.
A visited array stores every element which is popped from the fringe and thus that element is not re-visited saving computation time.

# Search Abstraction

Set of states : { IUB_map where IUB_map contains n "F" where n € [0,K]}

Initial state : { Empty board with no "F" }

Successor function : {IUB_map where IUB_map has n "F" where n&lt;K}

Goal State: {IUB_map where IUB_map has K "F"}
