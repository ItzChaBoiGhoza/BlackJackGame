'''
Deck class to intantiate the deck of cards
'''
import random
from game.card import Card
from game.constants import suits, ranks

class Deck:
    
    def __init__(self):
        self.deck = [] # start the deck of cards with empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
            
    def __str__(self):
        deck_placeholder = ''
        for card in self.deck:
            deck_placeholder += '\n ' + card.__str__() # add each Card object's print string
        return 'The deck: ' + deck_placeholder
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card