#This file will create the HumanPlayer class - a subclass of Player

#import the Player parent class
from player import *

class HumanPlayer(Player):
    def make_choice(self):
        choice = input(f"{self.name}, choose rock, papaer, or scissors: ").lower()
        while choice not in ["rock", "paper", "scissors"]:
            choice = input("That was not a valid choice. Try again! Choose rock, paper, or scissors: ").lower()
        self.choice = choice