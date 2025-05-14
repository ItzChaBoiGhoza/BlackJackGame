'''
Main game
'''
from game.hand import Hand
from game.deck import Deck


test_deck = Deck()

player_hand = Hand()
player_hand.add_card(test_deck.deal())
player_hand.add_card(test_deck.deal())

for card in player_hand.cards:
    print(card)
    
print(player_hand.value)