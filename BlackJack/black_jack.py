from card_enum import CardNumber, CardSuit
from deck import Deck
from hand import Hand

def main():
    
    deck = Deck()
    #print(deck)
    deck.shuffle()
    player_hand = Hand()
    for i in range(1, 5):
        print(player_hand.add_card(deck.pick_card()).number.value)
    print (player_hand.count())
    

if __name__ == '__main__':
    main()
