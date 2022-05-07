# ------------------ BEGIN: Import --------------------
import random
from time import sleep
# ------------------ END: Import ----------------------

# ------------------ BEGIN: Constants and global variables ---------------
# ------------------ END: Constants and global variables -----------------

# ------------------ BEGIN: Functions ------------------------------------
def speech(words, time_in_seconds):
    for char in words:
        sleep(0.05)
        print(char, end="", flush=True)

    print()
    sleep(time_in_seconds)

def calcution(user_calculation, dices):
    # user_calculation = "1+2*3-4+5"
    # dices = [1,2,3,4,5]

    # Gå igenom varje bokstav/siffra i texten och kontrollera vad du ska 
    
    # I slutet vill vi ha ett tal som är:
    # goal = 1+2*3-4+5 = 10

    # Look through all characters in the users calculation.
    goal = 0
    for letter in user_calculation:
        # Control if the letter is a number
        if letter.isdigit():
            pass
    return goal

# ------------------ END: Functions --------------------------------------

# ------------------ BEGIN: Main function ------------------------------------
def main():
    # Tell the user the instructions about the game
    speech("Welcome to roll a dice!", 1) 

    words = f"In this game, your task is to first roll the dice. Then, with the help of mathematics, you should get the result to a number.\nGood luck!"
    speech(words, 1.5)

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
    speech("I roll the dices", 1) 
    speech(f"Blue dice: {blue_dice}", 0.5) 
    speech(f"Red dice: {red_dice}", 0.5) 
    speech(f"White dices: {white_dices}", 2)

    speech(f"To win you should get the result: {goal}", 1)

    # Now it is time for the user to input his guess.
    # When we have the input call the calculation function.
# ------------------ END: Main function --------------------------------------

# ------------------ BEGIN: Entrance path ------------------------------------
if __name__ == "__main__":
    main()
# ------------------ END: Entrance path --------------------------------------