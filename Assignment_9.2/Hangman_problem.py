import random

# Function to read words from a text file and store them in a list
def read_words_from_file(filename):
    with open('assignment_9.2\word_list.txt', 'r') as file:
        words = [line.strip() for line in file]
    return words

# Function to choose a random word from the list
def choose_random_word(word_list):
    return random.choice(word_list)

# Function to play the Hangman game
def play_hangman(word):
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts
    word_to_guess = '_' * len(word)

    print("Welcome to Hangman!")
    print(word_to_guess)
    
    while attempts_left > 0:
        guess = input("Guess your letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            word_to_guess = update_word_to_guess(word, word_to_guess, guess)
            print(word_to_guess)
            
            if word_to_guess == word:
                print("Congratulations! You guessed the word correctly: ", word)
                break
        else:
            attempts_left -= 1
            print(f"Incorrect! You have {attempts_left} {'attempts' if attempts_left != 1 else 'attempt'} left.")
    
    if attempts_left == 0:
        print("You're out of attempts. The word was:", word)

# Function to update the word being guessed
def update_word_to_guess(word, current_word, letter):
    new_word = ""
    for i in range(len(word)):
        if word[i] == letter:
            new_word += letter
        else:
            new_word += current_word[i]
    return new_word

if __name__ == "__main__":
    filename = "word_list.txt"
    words = read_words_from_file(filename)
    
    while True:
        chosen_word = choose_random_word(words)
        play_hangman(chosen_word)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
