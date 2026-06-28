
import random

def get_valid_guess():

    """Ensures the user inputs an actual integer between 1 and 100."""
    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("⚠️ Please enter a number strictly between 1 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")

def play_game():
    print("\n=== 🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯 ===")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Adds a losing condition for a better challenge
    
    while attempts < max_attempts:
        user_guess = get_valid_guess()
        attempts += 1
        
        if user_guess > secret_number:
            print(f"📉 Lower number please! ({max_attempts - attempts} attempts left)")
        elif user_guess < secret_number:
            print(f"📈 Higher number please! ({max_attempts - attempts} attempts left)")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            return
            
    print(f"\n💥 Game Over! You ran out of turns. The number was {secret_number}.")

if __name__ == "__main__":

    # Standard Python entry point
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye. 👋")
            break