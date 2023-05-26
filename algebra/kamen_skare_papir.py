# 1 kamen
# 2 skare
# 3 papir
import random

game_on = True
while game_on:
    izbor_racunala = random.randint(1, 3)
    izbor_korisnika = int(
        input("Unesite broj: (1 = rock, 2 = scissors, 3 = paper)"))

# print("Izbor racunala", izbor_racunala)
    if izbor_korisnika == izbor_racunala:
        print(f"Both players selected {izbor_korisnika}. It's a tie!")
    elif izbor_korisnika == "rock":
        if izbor_racunala == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif izbor_korisnika == "paper":
        if izbor_racunala == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif izbor_korisnika == "scissors":
        if izbor_racunala == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    nastavak_igre = input(
        "Zelite li nastaviti igrati? Upisite NE za prestanak!").upper()
    if nastavak_igre == "NE":
        game_on = False
    else:
        game_on = True
