rules_variable = f"""
{'-'*80}
#    Welcome to BATTLESHIPS the game!
#    Difficulty: easy
#    Map size: 5 by 5 grid
#
#    Rules:
#    Sink the computer's 5 ships before it sinks yours!
#    You and the computer have each a separate grid with 5 ships
#    Select a row number (0 to 4), then a column number (0 to 4)
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