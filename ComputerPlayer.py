#This file will create the ComputerPlayer class - a subclass of Player

#import the Parent class
from Player import *

#Create a child class of player named ComputerPlayer. Within the child class, define a function where the player will make their choice.
class ComputerPlayer(Player):
    def make_choice(self):
        self.choice = random.choice(["rock", "paper", "scissors"])
        print(f"{self.name} chose {self.choice}")