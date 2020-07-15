# put into graph terms
## find get_neighbors
### what are nodes, edges?

# Islands Matrix Problem
# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# islands - connected components

# nodes are items
# edges are the cardinal directions
# for i, j in the 2d array
    # check if it's a one
    # if not, pass
    # if it is, check if visited
    # if it's not, put on the stack
        # while stack > 0
        # current item = stack-pop
        # add current coordinates to visited
        # check neighbors using indices
        # if neighbor is 1, add it to stack

def get_neighbors(node, matrix):
    ## take a step north
    ## take a step south
    ## take a step east
    ## take a step west
    row, col = node
    neighbors = []
    stepNorth = stepSouth = stepWest = stepEast = False
    if row > 0:
        stepNorth = row - 1
    if row < len(matrix) - 2:
        stepSouth = row + 1
    if col < len(matrix[row]) - 1:
        stepEast = col + 1
    if col > 0:
        stepWest = col - 1

    if stepNorth and matrix[stepNorth][col] == 1:
        neighbors.append((stepNorth, col))
    if stepSouth and matrix[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))

    if stepEast and matrix[stepEast][col] == 1:
        neighbors.append((row, stepEast))
    if stepWest and matrix[stepWest][col] == 1:
        neighbors.append((row, stepWest))

    return neighbors


def dft_recursive(node, visited, matrix):
    if node not in visited:
        visited.add(node)

        neighbors = get_neighbors(node, matrix)
        for neighbor in neighbors:
            dft_recursive(neighbor, visited, matrix)

def island_counter(isles, matrix):
    visited = set()
    number_islands = 0

    for row in range(len(isles)):
        for col in range(len(isles[row])):
            node = (row, col)
            if node not in visited and isles[row[col]] == 1:
                number_islands += 1
                dft_recursive(node, visited, matrix)

    return number_islands
