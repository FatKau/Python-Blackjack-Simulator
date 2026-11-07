import time
import random


RANKS = [2,3,4,5,6,7,8,9,10,"J","Q","K","Ace"]
SUITS = ["♠","♥","♦","♣"]


def ask_number(prompt,minimum,maximum):
    """Enter a prompt and give the min/max values required. Checks the value given falls in that range, otherwise repeats question"""
    while True:
        try:
            number = int(input(prompt))

        except ValueError:
            print("Please enter a whole number")
            continue

        if number < minimum or number > maximum:
            print(f"Please enter a number between {minimum} and {maximum}")
            continue

        return number

def deck_generation(number_of_decks):
    """Creates a randomized shoe according to number of decks given"""
    deck = []
    for rank in RANKS:
            for suit in SUITS:
                deck.append((rank,suit))
    shoe = deck * number_of_decks
    random.shuffle(shoe)
    return shoe


number_of_decks = ask_number("Enter number of decks: ",1,100)

shoe = deck_generation(number_of_decks)



class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def deal_card(self):
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



