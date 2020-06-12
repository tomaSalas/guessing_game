"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

from random import randint

    
        

def intro():
    print("-" * 40)
    print("Welcome to Guessing game, made by Tomas!")
    print("-" * 40)
    
def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
   
    
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    intro()
    highscore = []
    count = 0
    ramdom_number  = randint(1, 10)
    play = 1
    
    
    while (play):
        try:
            number = int(input("Pick a number between 1 and 10: "))
        except ValueError:
            print("Oh no! that is not a correct value for this game, Please try again")
        else:
            if (number >= 1) and (number <= 10):
                if number == ramdom_number:
                    count += 1
                    print("You got it! It took you {} tries".format(count))
                    answer = input("would you like to play again? (y/n):    ")
                    while True:
                        if answer.lower() == "y":
                            intro()
                            highscore.append(count)
                            print("High score to bet " + str(highscore[-1]))
                            count = 0
                            break
                            
                        elif answer.lower() == "n":
                            print("Thank you for playing!")
                            play = 0
                            break
                        else:
                            print("Please choose a valid command! either \'y\' or \'n\'")
                            answer = input("would you like to play again? (y/n):    ")
                            
                elif (ramdom_number < number):
                    print("Lower 💁‍♂️")
                    count += 1
                    continue
                    
                elif (ramdom_number > number):
                    print("Higher 😋")
                    count += 1
                    continue
                else:
                    print("Something when wrong 🤷‍♂️")
            else:
                print("that number is not in the ranged! Selecte a value between 1 and 10!! Try again")
                continue


# Kick off the program by calling the start_game function.
start_game()
