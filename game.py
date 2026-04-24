import random

def start_game():
    """A simple open-source number guessing game."""
    secret_number = random.randint(1, 20)
    attempts = 5
    
    print("--- Welcome to the Open Guessing Game! ---")
    print(f"I'm thinking of a number between 1 and 20. You have {attempts} tries.")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == secret_number:
            print(f"🎉 Success! You guessed the number {secret_number}!")
            return
        elif guess < secret_number:
            print("Higher...")
        else:
            print("Lower...")
        
        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(f"\nGame Over! The number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    start_game()
