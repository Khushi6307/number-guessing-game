# Import random module to generate secret number
import random  

def get_valid_guess():

    """Ensures the user inputs an actual integer between 1 and 100."""

    while True:  # Keep asking until valid input is given
        try:
            guess = int(input("Guess the number (1-100): "))  # Convert input to integer
            if 1 <= guess <= 100:  # Check if number is in valid range
                return guess  # Return valid guess
            else:
                print("⚠️ Please enter a number strictly between 1 and 100.")  # Out of range warning
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")  # Handle non-integer input


def play_game():

    print("\n=== 🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯 ===")
    secret_number = random.randint(1, 100)  # Generate random number between 1 and 100
    attempts = 0       # Track number of attempts
    max_attempts = 10  # Maximum allowed attempts

    while attempts < max_attempts:  # Loop until attempts are exhausted
        user_guess = get_valid_guess()  # Get valid input from user
        attempts += 1       # Increment attempt counter

        if user_guess > secret_number:
            print(f"📉 Lower number please! ({max_attempts - attempts} attempts left)")  # Guess too high
        elif user_guess < secret_number:
            print(f"📈 Higher number please! ({max_attempts - attempts} attempts left)")  # Guess too low
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")  # Correct guess
            return  # Exit function on win

    print(f"\n💥 Game Over! You ran out of turns. The number was {secret_number}.")  # Player lost

# Standard Python entry point
if __name__ == "__main__":  
    while True:  # Loop to allow multiple rounds
        play_game()  # Start a new game
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()  # Ask to replay
        if play_again not in ['yes', 'y']:  # Exit if player doesn't want to continue
            print("Thanks for playing! Goodbye. 👋")
            break  # Exit the loop