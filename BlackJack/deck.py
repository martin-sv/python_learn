import random
from card_enum import *
from card import Card
#from BlackJack.card import *

class Deck():

    def __init__(self):
        self.cards: Card = []

        for suit_iterator in range (1, 5):
            for number_iterator in range(1, 14):
                self.cards.append(Card(CardNumber(number_iterator), CardSuit(suit_iterator)))


    def shuffle(self):
        self.cards.shuffle()
        return self.cards()

    def pick_card(self) -> Card:
        return(self.cards.pop())

    def __str__(self):
        return '\n'.join(map(str, self.cards))

    def shuffle(self):
        random.shuffle(self.cards)