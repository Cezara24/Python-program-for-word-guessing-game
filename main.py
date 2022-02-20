from random_word import RandomWords


def check_maximum():
    while True:
        try:
            global maximum
            maximum = int(input("\nHow many letters do you want the word to have?\nMaximum: "))
            break
        except ValueError:
            print("Please choose a number!")


def get_random_word():
    global word
    global maximum
    word = r.get_random_word(includePartOfSpeech="noun", maxLength=int(maximum))


def simple_word():
    global word
    while True:
        if "-" in word:
            word = r.get_random_word(includePartOfSpeech="noun", maxLength=int(maximum))
            continue
        else:
            break


def display_guessed(letters):
    for ch in letters:
        print(ch, end=" ")
    print()


def guess_word():
    global guessed
    print(f"\nI chose a random word. Try to guess it!\nYou have 10 attempts.")
    guessed = ["_"] * len(word)
    display_guessed(guessed)
    return guessed


def letter_in_word():
    global letter, attempts, win, tried_letters

    if letter in word:
        count = 0
        for character in word:
            if character == letter:
                guessed[count] = letter
            count += 1
        display_guessed(guessed)
        if "_" not in guessed:
            win = True
            print("YOU WIN")
    else:
        if letter not in tried_letters:
            tried_letters += letter
            attempts += 1
        else:
            print("You've already tried this letter.")
        print(f"{10 - attempts} attempts left")
        if attempts < 10:
            print(f"Try again!")
            display_guessed(guessed)


def play():
    global attempts, win, lose, letter

    while not win and not lose:
        if attempts < 10:
            letter = input("\nIt contains the letter: ").lower()
            if letter.isalpha():
                if len(letter) == 1:
                    letter_in_word()
                else:
                    print("Please choose a single letter!")
            else:
                print("Please choose a letter!")
        else:
            print(f'GAME OVER\nThe word was "{word}".')
            lose = True


r = RandomWords()
maximum = 0
word = ""
guessed = []
win = False
lose = False
attempts = 0
letter = ""
tried_letters = []

check_maximum()
get_random_word()
simple_word()
guess_word()
play()
