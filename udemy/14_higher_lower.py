from game_data import data
import random
import os


logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def format_data(account):
    # format the account data into printable format
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    # generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    # get follower count to each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("clear")
    print(logo)
    # give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"Correct! Current score is {score}")
    else:
        should_continue = False
        print(f"Failed! Final score is {score}")
