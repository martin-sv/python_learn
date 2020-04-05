from card_enum import CardNumber, CardSuit

class Card():

  def __init__(self, number: CardNumber, suit: CardSuit):
      self.number = number
      self.suit = suit

  def __str__(self):
    return f'{self.number.name} of {self.suit.name}'
