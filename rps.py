#This is my first fully independent project - Rock, Paper, Scissors

#import required libraries
import random

#The main function will contain the game loop
def main():

    #Begin the loop
    while True:

        #Ask the user for the number of players for this game session
        num_players = input("Are there 1 or 2 players? ")

        #Validate user input. If valid, ask for player name(s)
        #If invalid, ask the user again.
        if num_players == "2":
            player1 = input("Enter the name for player 1: ")
            player2 = input("Enter the name for player 2: ")
        elif num_players == "1":
            player1 = input("Enter the name for player 1: ")
            player2 = "CPU"
        else:
            print("This was not valid input! Try again.")
            continue





        
main()