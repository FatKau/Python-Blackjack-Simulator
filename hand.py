
from cards import card_name

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return ", ".join(card_name(card) for card in self.cards)

    def deal_card(self, shoe):
        """Removes a card from the deck list"""
        card = (shoe.pop())
        self.cards.append(card)
        return self.cards
        
    def hand_value(self):
        """Calculates the value of the hand"""
        value = 0
        ace_count = 0

        for card in (self.cards):
            if card[0] in ["J","Q","K"]:
                value = value + 10
            elif card[0] in ["Ace"]:
                value = value + 11
                ace_count = ace_count + 1
            else:
                value = value + card[0]

        while value > 21 and ace_count > 0:
            value = value - 10
            ace_count = ace_count - 1
        return value

    def is_blackjack(self):
        """Returns boolean var for blackjack"""
        if self.hand_value() == 21 and len(self.cards) == 2:
            return True
        else:
            return False