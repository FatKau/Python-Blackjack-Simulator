from cards import card_name
from cards import deck_generation
from cards import deck_penetration

from helpers import say
from helpers import ask_number

from game import play_round

from validation import is_valid_stake


def main():
    bankroll = 1000
    number_of_decks = ask_number("Enter number of decks: ",1,100)
    shoe = deck_generation(number_of_decks)
    reshuffle_point = len(shoe) - deck_penetration(shoe)
    print(f"Cut card placed. The shoe will be reshuffled after any round that leaves fewer than {reshuffle_point} cards.")

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
            result = play_round(shoe)
            if result == "blackjack":
                bankroll = bankroll + (stake * 1.5)
                say(f"You won {stake*1.5}")

            if result == "win":
                bankroll = bankroll + stake
                say(f"You won {stake}")
            if result == "loss":
                bankroll = bankroll - stake
                say(f"You lost {stake}")
            say(f"Your bankroll is {bankroll}")

            play_again = input("Play again? ").lower()
            say(f"cards left in deck: {len(shoe)}")

        if len(shoe) < reshuffle_point:
            shoe = deck_generation(number_of_decks)
            say("Reshuffling deck...")
            say("Deck reshuffled!")
            reshuffle_point = len(shoe) - deck_penetration(shoe)

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
