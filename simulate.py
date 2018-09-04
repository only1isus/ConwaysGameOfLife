import numpy as np
import time
import pygame

grid = []

starting_config = []
state = []
rows = 10
columns = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 25
HEIGHT = 25
MARGIN = 1

grid = np.zeros((rows, columns))

def start_simulation(iterations):
    # make a copy of the grid so changes can be made
    steps = 0
    amount_of_live_neighbors = 0
    current_grid = grid[:]

    while steps < iterations:
        for origin_row in range(0, rows - 1):
            for origin_column in range(0, columns - 1):
                # find neighbors of current cell and determine if it will live or die
                if origin_row == 0:

                    neighbors = (origin_row + 1, origin_column), (origin_row , origin_column + 1), (origin_row , origin_column - 1), (origin_row + 1, origin_column + 1)
                elif origin_column == 0:
                    neighbors = (origin_row + 1, origin_column), (origin_row - 1, origin_column), (origin_row , origin_column + 1), (origin_row + 1, origin_column + 1)
                else:
                # print(neighbors)
                    neighbors = (origin_row + 1, origin_column), (origin_row - 1, origin_column), (origin_row , origin_column + 1), (origin_row , origin_column - 1), (origin_row + 1, origin_column + 1), (origin_row - 1, origin_column - 1), (origin_row + 1, origin_column - 1), (origin_row - 1, origin_column + 1)
                for neighbor in neighbors:
                    if current_grid[neighbor[0]][neighbor[1]] == 1:
                        amount_of_live_neighbors = amount_of_live_neighbors + 1
                print((origin_row, origin_column) , amount_of_live_neighbors)
                amount_of_live_neighbors = 0
        steps = steps + 1
pygame.init()
WINDOW_SIZE = [HEIGHT*columns+columns*MARGIN, HEIGHT*rows+rows*MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(BLACK)

"""Draw the grid to be used"""

for row in range(0, rows):
    for column in range(0, columns):
        pygame.draw.rect(screen,
                         WHITE,
                         [(MARGIN + WIDTH) * row + MARGIN,
                          (MARGIN + HEIGHT) * column + MARGIN,
                          WIDTH,
                          HEIGHT])
pygame.display.flip()


print('++++++++++++++++++++++++++')
print('After entering starting conditions then enter to start')
print('++++++++++++++++++++++++++')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            start_simulation(1)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            r = int(pos[0] / (MARGIN + WIDTH))
            c = int(pos[1] / (MARGIN + HEIGHT))
            grid[c][r] = 1


    for row in range(0, rows):
        for column in range(0, columns):
            if grid[row][column] == 1:
                color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                pygame.display.flip()
