from tkinter import*
from random import randint



#string functions and some word selection
word_list = ["book", "mother", "school", "hangman"]

ind = randint(0, len(word_list))

word=word_list[ind] 

word_ind =randint(0, len(word) - 2)


question= word.replace(word[word_ind], "_")

#tkinter main window
window = Tk()
ans_usr= StringVar()
window.title("Sewa hangman")
window.geometry("400x300")
window.resizable(0,0)



Label(window, text="Hangman Game", font=("arial", 18), fg="green").grid(row=0, column=1, sticky=N, pady=5,padx=10)
Label(window, text="Question: ", font=("times new roman", 14)).grid(row=1, column=0, sticky=W, pady=5,padx=10)


#Question word
Label(window, text=question, font=("times new roman", 12)).grid(row=1, column=1, sticky=W, pady=5,padx=10)

Entry(window, textvariable = ans_usr).grid(row=2, column=1, sticky=N, pady=5,padx=10)

Button(window,text="Submit?!?!", font=("arial", 14), fg="blue", bg="black").grid(row=3, column=1, sticky=N, pady=5,padx=10)



window.mainloop()