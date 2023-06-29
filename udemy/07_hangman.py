import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    ======''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    ======''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    ======''',
    '''
    +---+
    |   |
    O   |
    |   |
   /    |
        |
    ======''',
    '''
    +---+
    |   |
    O   |
    |   |
   / \  |
        |
    ======''',
    '''
    +---+
    |   |
    O   |
    |   |
   /|\  |
        |
    ======''',
    '''
    +---+
    |   |
    O   |
    |   |
   /|\  |
   /    |
    ======''',
    '''
    +---+
    |   |
    O   |
    |   |
   /|\  |
   / \  |
    ======'''
]

words = ["apple", "banana", "orange", "mango", "barley"]

chosen_word = random.choice(words)

lives = 6
display = []

print(logo)

for let in range(len(chosen_word)):
    display.append("_")

end_of_game = False

while end_of_game == False:
    guess = input("Pick a letter! ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for let in range(len(chosen_word)):
        letter = chosen_word[let]
        # print(
        #     f"Current position: {let}\n Current letter: {letter}\n Guessed letter: {guess} ")
        if letter == guess:
            display[let] = letter
            print("Congratulations! You guessed a letter.")

    if guess not in chosen_word:
        print("Wrong! You lost a life.")
        lives -= 1
        if lives == 0:
            print("You lose!")
            end_of_game = True

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives + 1])
