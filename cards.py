#Global constants
RANKS = [2,3,4,5,6,7,8,9,10,"J","Q","K","Ace"]
SUITS = ["♠","♥","♦","♣"]

import random


def card_name(card):
    """Writes one card in an easy to read format, e.g. 10♠"""
    return f"{card[0]}{card[1]}"

class Shoe:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.reshuffle_point = 0
        self.build()

    def build(self):
        """Creates a shuffled shoe and places the cut card"""
        deck = []
        for rank in RANKS:
            for suit in SUITS:
                deck.append((rank, suit))
        self.cards = deck * self.number_of_decks
        random.shuffle(self.cards)
        self.reshuffle_point = len(self.cards) - self.deck_penetration()

    def deck_penetration(self):
        """Calculates the position of the cut card in the shoe (between 65-80% of the shoe)"""
        lower_bound = len(self.cards) * 0.65
        upper_bound = len(self.cards) * 0.80
        return round(random.uniform(lower_bound, upper_bound))

    def deal(self):
        """Removes and returns one card from the shoe"""
        return self.cards.pop()

    def needs_reshuffle(self):
        """True once fewer cards remain than the cut card position allows"""
        return len(self.cards) < self.reshuffle_point