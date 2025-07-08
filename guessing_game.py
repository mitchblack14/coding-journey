import random

def get_difficulty():
    """Let player choose difficulty level"""
    print("\nChoose your difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice == 1:
                return 50, 10, "Easy"
            elif choice == 2:
                return 100, 7, "Medium"
            elif choice == 3:
                return 200, 5, "Hard"
            else:
                print("Please enter 1, 2, or 3!")
        except ValueError:
            print("Please enter a valid number!")

def give_hint(secret_number, attempts):
    """Give hints based on attempts"""
    if attempts == 3:
        if secret_number % 2 == 0:
            print("💡 Hint: The number is even!")
        else:
            print("💡 Hint: The number is odd!")
    elif attempts == 5:
        if secret_number % 10 == 0:
            print("💡 Hint: The number is divisible by 10!")
        elif secret_number % 5 == 0:
            print("💡 Hint: The number is divisible by 5!")

def number_guessing_game():
    """Main game function"""
    print("🎯 Welcome to the Number Guessing Game!")
    print("=" * 40)
    
    # Get difficulty
    max_num, max_attempts, difficulty = get_difficulty()
    
    print(f"\n🎮 {difficulty} Mode Selected!")
    print(f"I'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it!")
    
    # Generate random number
    secret_number = random.randint(1, max_num)
    attempts = 0
    guesses = []
    
    while attempts < max_attempts:
        try:
            # Get user input
            print(f"\nAttempt {attempts + 1}/{max_attempts}")
            if guesses:
                print(f"Previous guesses: {', '.join(map(str, guesses))}")
            
            guess = int(input("Enter your guess: "))
            
            # Validate range
            if guess < 1 or guess > max_num:
                print(f"❌ Please enter a number between 1 and {max_num}!")
                continue
            
            # Check if already guessed
            if guess in guesses:
                print("❌ You already guessed that number!")
                continue
            
            attempts += 1
            guesses.append(guess)
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}!")
                
                # Calculate score
                score = max(0, (max_attempts - attempts + 1) * 10)
                print(f"Your score: {score} points!")
                break
            elif guess < secret_number:
                difference = secret_number - guess
                if difference <= 5:
                    print("🔥 Very close! Too low, but you're getting hot!")
                elif difference <= 10:
                    print("🌡️ Close! Too low.")
                else:
                    print("📈 Too low! Try a higher number.")
            else:
                difference = guess - secret_number
                if difference <= 5:
                    print("🔥 Very close! Too high, but you're getting hot!")
                elif difference <= 10:
                    print("🌡️ Close! Too high.")
                else:
                    print("📉 Too high! Try a lower number.")
            
            # Give hints
            give_hint(secret_number, attempts)
                
        except ValueError:
            print("❌ Please enter a valid number!")
            continue
    
    else:
        # This runs if the loop completes without breaking
        print(f"\n💔 Game over! You've used all {max_attempts} attempts.")
        print(f"The number was {secret_number}. Better luck next time!")

def main():
    """Main function to handle multiple games"""
    while True:
        number_guessing_game()
        
        # Ask if they want to play again
        play_again = input("\n🔄 Would you like to play again? (y/n): ").lower()
        if play_again != 'y' and play_again != 'yes':
            print("Thanks for playing! 👋")
            break
        print("\n" + "="*50)

# Run the game
if __name__ == "__main__":
    main()