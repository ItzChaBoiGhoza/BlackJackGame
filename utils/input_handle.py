def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much do you want to bet? "))
        except:
            print("Wrong input, only integers.")
        else:
            if chips.bet > chips.total:
                print(f"Insufficient total chips: {chips.total}")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()

def hit_or_stand(deck, hand):
    global playing
    
    while True:
        hit_stand = input('Do you want to Hit or Stand? (H or S)')
        
        if hit_stand[0].lower() == 'h':
            hit(deck, hand) # hit() functioned defined above gets called
        elif hit_stand[0].lower() == 's':
            print("Player stands. Dealer plays")
            playing = False
        else:
            print("Sorry, please try again!")
            continue
        break