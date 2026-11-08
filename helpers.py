import time
SLEEP_TIME = 0.3
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

def say(message):
    print(message)
    time.sleep(SLEEP_TIME)

