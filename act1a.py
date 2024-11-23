import random

def display_welcome():
    print("\n==================================================")
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it? You have 3 attempts!")
    print("If you're close, I'll give you a hint! Let's play!")
    print("==================================================")

def get_hint(guess, number):
    if abs(guess - number) <= 10:
        return "You're very close! 🔥"
    elif abs(guess - number) <= 20:
        return "You're getting warmer! 🌡️"
    else:
        return "You're quite far off! ❄️"

def main():
    while True:
        number = random.randint(1, 100)
        attempts = 3
        guess = None
        
        display_welcome()
        
        while attempts > 0 and guess != number:
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < 1 or guess > 100:
                    print("Please guess a number between 1 and 100.")
                    continue
                
                attempts -= 1
                
                if guess < number:
                    print("Guess higher! ⬆️")
                elif guess > number:
                    print("Guess lower! ⬇️")
                else:
                    print("🎉 You won! The number was", number)
                    break
                
                # Provide a hint
                print(get_hint(guess, number))
                print(f"You have {attempts} attempts left.\n")
            except ValueError:
                print("Oops! That's not a valid number. Please try again.")
        
        if guess != number:
            print(f"Sorry, you've run out of attempts! The number was {number}. Better luck next time! 🍀")
        
        # Fail-safe for replay prompt
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == 'yes':
                break  # Exit the loop and start a new game
            elif play_again == 'no':
                print("\nThank you for playing! Goodbye! 👋")
                return  # Exit the program
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()