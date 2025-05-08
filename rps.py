#This is my first fully independent project - Rock, Paper, Scissors
import random
import sys

def main():
    while True:
        num_players = input("Are there 1 or 2 players? ")
    
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