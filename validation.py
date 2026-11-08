def is_valid_stake(stake,bankroll):
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