#This file will contain the Player class constructor and functions available to the player

#import required libraries
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None

    def make_choice(self):
        pass
    
    def get_choice(self):
        return self.choice
        
    def update_score(self):
        self.score += 1