"""
@Purpose: A program that uses the Breadth First search algorithm to solve a maze
@Author: Youssef Ahmed Beshir
@Email: yousssefahmedbeshir@gmail.com
@GitHub: https://github.com/beshirr
"""


import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", " ", " ", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", " ", " ", " ", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#", "#", "#", "#", "#"]
]


def get_start(maze, start):
    # Find the starting point of the maze (O)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j


def get_neighbors(maze, row, column):
    # @Brief: Find the neighbors of the current position
    # @Param: the maze map, and coordinates of the current position
    # @returns: the neighbors of the current position
    neighbors = []
    
    # UP
    if row > 0:
        neighbors.append((row - 1, column))
    # DOWN
    if row + 1 < len(maze):
        neighbors.append((row + 1, column))
    # Left
    if column > 0:
        neighbors.append((row, column - 1))
    # Right
    if column + 1 < len(maze[0]):
        neighbors.append((row, column + 1))
        
    return neighbors


def find_path(maze, stdscr):
    # @Brief: Breadth First search algorithm implementation
    # @Param: Maze map
    # @returns: The shortest path
    process = queue.Queue()
    visited = set()
    
    start = 'O'
    end = 'X'
    str_position = get_start(maze, start)
    
    # Adding the starting position to the Queue
    process.put((str_position, [str_position]))
    
    while not process.empty():
        # If the processing Queue is empty that means that
        # either the end point is found or there is no solution for the maze
        current_position, path = process.get()
        row, column = current_position

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()
        
        if maze[row][column] == end:
            return path

        neighbors = get_neighbors(maze, row, column)
        for neighbor in neighbors:
            # r -> rows, c -> columns
            r, c = neighbor

            if neighbor in visited or maze[r][c] == '#':
                continue

            visited.add(neighbor)
            # Updating the path
            new_path = path + [neighbor]
            process.put((neighbor, new_path))


def print_maze(maze, stdscr, path=None):
    if path is None:
        path = []
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()


wrapper(main)
