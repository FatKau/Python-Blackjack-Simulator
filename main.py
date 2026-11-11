from cards import Shoe

from helpers import say
from helpers import ask_number

from game import play_round

from validation import is_valid_stake

PAYOUTS = {"blackjack":1.5,"win":1,"loss":-1,"double win":2,"double loss":-2,"push":0}

def main():
    bankroll = 1000
    number_of_decks = ask_number("Enter number of decks: ",1,100)
    shoe = Shoe(number_of_decks)
    print(f"Cut card placed. The shoe will be reshuffled after any round that leaves fewer than {shoe.reshuffle_point} cards.")
    play_again = "yes"

    while play_again in ["yes", "yeah", "y"]:

        if bankroll < 0.01:
            print("You have busted!")
            break

        try:
            stake = float(input("Enter your stake: "))
        except ValueError:
            say("That's not a number")
            continue

        if is_valid_stake(stake, bankroll):
            result = play_round(shoe,stake,bankroll)
            profit_loss = stake*PAYOUTS[result]
            bankroll = bankroll + (profit_loss)

            if PAYOUTS[result] > 0:
                say(f"you won {profit_loss}\nBankroll is {bankroll}")

            elif PAYOUTS[result] < 0:
                say(f"you lost {abs(profit_loss)}\nBankroll is {bankroll}")

            else:
                say(f"Stake is pushed, bankroll remains at {bankroll}")

            if bankroll > 0.01:
                play_again = input("Play again? ").lower()
                say(f"cards left in deck: {len(shoe.cards)}")

            if shoe.needs_reshuffle():
                shoe.build()
                say("Reshuffling deck...")
                say("Deck reshuffled!")


    print("Thanks for playing!")


if __name__ == "__main__":
    main()




