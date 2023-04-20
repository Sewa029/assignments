import tkinter as tk
import random

window= tk.Tk()
window.title("Sewa hangman")
window.geometry("400x350")
window.resizable(0,0)

#define a list of random words
words = ["python","bicycle","food","school","book"]

#define the   ASCII aret for hangman
hangman_art = [

    "   +---+\n      |    |\n      |\n          |\n       |\n       |\n=========",
    "   +---+\n      |    |\n   o  |\n          |\n       |\n       |\n=========",
    "   +---+\n      |    |\n   o  |\n   |      |\n       |\n       |\n=========",
    "   +---+\n      |    |\n   o  |\n  /|      |\n       |\n       |\n=========",
    "   +---+\n      |    |\n   o  |\n  /|\\     |\n       |\n       |\n=========",
    "   +---+\n      |    |\n   o  |\n  /|\\     |\n  /    |\n       |\n=========",
    "   +---+\n      |    |\n   o  |\n  /|\\     |\n  / \\  |\n       |\n=========",
 
]


#define a function to choose a random word from the list
def choose_word():
    return random.choice(words)


#define a function to update the hangman ASCII art
def update_hangman(mistakes):
    hangman_label.config(text=hangman_art[mistakes])


#define a function to check if the letter is in word
def check_guess(guess):
    global word_with_blanks
    if guess in word:
        for i in range(len(word)):
            if word[i]== guess:
                word_with_blanks = word_with_blanks[:i] + guess + word_with_blanks[i+1:]
        word_label.config(text=word_with_blanks)
        if '_' not in word_with_blanks:
            end_game("lose")
    else:
        global mistakes
        update_hangman(mistakes)
        if mistakes == 6 :
            end_game("lose")

def end_game(result):
    if result == "WIN!":
        result_text="YOU WIN"
    else:
        result_text="YOU LOSE,the word was" + word
    result_label.config(text=result_text)
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")



hangman_label = tk.Label(window, font=("arial", 20))
hangman_label.grid(row=0, column=0)

word= choose_word()
word_with_blanks='_' * len(word)
word_label =tk.Label(window,text=word_with_blanks,font=("arial", 20))
word_label.grid(row=1, column=0)


#create the guess entry and button
guess_entry=tk.Entry(window, width=5, bg= "yellow", font=("arial", 20))
guess_entry.grid(row=2,column=0)
guess_button=tk.Button(window, text="Guess")
guess_button.grid(row=2, column=1)

#create the result label
result_label=tk.Label(window, font=("arial", 20))
result_label.grid(row=3, column=0)

#INITIALISE THE GAME
mistakes=0
update_hangman(mistakes)


window.mainloop()