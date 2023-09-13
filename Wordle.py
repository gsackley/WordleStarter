import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        if len(s) != 5:
            gw.show_message("Enter a 5-letter word.")
            return

        s = s.upper()  # Convert the entered word to uppercase for case-insensitive comparison

        if s not in [word.upper() for word in FIVE_LETTER_WORDS]:
            gw.show_message("Not in word list")
            return

        # Check for correct positions and color the boxes accordingly
        for i in range(len(s)):
            if s[i] == secret_word[i]:
                gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
            elif s[i] in secret_word:
                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
            else:
                gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)

        # Check if the entered word is the same as the secret word (winning condition)
        if s == secret_word:
            gw.show_message("Congratulations! You guessed the word.")
        else:
            gw.set_current_row(gw.get_current_row() + 1)  # Move to the next row

            # If all rows are used, display a game over message
            if gw.get_current_row() >= N_ROWS:
                gw.show_message(f"Game over. The word was {secret_word}")

    # Initialize the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Pick a random word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS)

if __name__ == "__main__":
    wordle()