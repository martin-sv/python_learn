from card import Card
from card_enum import  CardNumber, CardSuit

class Hand():
    cards: Card = []

    def add_card(self, card: Card):
        # card passed in
        # from Deck.deal() --> single Card()
        self.cards.append(card)
        return self.cards[len(self.cards) - 1]
    
    def count(self):
        total = 0
        ace = False
        # Switcher to count cards
        switcher = {
            11: 10,
            12: 10,
            13: 10,
            1: 11
        }
        # Count the Cards
        for card in self.cards:
            total += switcher.get(card.number.value, card.number.value)
            if card.number.value == 1: ace = True
        # If an Ace and over 21, the Ace will be a 1 and not an 11
        if (total > 21 and ace):
            total -= 10
        
        return(total)
