import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

print("Input Sudoku: \n{}".format(np.matrix(grid)))

# method to check if number n if a viable option in xy position on sudoku grid
def possible(y,x,n):
    global grid

    # check if number n if viable option in y (row)
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    
    # check if number n if viable option in x (column)
    for i in range(0,9):
        if grid[i][x] == n:
            return False

    # check if number n if viable option in 3x3 subgrid
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    
    return True


# recursive method to solve the sudoku grid
def solve():
    global grid

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range (1,10):
                    if possible(y,x,n):
                        grid[y][x] = n # if possible set number
                        solve() # recursion
                        grid[y][x] = 0 # backtracking due to bad choice number
                return
    print("\nOutput Sudoku: \n{}".format(np.matrix(grid)))
    input("\nCheck to see more options?") # allows user to get more solutions if available

solve()