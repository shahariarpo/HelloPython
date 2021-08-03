secret_word = "Apple"
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    player_guess = input("Guess the word: ")
    guess_count += 1
    if player_guess.lower() == secret_word.lower():
        print("You Won!")
        break
else:
    print("You lose")