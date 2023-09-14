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

def rules():
    print(rules_variable)

rules()
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high