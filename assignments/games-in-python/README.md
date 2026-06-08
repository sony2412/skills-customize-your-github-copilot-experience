
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input to practice fundamental programming concepts.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a function that sets up the game by randomly selecting a word from a predefined list and initializing game variables.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Initialize tracking variables for incorrect guesses and displayed progress
- Display the hidden word in format: `_ _ _`
- Example:
  ```
  Word selected: "python"
  Display: _ _ _ _ _ _
  ```

### 🛠️ Handle Player Guesses

#### Description
Implement a function that accepts letter guesses from the user and updates the game state.

#### Requirements
Completed program should:

- Accept letter guesses from the user via `input()`
- Reveal correct guesses in the word display
- Track incorrect guesses and decrement remaining attempts
- Prevent duplicate guess submissions
- Example:
  ```
  Current: _ _ _ _ _ _
  Guess a letter: e
  Current: _ _ _ _ _ e
  Incorrect guesses: 0
  ```

### 🛠️ Game Flow and Win/Lose Conditions

#### Description
Create the main game loop that manages gameplay flow and determines when the game ends.

#### Requirements
Completed program should:

- Run a loop that continues until the word is guessed or attempts are exhausted
- Display win/lose messages at game end
- Show the final word when game ends
- Allow player to play multiple games if desired
- Example win message: `Congratulations! You guessed the word: python`
- Example lose message: `Game Over! The word was: python`
