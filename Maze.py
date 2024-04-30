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
    # Find the starting point of the maze
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j


def get_neighbors(maze, row, column):
    # Find the neighbors of the current position
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
    process = queue.Queue()
    
    start = 'O'
    end = 'X'
    str_position = get_start(maze, start)
    
    
    
        
    