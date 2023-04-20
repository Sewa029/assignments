from tkinter import*
from tkinter import messagebox


window= Tk()
window.title("Sewa tic tac toe")
window.geometry("285x305")
window.resizable(0,0)

#x starts so true
clicked = True
count = 0

#start the game over!
def reset():
    pass

#disable all the buttons
def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state =DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)


#check to see if someone won
def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"]== "X" and b3["text"]== "X":
        b1.configure(bg="red")
        b2.configure(bg="red")
        b3.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","X Wins!")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"]== "X" and b6["text"]== "X":
        b4.configure(bg="red")
        b5.configure(bg="red")
        b6.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","X Wins!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"]== "X" and b9["text"]== "X":
        b7.configure(bg="red")
        b8.configure(bg="red")
        b9.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","X Wins!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"]== "X" and b7["text"]== "X":
        b1.configure(bg="red")
        b4.configure(bg="red")
        b7.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","X Wins!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"]== "X" and b8["text"]== "X":
        b2.configure(bg="red")
        b5.configure(bg="red")
        b8.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","X Wins!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"]== "X" and b9["text"]== "X":
        b3.configure(bg="red")
        b6.configure(bg="red")
        b9.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "X Wins!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"]== "X" and b9["text"]== "X":
        b1.configure(bg="red")
        b5.configure(bg="red")
        b9.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","X Wins!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"]== "X" and b7["text"]== "X":
        b3.configure(bg="red")
        b5.configure(bg="red")
        b7.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","X Wins!")
        disable_all_buttons()

    #### check for o's win
    elif b1["text"] == "O" and b2["text"]== "O" and b3["text"]== "O":
        b1.configure(bg="red")
        b2.configure(bg="red")
        b3.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"]== "O" and b6["text"]== "O":
        b4.configure(bg="red")
        b5.configure(bg="red")
        b6.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"]== "O" and b9["text"]== "O":
        b7.configure(bg="red")
        b8.configure(bg="red")
        b9.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    elif b1["text"] == "0" and b4["text"]== "O" and b7["text"]== "O":
        b1.configure(bg="red")
        b4.configure(bg="red")
        b7.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"]== "O" and b8["text"]== "O":
        b2.configure(bg="red")
        b5.configure(bg="red")
        b8.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"]== "O" and b9["text"]== "O":
        b3.configure(bg="red")
        b6.configure(bg="red")
        b9.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"]== "O" and b9["text"]== "O":
        b1.configure(bg="red")
        b5.configure(bg="red")
        b9.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"]== "O" and b7["text"]== "O":
        b3.configure(bg="red")
        b5.configure(bg="red")
        b7.configure(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","O Wins!")
        disable_all_buttons()

    # check if tie
    if count ==9 and  winner == False:
        messagebox.showinfo("tic tac toe", "NO WINNER")
        disable_all_buttons()

#Button clicked function
def b_click(b):
    global clicked, count

    if b["text"]==" " and clicked ==True:
        b["text"]="X"
        clicked = False
        count += 1
        checkifwon()

    elif b["text"]==" " and clicked ==False:
        b["text"]="O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe","clicked already\n select another")

#start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked =True
    count = 0
    #build our buttons
    b1 = Button(window, text=" ",font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b1))
    b2 = Button(window, text=" ",font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b2))
    b3 = Button(window, text=" ", font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b3))

    b4 = Button(window, text=" ", font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b4))
    b5 = Button(window, text=" ", font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b5))
    b6 = Button(window, text=" ", font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b6))

    b7 = Button(window, text=" ", font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b7))
    b8 = Button(window, text=" ", font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b8))
    b9 = Button(window, text=" ", font=("arial", 18), height =3, width=6, bg="grey", command=lambda:b_click(b9))

    #grid our buttons to the screen 
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


#create menu
my_menu = Menu(window)
window.config(menu=my_menu)

#create options menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options",menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)




window.mainloop()