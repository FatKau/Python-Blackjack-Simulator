from cards import card_name
from helpers import say
from hand import Hand

#Tests
dealer_blackjack_test = False
player_blackjack_test = False
both_blackjack_test = False

def play_round(shoe,stake,bankroll):
  
    #Blackjack Test Rigs
    if player_blackjack_test == True:
        shoe.cards.extend([(2,"♠"),("Ace","♠"),(2,"♠"),("K","♠") ])
    if dealer_blackjack_test == True:
        shoe.cards.extend([("Ace","♠"),(2,"♠"),("K","♠"),(2,"♠") ])
    if both_blackjack_test == True:
        shoe.cards.extend([("Ace","♠"),("Ace","♠"),("K","♠"),("K","♠") ])

#---------------------------------------------------------------------Initial Deal----------------------------------------------

    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.deal_card(shoe)
    dealer_hand.deal_card(shoe)
    player_hand.deal_card(shoe)
    dealer_hand.deal_card(shoe)

    #Shoe length test

    say(f"Player has {player_hand}")
    say(f"Dealer has {card_name(dealer_hand.cards[0])} face up")
    say(f"Cards left in shoe: {len(shoe.cards)}")
    say(f"Player's hand value is {player_hand.hand_value()}")

    #------------------------------Natural Check----------------------------------
    #Natural Check Player
    if player_hand.is_blackjack():
        say("Blackjack!")
        say (f"Dealer's 2nd card is {card_name(dealer_hand.cards[1])}. Dealer has {dealer_hand.hand_value()}")
        if player_hand.hand_value() > dealer_hand.hand_value():
            say("Player wins!")
            return "blackjack"
        
        if player_hand.hand_value() == dealer_hand.hand_value():
            say("Dealer also has Blackjack! Hand Pushes")
            return "push"
    
    #Natural Check Dealer
    if dealer_hand.is_blackjack():
        say(f"Dealer's 2nd card is {card_name(dealer_hand.cards[1])}. Dealer has BlackJack! \nDealer wins!")
        return "loss"

    def double_down(stake,bankroll):
        if bankroll < stake * 2:
            say("You don't have enough bankroll to double down")
            return False
        answer = input("Would you like to double down? ").lower()
        return answer in ["y","yes","yea","yeh"]

        
    if double_down(stake,bankroll):
        player_hand.deal_card(shoe)
        say(f"You've doubled down. You drew {card_name(player_hand.cards[-1])}")
        say(f"Your hand value is now {player_hand.hand_value()}")
        doubled = True

    else:
        doubled = False
        while player_hand.hand_value() < 21:
            choice = input("hit or stand? ").lower()

        
            if choice in ["hit", "h"]:
                player_hand.deal_card(shoe)
                say(f"You drew {card_name(player_hand.cards[-1])}")
                
                say(f"Your hand value is now {player_hand.hand_value()}")
                
                
            elif choice in ["stand", "s"]:
                
                say(f"You have stood at {player_hand.hand_value()}")
                break

            else:
                say("I didn't understand your input. type hit or stand")
            
        #Dealer's turn

    if player_hand.hand_value() < 22:
        say (f"Dealer's 2nd card is {card_name(dealer_hand.cards[1])}. Dealer has {dealer_hand.hand_value()}")
        while dealer_hand.hand_value() < 17:
            dealer_hand.deal_card(shoe)
            say(f"Dealer draws {card_name(dealer_hand.cards[-1])}")
            say(f"Dealer's hand value is now {dealer_hand.hand_value()}")


        if dealer_hand.hand_value() <= 21:
            say(f"Dealer stands on {dealer_hand.hand_value()}")


    #Player vs. Dealer
    if doubled:
        
        if player_hand.hand_value() > 21:
            say("Player busts, dealer wins!")
            return "double loss"

        elif dealer_hand.hand_value() > 21:
            say("Dealer busts, Player wins!")
            return "double win"

        elif player_hand.hand_value() > dealer_hand.hand_value():
            say("Player wins!")
            return "double win"

        elif player_hand.hand_value() == dealer_hand.hand_value():
            say("Hands are equal, push")
            return "push"

        else:
            say("Dealer's hand is higher, dealer wins")
            return "double loss"

    else:
            
        if player_hand.hand_value() > 21:
            say("Player busts, dealer wins!")
            return "loss"

        elif dealer_hand.hand_value() > 21:
            say("Dealer busts, Player wins!")
            return "win"

        elif player_hand.hand_value() > dealer_hand.hand_value():
            say("Player wins!")
            return "win"

        elif player_hand.hand_value() == dealer_hand.hand_value():
            say("Hands are equal, push")
            return "push"

        else:
            say("Dealer's hand is higher, dealer wins")
            return "loss"