import random

def play_number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 5
    
    print(f"\nI have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess the correct number.")
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            break
    else:
        print(f"\nSorry, you are out of attempts. The correct number was {number_to_guess}.")
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_number_guessing_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    play_number_guessing_game()
