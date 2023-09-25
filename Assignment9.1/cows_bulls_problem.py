import random

def generate_random_number():
    """
    Generate a random 4-digit number with non-repeating digits.
    """
    while True:
        num = random.sample(range(10), 4)
        if num[0] != 0:
            return ''.join(map(str, num))

def count_cows_and_bulls(secret_number, user_guess):
    """
    Count cows and bulls for the user's guess.
    """
    cows, bulls = 0, 0
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            cows += 1
        elif user_guess[i] in secret_number:
            bulls += 1
    return cows, bulls

def main():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_random_number()
    attempts = 0

    while True:
        user_guess = input("Enter a 4-digit number with non-repeating digits: ")
        
        if not user_guess.isdigit() or len(user_guess) != 4 or len(set(user_guess)) != 4:
            print("Invalid input. Please enter a valid 4-digit number with non-repeating digits.")
            continue
        
        attempts += 1
        cows, bulls = count_cows_and_bulls(secret_number, user_guess)
        
        if cows == 4:
            print(f"Congratulations! You guessed the correct number '{secret_number}' in {attempts} attempts.")
            break
        else:
            print(f"{cows} cow{'s' if cows != 1 else ''}, {bulls} bull{'s' if bulls != 1 else ''}")

if __name__ == "__main__":
    main()
