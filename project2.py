from hashlib import new
import sys
#
# CIS 500, Fall 2022, Project 2 - Game of Life
#

#
# Funtion that reads the contents of a given file, creates, and
# returns the initial grid (as a list of lists) for the game. The
# file contains just a single line of values.
# 
# You can assume that the contents of the file adhere to the following
# format conventions:
#   - File contains only integers
#   - The first number is the length (rows) of the grid
#   - The second number is the width (columns) of the grid
#   - The remaining values are only 0s and 1s indicating if a cell is dead or live
#   - After the first two numbers, there will be rows * columns number of values
#     (values of first row followed by values of second row and so on)
# 
def create_grid_from_file(filename):
    
    with open(filename) as f:
        line = f.readline()
        f.close()
    cell_states = line.split(" ")[2:]
    cell_states = [int(i) for i in cell_states]
    l,w = line.split(" ")[:2]
    l,w = int(l),int(w)
    grid = [[0]*l]*w

    for i in range(l):
        grid[i] = cell_states[i*l:(i+1)*l]
    return grid


#
# Function that saves the current state of a grid to the file specified
# following the file format conventions described above (also in the project specifications).
#
def save_grid_to_file(filename, grid):
    with open(filename,"w") as f:
        f.write(str(len(grid))+" ")
        f.write(str(len(grid[0]))+" ")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                f.write(str(grid[i][j])+" ")
        f.write("\n")
        f.close()


#
# Function that returns the grid contents as a string in the format specified below
# as demonstrated using an example grid:
#
# Example input grid: [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# String returned: '. . . . .\n. . X . .\n. . X . .\n. . X . .\n. . . . .'
#
# Make sure to strip off any leading and trailing whitespace before the string is returned.
#
def grid_as_string(grid):
    gridString = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                gridString += "."
            else:
                gridString += "X"
            if j<len(grid[0])-1:
                gridString += " "
        if i<len(grid)-1:
            gridString += "\n"
    return gridString


#
# Function that makes a deep copy of the given grid and returns it.
# Do not use copy.deepcopy() function.
#
def copy_grid(grid):
    l,w = len(grid),len(grid[0])
    new_grid = []
    for i in range(l):
        new_grid.append([])
        for j in range(w):
            new_grid[i].append(grid[i][j])
    return new_grid


#
# Function that mutates the given grid and returns the result as a new grid.
# It does not alter the input grid. It makes a copy (using copy_grid function)
# of the input grid, advances it to next generation by making appropriate changes,
# and returns the new grid.
#
def mutate_grid(grid):

    new_grid = copy_grid(grid)

    #print(get_nbr_of_neighbors(0,3,grid))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            alive_neighbours = get_nbr_of_neighbors(i,j,grid)

            if grid[i][j] == 1:
                if alive_neighbours<2:
                    new_grid[i][j] = 0
                elif alive_neighbours ==2 or alive_neighbours ==3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
                
            if grid[i][j] == 0:
                if alive_neighbours == 3:
                    new_grid[i][j] = 1

    return new_grid


#
# Function that returns the number of live neighbors of a cell at
# position [row,col] in the grid.
#
def get_nbr_of_neighbors(row,col,grid):
    neighbours = []
    l,w = len(grid),len(grid[0])
    
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if (-1 < row <= l and -1 < col <= w and (row != i or col != j) and (0 <= i <= l) and (0 <= j <= w)):
    #             neighbours.append(grid[i][j])
    
    for i in range(max(0,row-1),min(l,row+2)):
        for j in range(max(0,col-1),min(w,col+2)):
            if (row,col)==(i,j):
                continue
            #print(grid[i][j])
            neighbours.append(grid[i][j])
    alive_neighbours = neighbours.count(1)
    return alive_neighbours


#
# Driver to play the game from command line.
# WARNING: DO NOT MAKE ANY CHANGES TO THIS FUNCTION
#
def main():
    if len(sys.argv) != 2:
        print('Usage error - This program requires a filename as argument')
        print('Correct usage: python project2.py filename')
        print('Example: python project2.py beacon.txt')
        sys.exit()
    grid = create_grid_from_file(sys.argv[1])
    print(grid_as_string(grid) + '\n')
    while(True):
        response = input('Press q to quit, n to iterate, w to save to file, or any other key to move to next generation: ')
        response = response.upper()
        if response == 'Q':
            print('Exiting the program.')
            sys.exit()
        elif response == 'W':
            filename = input('Enter a filename to save the grid to: ')
            save_grid_to_file(filename,grid)
            print('Grid saved to file %s' % filename)
        elif response == 'N':
            nbr = int(input('How any iterations? '))
            for i in range(nbr):
                grid = mutate_grid(grid)
                print(grid_as_string(grid) + '\n')
        else:
            grid = mutate_grid(grid)
            print(grid_as_string(grid) + '\n')


# run main to play the game if this script is executed as a top-level program
if __name__ == '__main__':
    main()
