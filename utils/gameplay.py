def player_busts(player, dealer, chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer Busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Player and Dealer tie! It is a PUSH!")