import turtle
import random

# Setup turtle
screen = turtle.Screen()
screen.title("Sudoku Grid")
t = turtle.Turtle()
t.speed(0)

def draw_grid():
    # Draw the outer grid
    t.penup()
    t.goto(-180, 180)
    t.pendown()
    t.pensize(3)
    for _ in range(4):
        t.forward(360)
        t.right(90)

    # Draw the inner lines
    for i in range(1, 9):
        t.penup()
        t.goto(-180 + i * 40, 180)
        t.pendown()
        t.pensize(3 if i % 3 == 0 else 1)
        t.right(90)
        t.forward(360)
        t.left(90)

    for i in range(1, 9):
        t.penup()
        t.goto(-180, 180 - i * 40)
        t.pendown()
        t.pensize(3 if i % 3 == 0 else 1)
        t.forward(360)

def draw_numbers(grid):
    t.penup()
    start_x, start_y = -160, 160
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                t.goto(start_x + j * 40, start_y - i * 40 - 10)
                t.write(grid[i][j], align="center", font=("Arial", 18, "normal"))

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def generate_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                num = random.randint(1, 9)
                while not is_valid(grid, i, j, num):
                    num = random.randint(1, 9)
                grid[i][j] = num
                if not solve_sudoku(grid):
                    grid[i][j] = 0
                    continue
                return True
    return False

def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def create_puzzle(grid, num_holes=40):
    count = 0
    while count < num_holes:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            count += 1

# Create a blank grid
sudoku_grid = [[0]*9 for _ in range(9)]

# Generate a complete Sudoku grid
generate_sudoku(sudoku_grid)

# Create a Sudoku puzzle by removing some numbers
create_puzzle(sudoku_grid)

# Draw the Sudoku grid
draw_grid()

# Draw the numbers on the Sudoku grid
draw_numbers(sudoku_grid)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
