# ------------------ BEGIN: Import --------------------
import random
# ------------------ END: Import ----------------------

# ------------------ BEGIN: Constants and global variables ---------------
# ------------------ END: Constants and global variables -----------------

# ------------------ BEGIN: Functions ------------------------------------
# ------------------ END: Functions --------------------------------------

# ------------------ BEGIN: Main function ------------------------------------
def main ():
    # Tell the user the instructions about the game
    print ("Welcome to roll a dice!")
    print ("")

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
    print ("I roll the dices")
    print ("Blue dice:", blue_dice)
    print ("Red dice:", red_dice)
# ------------------ END: Main function --------------------------------------

# ------------------ BEGIN: Entrance path ------------------------------------
if __name__ == "__main__":
    main()
# ------------------ END: Entrance path --------------------------------------