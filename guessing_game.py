"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

from random import randint
    

def lines():
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
    lines()
    print("Welcome to Guessing game, made by Tomas!")
    lines()
    count = 0
    ramdom_number  = randint(1, 10)
    while True:
        
        number = int(input("Pick a number between 1 and 10: "))
        
        if number == ramdom_number:
            count += 1
            print("You got it! It took you {} tries".format(count))
            answer = input("would you like to play again? (y/n):    ")
            if answer.lower() == "y":
                start_game()
                
            elif answer.lower() == "n":
                print("Thank you for playing!")
                break
            
        elif (ramdom_number < number):
            print("Lower 💁‍♂️")
            count += 1
            continue
            
        elif (ramdom_number > number):
            print("Higher 😋")
            count += 1
            continue
        else:
            print("That is not a valid input, please try again 🙈")
  


# Kick off the program by calling the start_game function.
start_game()
