import random
from termcolor import colored


def input_username():
    """
    Allows the user to insert a username.
    """

    return input(f"Insert username: \n")


def choose_difficulty():
    """
    Select between three difficulties:
    easy: 5 by 5 grid.
    normal: 7 by 7 grid.
    hard: 10 by 10 grid.
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
            print("    #Invalid difficulty choice")

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
    #    Select a row number (0 to {grid_size - 1}), \
then a column number (0 to {grid_size - 1})
    #    Used coordinates are removed from game!
    #    Good luck!
    {'-'*80}
    """
    print(rules_variable)


def create_grid(grid_size):
    """
    Generates an empty grid.
    Size is based on selected difficulty.
    """

    # The generated grid comes as a list of lists
    return [["." for columns in range(grid_size)] for rows in range(grid_size)]


def ships(grid, grid_size):
    """
    Sets 5 ships randomly on a grid.
    Each ship is marked with an 'O'.
    """

    for _ in range(5):
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        while grid[row][col] == "O":
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
        grid[row][col] = "O"


def print_grid(grid, hide_ships=False):
    """
    Sets up a proper grid from the generated grid (which is a list of lists).
    Cells are separated with a space.
    Has a hide_ship condition that hides the ships 'O',
    by setting them as an empty cell '.'.
    This condition is set as 'True' for computer's grid.
    """

    for row in grid:
        if hide_ships:
            # list comprehension
            # iterating through each cell and hides ships marked 'O' with '.'
            print(" ".join(["." if cell == "O" else cell for cell in row]))
        else:
            # without the join statement to concatanate
            # the elements into a single string
            # (thus also formatting it from a list to a string)
            # the rows will be shown as obvious lists
            # containing string literals
            print(" ".join(row))


def player_turn(player_grid, computer_grid, grid_size, username):
    """
    Allows the player to type in a row, then a column.
    Checks if it is a hit or miss on computer's grid.
    Ships marked with 'O' that are hit are marked 'X'.
    Misses are marked with '+'.
    """

    while True:
        player_guess_row = \
            input(colored("Enter row for computer's grid: ", "yellow"))
        # if string is digit, converts to integer
        if player_guess_row.isdigit():
            player_guess_row = int(player_guess_row)
            if valid_coordinate(player_guess_row, 0, grid_size):
                pass
            else:
                print(f"    #Enter valid row number (0 to {grid_size - 1})")
                continue
        else:
            print(f"    #Enter a valid numeric row.")
            continue

        while True:
            player_guess_col = \
                input(colored("Enter column for computer's grid: ", "yellow"))
            # if string is digit, converts to integer
            if player_guess_col.isdigit():
                player_guess_col = int(player_guess_col)
                # if col within grid, break child loop
                if valid_coordinate(player_guess_row,
                   player_guess_col, grid_size):
                    break
                else:
                    print(f"    #Enter valid column number \
                    (0 to {grid_size - 1})")
            else:
                print(f"    #Enter a valid numeric column.")
        # checks if coordinate (row and col) has already been used
        if computer_grid[player_guess_row][player_guess_col] in ["+", "X"]:
            print(f"    #Enter an unused coordinate (marked as '.')")
        # if coordinate with '.' selected, break parent loop
        else:
            break

    if computer_grid[player_guess_row][player_guess_col] == "O":
        print(colored(f"{username} hit computer's ship!", "blue"))
        computer_grid[player_guess_row][player_guess_col] = "X"
        return True
    else:
        print(f"{username} missed!")
        computer_grid[player_guess_row][player_guess_col] = "+"
        return False


def computer_turn(player_grid, computer_grid, grid_size):
    """
    Allows the computer to select a row, then a column.
    Checks if it is a hit or miss on player's grid.
    Ships marked with 'O' that are hit are marked 'X'.
    Misses are marked with '+'.
    """
    while True:
        computer_guess_row = random.randint(0, grid_size - 1)
        computer_guess_col = random.randint(0, grid_size - 1)

        # Validates computer's choice to only target unused coordinates
        if player_grid[computer_guess_row][computer_guess_col] in [".", "O"]:
            break

    if player_grid[computer_guess_row][computer_guess_col] == "O":
        print(colored("Computer hit player's ship!", "red"))
        player_grid[computer_guess_row][computer_guess_col] = "X"
        return True
    else:
        print("Computer missed!")
        player_grid[computer_guess_row][computer_guess_col] = "+"
        return False


def valid_coordinate(row, col, grid_size):
    """
    Checks if coordinate is valid on grid.
    """

    return 0 <= row < grid_size and 0 <= col < grid_size


def new_game():
    """
    Main game function.
    """

    username = input_username()
    difficulty, grid_size = choose_difficulty()
    rules(difficulty, grid_size)

    player_grid = create_grid(grid_size)
    ships(player_grid, grid_size)

    computer_grid = create_grid(grid_size)
    ships(computer_grid, grid_size)

    player_ships_remaining = 5
    computer_ships_remaining = 5
    player_score = 0
    computer_score = 0

    while True:
        print(colored(f"{username}'s grid: ", "blue") +
              f"score {player_score}")
        print_grid(player_grid)
        print(colored("Computer grid: ", "red") + f"score {computer_score}")
        # computer's ships are hidden
        print_grid(computer_grid, hide_ships=True)

        if player_ships_remaining == 0:
            print(colored("Computer won the game!", "red"))
            break
        elif computer_ships_remaining == 0:
            print(colored(f"{username} won the game!", "blue"))
            break

        if player_turn(player_grid, computer_grid, grid_size, username):
            computer_ships_remaining -= 1
            player_score += 1

        if computer_turn(player_grid, computer_grid, grid_size):
            player_ships_remaining -= 1
            computer_score += 1


while True:
    new_game()

    while True:
        restart = input(f"Play again? (yes/no): \n")
        if restart == "yes":
            print("Restarting game")
            break
        elif restart == "no":
            print("Closing game")
            break
        else:
            print("    #Invalid choice")
    if restart == "yes":
        continue
    break
