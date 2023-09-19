# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

random_word = random.choice(FIVE_LETTER_WORDS)


def wordle():
    row = 0
    col = 0

    def enter_action(s):  
        row = gw.get_current_row()
        col = 0        
        word = ""    
        for x in range(N_COLS):
            word += gw.get_square_letter(row,col)
            col = col + 1
       
        #gw.show_message(word)

        if word.lower() in FIVE_LETTER_WORDS:
            gw.show_message("That's a good word")
            square = 0
            for x in range(N_COLS):
                letter = gw.get_square_letter(row,square)
                if letter.lower() == random_word[square]:
                    gw.set_square_color(row,square,"#66BB66")
                elif letter.lower() in random_word:
                    gw.set_square_color(row,square, "#CCBB66")
                else:
                    gw.set_square_color(row,square, "#999999")
                square = square+1
            gw.set_current_row(row+1)
        elif (word[-1]) == " ":
            gw.show_message("Not enough letters")
        else:
            gw.show_message("Not in word list")    
   
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    gw.set_current_row(0)

    # for x in random_word:
    #     gw.set_square_letter(row,col,x)
    #     col = col + 1

   
print(random_word)
# Startup code

if __name__ == "__main__":
    wordle()