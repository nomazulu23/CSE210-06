#from hangman import Hangman

class Pole():
    def __init__(self):
        self._pole = ["_________"]
        
    def display_pole(self):
        for i in self._pole:
            print(i)