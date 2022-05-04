# ------------------ BEGIN: Import --------------------
import random
from time import sleep
import sys
import os
# ------------------ END: Import ----------------------

# ------------------ BEGIN: Constants and global variables ---------------
# ------------------ END: Constants and global variables -----------------

# ------------------ BEGIN: Functions ------------------------------------
words=""
def speech():
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    print(os.linesep)
# ------------------ END: Functions --------------------------------------

# ------------------ BEGIN: Main function ------------------------------------
def main():
    global words
    # Tell the user the instructions about the game
    words = "Welcome to roll a dice!"
    speech() 
    sleep(1)
    words = f"In this game, your task is to first roll the dice. Then, with the help of mathematics, you should get the sum to 25.{os.linesep}Good luck!"
    speech()
    sleep(1.5)
    # Throw the blue and red dice
    red_dice = random.randrange (1, 7)
    blue_dice = random.randrange (1, 7)

    # Create a 2 digit number 
    goal = red_dice + 10*blue_dice
    
    # Throw the 5 white dices
    white_dices = []
    for repeat in range (5):
        white_dice = random.randrange (1, 7 )
        white_dices.append(white_dice)

    # Show the user the dices
    words = "I roll the dices"
    speech() 
    sleep(1)
    words = f"Blue dice: {blue_dice}"
    speech() 
    sleep(0.5)
    words = f"Red dice: {red_dice}"
    speech() 
# ------------------ END: Main function --------------------------------------

# ------------------ BEGIN: Entrance path ------------------------------------
if __name__ == "__main__":
    main()
# ------------------ END: Entrance path --------------------------------------