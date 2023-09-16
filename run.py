import random

def choose_difficulty():
    """
    Select between three difficulties:
    easy: 5 by 5 grid
    normal: 7 by 7 grid
    hard: 10 by 10 grid
    """

    while True:
        difficulty = input(f"Insert difficulty (easy/normal/hard): \n")

        if difficulty == "easy":
            grid_size = 5
            break
        elif difficulty == "normal":
            grid_size = 7
            break
        elif difficulty == "hard":
            grid_size = 10
            break
        else:
            print("Invalid difficulty choice")

    return difficulty, grid_size

def rules(difficulty, grid_size):
    """
    Prints the rules for the chosen difficulty of the game.
    """

    rules_variable = f"""
    {'-'*80}
    #    Welcome to BATTLESHIPS the game!
    #    Difficulty: {difficulty}
    #    Map size: {grid_size} by {grid_size} grid
    #
    #    Rules:
    #    Sink the computer's 5 ships before it sinks yours!
    #    You and the computer have each a separate grid with 5 ships
    #    Select a row number (0 to {grid_size - 1}), then a column number (0 to {grid_size - 1})
    #    Used coordinates are removed from game!
    #    Good luck!
    {'-'*80}
    """
    print(rules_variable)

def create_grid(grid_size):
    return [["." for columns in range(grid_size)] for rows in range(grid_size)]

def player_ships(grid):
    """
    Sets 5 ships randomly on player's grid
    Each ship is marked with an 'O'
    """
    for _ in range(5):
        row, col = random.randint(0, 4), random.randint(0, 4)
        while grid[row][col] == "O":
            row, col = random.randint(0, 4), random.randint(0, 4)
        grid[row][col] = "O"

def computer_ships(grid):
    """
    Sets 5 ships randomly on computer's grid
    Each ship is marked with an 'O'
    """
    for _ in range(5):
        row, col = random.randint(0, 4), random.randint(0, 4)
        while grid[row][col] == "O":
            row, col = random.randint(0, 4), random.randint(0, 4)
        grid[row][col] = "O"

def print_player_grid(grid):
    """
    Sets up player's grid and separates the dots with a space
    """
    print("Player grid:")
    for row in grid:
        print(" ".join(row)) # without the join statement to concatanate the elements into a single string (thus also formatting it from a list to a string), the rows will be shown as obvious lists containing string literals

def print_computer_grid(grid):
    """
    Sets up computer's grid and separates the dots with a space
    """
    print("Computer grid:")
    for row in grid:
        print(" ".join(row)) # without the join statement to concatanate the elements into a single string (thus also formatting it from a list to a string), the rows will be shown as obvious lists containing string literals

def player_turn(player_grid, computer_grid, grid_size):
    """
    Allows the player to type in a row, then a column
    Checks if it is a hit or miss on computer's grid
    Ships marked with 'O' that are hit are marked 'X'
    Misses are marked with '+'
    """
    while True:
        player_guess_row = int(input("Enter row for computer's grid: "))
        if valid_coordinate(player_guess_row, 0, grid_size):
            break
        else:
            print(f"    #Enter valid row number (0 to {grid_size - 1})")
    
    while True:
        player_guess_col = int(input("Enter column for computer's grid: "))
        if valid_coordinate(player_guess_row, player_guess_col, grid_size):
            break
        else:
            print(f"    #Enter valid column number (0 to {grid_size - 1})")
    
    if computer_grid[player_guess_row][player_guess_col] == "O":
        print("Player hit computer's ship!")
        computer_grid[player_guess_row][player_guess_col] = "X"
    else:
        print("Player missed!")
        computer_grid[player_guess_row][player_guess_col] = "+"

def computer_turn(player_grid, computer_grid, grid_size):
    """
    Allows the computer to select a row, then a column
    Checks if it is a hit or miss on player's grid
    Ships marked with 'O' that are hit are marked 'X'
    Misses are marked with '+'
    """
    computer_guess_row = random.randint(0, grid_size - 1)
    computer_guess_col = random.randint(0, grid_size - 1)
    
    if player_grid[computer_guess_row][computer_guess_col] == "O":
        print("Computer hit player's ship!")
        player_grid[computer_guess_row][computer_guess_col] = "X"
    else:
        print("Computer missed!")
        player_grid[computer_guess_row][computer_guess_col] = "+"

def valid_coordinate(row, col, grid_size):
    """
    Checks if coordinate is valid on grid
    """
    return 0 <= row < grid_size and 0 <= col < grid_size

def new_game():
    difficulty, grid_size = choose_difficulty()
    rules(difficulty, grid_size)
    #print(create_grid(grid_size))

    player_grid = create_grid(grid_size)
    player_ships(player_grid)
    print_player_grid(player_grid)

    computer_grid = create_grid(grid_size)
    player_ships(computer_grid)
    print_computer_grid(computer_grid)

    player_turn(player_grid, computer_grid, grid_size)
    computer_turn(player_grid, computer_grid, grid_size)

    print_player_grid(player_grid)
    print_computer_grid(computer_grid) # updates computer grid after player input

new_game()
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high