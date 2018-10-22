import numpy as np
import time
import pygame
import random

grid = []

# starting_points = []
node_neighbor = []
rows = 100
columns = 100


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 8
HEIGHT = 8
MARGIN = 1

grid = np.zeros((rows, columns))

def initilize(max):
    random.seed()
    return [ ( random.randint(3, rows-3), random.randint(3, rows-3) ) for k in range(max) ]


# finding neighbors for a given cell
# this function takes the current grid and and find the neighors of the live cells as a tupil
def find_neighbors(grid, starting_points):
    current_grid = grid[:]
    for row in range(grid.shape[0]-1):
        for column in range(grid.shape[0]-1):
            get_neighbors(row, column, current_grid)

def get_neighbors(rw, col, cg):
    if not rw and not col:
        neighbors = (rw + 1, col), (rw , col + 1), (rw + 1 , col + 1)
    elif rw == 0:
        neighbors = (rw, col + 1), (rw , col - 1), (rw + 1 , col)
    elif col == 0:
        neighbors = (rw + 1, col), (rw - 1, col), (rw , col + 1)
    else:
        neighbors = (rw + 1, col), (rw - 1, col), (rw , col + 1), (rw , col - 1), (rw + 1, col + 1), (rw - 1, col - 1), (rw + 1, col - 1), (rw - 1, col + 1)

    amt = 0
    for n in neighbors:
        if cg[n[0]][n[1]] == 1:
            amt = amt + 1
    node_neighbor.append(((rw, col), amt))
    # print(neighbors)

def generation(node_neighbor, g):
    next_generation = g[:]
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

        elif amount_of_neighbors == 3 and g[node[0]][node[1]] == 0:
            next_generation[node[0]][node[1]] = 1

    # print(next_generation)



# this function takes the starting config and populate the grid with the first few automatas
def populate(starting_points, grid):
    for i in range(0, len(starting_points)):
        x, y = starting_points[i]
        grid[x][y] = 1
    # print(grid)
    return grid


def drawgrid(g):
    pygame.init()
    WINDOW_SIZE = [HEIGHT*columns+columns*MARGIN, HEIGHT*rows+rows*MARGIN]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(BLACK)

    """Draw the grid to be used"""

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

if __name__ == '__main__':
    starting_points = initilize(5000)
    print(starting_points)
    staring_condition = populate(starting_points, grid)
    drawgrid(grid)
    while 1:
        find_neighbors(staring_condition, starting_points)
        time.sleep(.1)
        generation(node_neighbor, grid)
        drawgrid(grid)
    # print(node_neighbor)
    # get_neighbors(0, 1)
