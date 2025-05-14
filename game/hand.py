'''
Hand class for handling adding card, and adjusting to how 'ACE' works
'''
from game.constants import values

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1