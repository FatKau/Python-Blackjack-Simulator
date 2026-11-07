import random
import time

#Tests
dealer_blackjack_test = False
player_blackjack_test = False
both_blackjack_test = False

bankroll = 1000
RANKS = [2,3,4,5,6,7,8,9,10,"J","Q","K","Ace"]
SUITS = ["♠","♥","♦","♣"]
#---------------------------Nice to have stuff for neatness----------------------------------------
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
#----------------------------------Deck Generation------------------------------------------------------------
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

#-------------------------New Hand Class----------------------------------------------
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



def hand_value(hand):
    """Calcuates the value of the hand"""
    value = 0
    ace_count = 0

    for card in (hand):
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


def deal_card(deck,hand):
    """Removes a card from the deck list"""
    card = (deck.pop())
    hand.append(card)
    return card

def card_name(card):
    """Writes the name of the card in an easy to read format"""
    card = f"{card[0]}{card[1]}"
    return card

def hand_name(hand):
    """Writes the hand name in a easy to read format"""
    hand_list = []
    for card in (hand):
        hand_list.append(card_name(card))
    hand_list = ", ".join(hand_list)
    return hand_list

def check_stake(stake):
    """Checks stake value entered is valid"""
    if stake < 0:
        print("Stake cannot be negative")
        return False
    if stake == 0:
        print("Stake cannot be 0")
        return False
    if stake <= bankroll:
        return True
    if stake > bankroll:
        print("Stake exceeds bankroll")
        return False



def deck_penetration(deck):
    lower_bound = len(deck)*0.65
    upper_bound = len(deck)*0.85
    penetration = round(random.uniform(lower_bound,upper_bound))
    return penetration

reshuffle_point = len(shoe) - deck_penetration(shoe)
print(f"Deck penetration is {reshuffle_point}")

def play_round():
  
    #---------------------------------------------------------------------Initial Deal----------------------------------------------

    #Blackjack Test Rigs
    if player_blackjack_test == True:
        shoe.extend([(2,"♠"),("Ace","♠"),(2,"♠"),("K","♠") ])
    if dealer_blackjack_test == True:
        shoe.extend([("Ace","♠"),(2,"♠"),("K","♠"),(2,"♠") ])
    if both_blackjack_test == True:
        shoe.extend([("Ace","♠"),("Ace","♠"),("K","♠"),("K","♠") ])

    player_hand = []
    dealer_hand = []
    deal_card(shoe,player_hand)
    dealer_first_card = deal_card(shoe,dealer_hand)
    deal_card(shoe,player_hand)
    dealer_second_card = deal_card(shoe,dealer_hand)

    #Deck length test
    print (f"Cards left in shoe: {len(shoe)}")

    print("Player has",hand_name(player_hand))
    time.sleep(0.3)
    print("Dealer has",card_name(dealer_first_card) ,"face up")
    time.sleep(0.3)


    print("Player's hand value is",hand_value(player_hand))
    time.sleep(0.3)

    #------------------------------Natural Check----------------------------------
    #Natural Check Player
    if hand_value(player_hand) == 21 and len(player_hand) == 2:
        print("Blackjack!")
        time.sleep(0.3)
        print (f"Dealer's 2nd card is {card_name(dealer_second_card)}. Dealer has", hand_value(dealer_hand))
        if hand_value(player_hand) > hand_value(dealer_hand):
            print("Player wins!")
            return "blackjack"
        
        if hand_value(player_hand) == hand_value(dealer_hand):
            print("Dealer also has Blackjack! Hand Pushes")
            return "push"
    
    #Natural Check Dealer
    if hand_value(dealer_hand) == 21 and len(dealer_hand) == 2:
        print (f"Dealer's 2nd card is {card_name(dealer_second_card)}. Dealer has BlackJack! \nDealer wins!")
        time.sleep(0.3)
        return "loss"


    while hand_value(player_hand) < 21:
        choice = input("hit or stand? ").lower()

    
        if choice in ["hit", "h"]:
            card_dealt = deal_card(shoe,player_hand)
            print("You drew", card_name(card_dealt))
            time.sleep(0.3)
            print ("Your hand value is now", hand_value(player_hand))
            time.sleep(0.3)
            
        elif choice in ["stand", "s"]:
            time.sleep(0.3)
            print("You have stood at", hand_value(player_hand))
            break

        else:
            print("I didn't understand your input. type hit or stand")


        
    #Dealer's turn

    if hand_value(player_hand) < 22:
        print (f"Dealer's 2nd card is {card_name(dealer_second_card)}. Dealer has {hand_value(dealer_hand)}")
        while hand_value(dealer_hand) < 17:
            card_dealt = deal_card(shoe,dealer_hand)
            print("Dealer draws", card_name(card_dealt))
            time.sleep(0.3)
            print("Dealer's hand value is now", hand_value(dealer_hand))
            time.sleep(0.3)

        if hand_value(dealer_hand) <= 21:
            print("Dealer stands on", hand_value(dealer_hand))
            time.sleep(0.3)

    #Player vs. Dealer

    if hand_value(player_hand) > 21:
        print("Player busts, dealer wins!")
        return "loss"

    elif hand_value(dealer_hand) > 21:
        print("Dealer busts, Player wins!")
        return "win"

    elif hand_value(player_hand) > hand_value(dealer_hand):
        print("Player wins!")
        return "win"

    elif hand_value(player_hand) == hand_value(dealer_hand):
        print("Hands are equal, push")
        return "push"

    else:
        print("Dealer's hand is higher, dealer wins")
        return "loss"


play_again = "yes"

while play_again in ["yes", "yeah", "y"]:

    if bankroll < 0.01:
        print("You have busted!")
        break


    try:
        stake = float(input("Enter your stake: "))
    except ValueError:
        print("That's not a number")
        continue

    if check_stake(stake):
        result = play_round()
        if result == "blackjack":
            bankroll = bankroll + (stake * 1.5)

        if result == "win":
            bankroll = bankroll + stake

        if result == "loss":
            bankroll = bankroll - stake

        print(f"Your bankroll is {bankroll}")

        play_again = input("Play again? ").lower()
        print(f"cards left in deck: {len(shoe)}")


    if len(shoe) < reshuffle_point:
        shoe = deck_generation(number_of_decks)
        print ("Reshuffling deck...")
        time.sleep(0.5)
        print("Deck reshuffled!")
        reshuffle_point = len(shoe) - deck_penetration(shoe)

print("Thanks for playing!")
