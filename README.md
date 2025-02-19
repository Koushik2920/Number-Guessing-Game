# Number-Guessing-Game
This is a simple number guessing game where the player has to guess a randomly generated number within a specific range. After each guess, the player receives feedback on whether their guess was too high, too low, or correct. The game ends when the player guesses the correct number or exhausts the allowed attempts.
Features of the Number Guessing Game
Random Number Generation – The game generates a random number within a user-defined range using Python's random.randint() function.

User-Defined Range – The player can choose the lower and upper bounds for the number to be guessed, making the game customizable.

Limited Attempts – The player gets a fixed number of attempts (default is 5) to guess the correct number.

Feedback System – The game provides feedback after each guess:

"Too high!" if the guess is greater than the number.
"Too low!" if the guess is smaller than the number.
"Congratulations!" if the guess is correct.
Looping Through Attempts – The game keeps track of the number of attempts and ends when the player guesses correctly or runs out of attempts.

Game Over Condition – If the player fails to guess the correct number within the given attempts, the correct number is revealed.

Replay Option – After the game ends, the player is given the choice to play again or exit.

User Input Handling – Ensures that the player enters valid numbers and prevents crashes due to invalid input.

Simple and Interactive Interface – The game runs in a command-line interface with clear instructions, making it beginner-friendly.

Number Guessing Game - Installation & Setup Guide
🛠 Requirements
Ensure you have the following installed on your system:

A terminal or command prompt to run the script
💾 Installation & Setup
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game
🎮 How to Play
The game will ask you to enter a lower and upper bound for the number range.
The game will randomly select a number within this range.
You have 5 attempts to guess the correct number.
After each guess, you’ll receive hints:
If your guess is too high, it will print "Too high! Try again."
If your guess is too low, it will print "Too low! Try again."
If your guess is correct, it will print "Congratulations! You guessed the number!"
If you run out of attempts, the correct number will be revealed.
You’ll be given the option to play again or exit.

📝 Example Menu (Game Output)

Welcome to the Number Guessing Game!
Enter the lower bound of the range: 1
Enter the upper bound of the range: 50

I have selected a number between 1 and 50.
You have 5 attempts to guess the correct number.

Attempt 1: Enter your guess: 25
Too high! Try again.

Attempt 2: Enter your guess: 10
Too low! Try again.

Attempt 3: Enter your guess: 15
Too low! Try again.

Attempt 4: Enter your guess: 20
Correct! You guessed the number 20 correctly!

Do you want to play again? (yes/no): no
Thank you for playing!

✨ Possible Enhancements
Difficulty Levels (Easy, Medium, Hard with different attempt limits)
Score Tracking (Keep track of the number of games won)
Leaderboard System (Save high scores in a file)
GUI Version (Using tkinter or PyQt for a graphical interface)
