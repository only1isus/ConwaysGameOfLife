import numpy as np
import time
import pygame
import random

# a matrix of all zeros
grid = []

# an array of tuple (node, amount of neighbor)
node_neighbor = []

# dimension of the grid
rows = 30
columns = 30

# RGB values of the colors being used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# dimension of the blocks
WIDTH = 15
HEIGHT = 15
MARGIN = 1

# making a grid of all zeros using numpy
grid = np.zeros((rows, columns))

# this function creates a tuple of of random numbers and return them as a tuple
def initilize(max):
    random.seed()
    return [ ( random.randint(1, rows-2), random.randint(1, rows-2) ) for k in range(max) ]

# draw the grid
def drawgrid(g):
    pygame.init()
    WINDOW_SIZE = [HEIGHT*columns+columns*MARGIN, HEIGHT*rows+rows*MARGIN]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(BLACK)
    for row in range(0, g.shape[0]):
        for column in range(0, g.shape[0]):
            if g[row][column] == 1:
                pygame.draw.rect(screen,
                                 RED,
                                 [(MARGIN + WIDTH) * row + MARGIN,
                                  (MARGIN + HEIGHT) * column + MARGIN,
                                  WIDTH,
                                  HEIGHT])
            else:
                pygame.draw.rect(screen,
                                 WHITE,
                                 [(MARGIN + WIDTH) * row + MARGIN,
                                  (MARGIN + HEIGHT) * column + MARGIN,
                                  WIDTH,
                                  HEIGHT])
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            break
        break


# finding neighbors for a given cell
def find_neighbors(grid, starting_points):
    current_grid = grid[:]
    for row in range(grid.shape[0]-1):
        for column in range(grid.shape[0]-1):
            get_neighbors(row, column, current_grid)

# this function takes the current row and column and the grid and find the neighors node as a tuple
def get_neighbors(rw, col, cg):
    if not rw and not col:
        neighbors = (rw + 1, col), (rw , col + 1), (rw + 1 , col + 1)
    elif rw == 0:
        neighbors = (rw, col + 1), (rw , col - 1), (rw + 1 , col)
    elif col == 0:
        neighbors = (rw + 1, col), (rw - 1, col), (rw , col + 1)
    else:
        neighbors = (rw + 1, col), (rw - 1, col), (rw , col + 1), (rw , col - 1), (rw + 1, col + 1), (rw - 1, col - 1), (rw + 1, col - 1), (rw - 1, col + 1)

    # finding the amount of LIVE neighbors and returning the value along with the current cell/node as a tuple
    amt = 0
    for n in neighbors:
        if cg[n[0]][n[1]] == 1:
            amt = amt + 1
    node_neighbor.append(((rw, col), amt))

# takes the node and neighbor tuple and the grid and finds the next generation
def generation(node_neighbor, g):
    next_generation = g[:] # make a copy of the current grid and save it in a new array
    for i in range(0, len(node_neighbor)):
        node, amount_of_neighbors = node_neighbor[i]

        # death by isolation
        if amount_of_neighbors <= 1 and g[node[0]][node[1]] == 1:
            next_generation[node[0]][node[1]] = 0

        # case of death by over crowding
        elif amount_of_neighbors >= 4 and g[node[0]][node[1]] == 1:
            next_generation[node[0]][node[1]] = 0

        # case of survival
        elif (amount_of_neighbors in range(2, 4)) and g[node[0]][node[1]] == 1:
            next_generation[node[0]][node[1]] = 1

        # case of birth
        elif amount_of_neighbors == 3 and g[node[0]][node[1]] == 0:
            next_generation[node[0]][node[1]] = 1

# this function takes the starting config and populate the grid with the first few automatas
def populate(starting_points, grid):
    for i in range(0, len(starting_points)):
        x, y = starting_points[i]
        grid[x][y] = 1
    return grid



if __name__ == '__main__':
    starting_points = initilize(250) # start using 250 cells
    staring_condition = populate(starting_points, grid)
    drawgrid(grid)
    # start the main loop
    while 1:
        find_neighbors(staring_condition, starting_points)
        time.sleep(1)
        generation(node_neighbor, grid)
        drawgrid(grid)
