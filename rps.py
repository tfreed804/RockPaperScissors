#This is my first fully independent project - Rock, Paper, Scissors

#import required libraries
import random
from Player import *
from HumanPlayer import *
from ComputerPlayer import *

#Create an object for HumanPlayer
player_1 = HumanPlayer("")

#Create an object for ComputerPlayer
player_2 = ComputerPlayer("CPU")

#Define win conditions
win_conditions = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

#Ask the User for their name
player_1.name = input("Enter your name: ")


#The main function will contain the game loop
def main():
    
    #create a variable to count the current round number
    round_num = 1
    
    #Begin the loop
    while True:
        #display round information
        print(f"\n--- Round {round_num} ---\n")
        print(f"{player_1.name}: {player_1.score}")
        print(f"{player_2.name}: {player_2.score}\n")

        #User and CPU will make their choices
        player_1.make_choice()
        player_2.make_choice()

        #Store choices in a variable to for conditional checks + to be displayed
        choice_1 = player_1.get_choice()
        choice_2 = player_2.get_choice()

        #Display choices
        print(f"\n{player_1.name} chose {choice_1}...")
        print(f"{player_2.name} chose {choice_2}...")

        #Check conditions for a winner
        if choice_1 == choice_2:
            print("\nIt's a draw!")
        elif win_conditions[choice_1] == choice_2:
            print(f"\n{player_1.name} wins!")
            player_1.update_score()
        else:
            print(f"\n{player_2.name} wins!")
            player_2.update_score()

        #Ask if user wants to play again
        rematch = input("Would you like to play again? (y/n): ").lower()

        #Check conditions for user response
        if rematch != "y" and rematch != "n":
            rematch = input("That input was not valid. Would you like to play again? (y/n): ").lower()
        elif rematch == "y":
            round_num += 1
            continue
        elif rematch == "n":
            print("\nThanks for playing!")
            print("The final scores are... ")
            print(f"\n{player_1.name}: {player_1.score}")
            print(f"{player_2.name}: {player_2.score}")
            break


#Call the main function to run the game
main()