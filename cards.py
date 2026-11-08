#Global constants
RANKS = [2,3,4,5,6,7,8,9,10,"J","Q","K","Ace"]
SUITS = ["♠","♥","♦","♣"]

import random

#Writes cards nicely
def card_name(card):
    """Writes one card in an easy to read format, e.g. 10♠"""
    return f"{card[0]}{card[1]}"


def deck_generation(number_of_decks):
    """Creates a randomized shoe according to number of decks given"""
    deck = []
    for rank in RANKS:
            for suit in SUITS:
                deck.append((rank,suit))
    shoe = deck * number_of_decks
    random.shuffle(shoe)
    return shoe

def deck_penetration(shoe):
    lower_bound = len(shoe)*0.65
    upper_bound = len(shoe)*0.85
    penetration = round(random.uniform(lower_bound,upper_bound))
    return penetration





