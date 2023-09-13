import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_COLS, N_ROWS

def wordle():
    def initialize_keyboard_colors():
        # Initialize the colors of the keyboard letters
        for i in range(N_COLS):
            key_letter = keyboard_letters[i]
            gw.set_key_color(key_letter, MISSING_COLOR)

    def reset_game_state():
        # Pick a new random word from the list
        secret_word.clear()
        secret_word.extend(random.choice(FIVE_LETTER_WORDS))

        # Clear the color-coding of the boxes
        for i in range(N_COLS):
            gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)

        # Reset the current row
        gw.set_current_row(0)

        # Initialize keyboard colors
        initialize_keyboard_colors()

    def enter_action(s):
        if len(s) != 5:
            gw.show_message("Enter a 5-letter word.")
            return

        s = s.upper()  # Convert the entered word to uppercase for case-insensitive comparison

        if s not in [word.upper() for word in FIVE_LETTER_WORDS]:
            gw.show_message("Not in word list")
            return

        current_row = gw.get_current_row()

        # Check for correct positions and color the boxes accordingly
        for i in range(len(s)):
            if s[i] == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
            elif s[i] in secret_word:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)

        # Check if the entered word is the same as the secret word (winning condition)
        if s == ''.join(secret_word):
            gw.show_message("Congratulations! You guessed the word.")
            reset_game_state()  # Reset the game state after a correct guess
        else:
            if current_row + 1 >= N_ROWS:
                gw.show_message(f"Game over. The word was {''.join(secret_word)}")
                reset_game_state()  # Reset the game state after a game over
            else:
                gw.set_current_row(current_row + 1)  # Move to the next row

        # Update the color of keyboard letters based on the current row
        update_keyboard_colors(current_row, s)

    def update_keyboard_colors(current_row, guessed_word):
        # Update the color of keyboard letters based on the current row
        for i in range(N_COLS):
            key_letter = keyboard_letters[i]
            if key_letter in guessed_word:
                if key_letter == secret_word[i]:
                    gw.set_key_color(key_letter, CORRECT_COLOR)
                else:
                    gw.set_key_color(key_letter, PRESENT_COLOR)
            else:
                if current_row > 0:
                    prev_row = current_row - 1
                    prev_guess = [gw.get_square_letter(prev_row, j) for j in range(N_COLS)]
                    if key_letter not in prev_guess:
                        gw.set_key_color(key_letter, MISSING_COLOR)

    # Initialize the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Initialize the game state
    secret_word = []
    keyboard_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:N_COLS]
    reset_game_state()

if __name__ == "__main__":
    wordle()