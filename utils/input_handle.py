from game.chips import Chips

def take_bet():
    while True:
        try:
            Chips.bet = int(input("How much do you want to bet? "))
        except:
            print("Wrong input, only integers.")
        else:
            if Chips.bet > Chips.total:
                print(f"Insufficient total chips: {Chips.total}")
            else:
                break

def hit(deck, hand):
    
    pass

def hit_or_stand(deck, hand):
    global playing
    
    pass
