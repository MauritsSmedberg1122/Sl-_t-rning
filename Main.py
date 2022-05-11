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

def calculation(user_calculation, dices):
    result = 0
    operation = "+"

    # Look through all characters in the users calculation.
    for letter in user_calculation:

        # Control if the letter is a number
        if letter.isdigit():
            number = int(letter)

            # Control if the number is in dices
            if number in dices:
                # Remove number from dices
                dices.remove(number)
            else:
                speech("You used a non-existing number", 1)
                return False
            
            # Adding the different calculations
            if operation == "+":
                result = result + number
            elif operation == "-":
                result = result - number
            elif operation == "/":
                result = result / number
            elif operation == "*":
                result = result * number
            else:
                speech("You typed the wrong calculation.", 1)
                return False
        
        else:
            # Change the calculation.
            operation = letter

    return result

# ------------------ END: Functions --------------------------------------

# ------------------ BEGIN: Main function ------------------------------------
def main():
    # Tell the user the instructions about the game
    speech("Welcome to roll a dice!", 1) 

    speech(f"In this game, your task is to first roll the dice. Then, with the help of\nmathematics\n(plus, minus, times and divided)\nyou should get the result to the result of blue and white dice together.\nGood luck!", 1.5)

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
    speech("Now it's time to start calculating! Input your guess:", 1)
    user_calculation = input()
    user_result = calculation(user_calculation, white_dices) 
    speech(f"Your answer was {user_result}", 1)
    if goal == user_result:
        speech("You won!", 1)
    else:
        speech("You lost!", 1)
    # ------------------ END: Main function --------------------------------------

# ------------------ BEGIN: Entrance path ------------------------------------
if __name__ == "__main__":
    play_again = "Yes"
    while play_again == "Yes":
        main()
        speech("If you want to play again type 'Yes'", 1)
        play_again = input()

        
    
# ------------------ END: Entrance path --------------------------------------