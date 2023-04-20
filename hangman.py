from tkinter import *

window = Tk() 
#// means to divide the value and dont give the decimal value and called(FLOOR DIVISION)
width, height =500, 550 #HEIGHT AND WIDTH OF THE CREATED WINDOW
s_width= ((window.winfo_screenwidth() // 2)- (width // 2))  # (WIDTH OF THE MONITOR DISPLAY)//2 - (HEIGHT OF THE CREATED WINDOW)//2
s_height = ((window.winfo_screenwidth() // 2) -(height // 2))  #(HEIGHT OF THE MONITOR DISPLAY)//2 - (HEIGHT OF THE CREATED WINDOW)//2
window.geometry(f"{width}x{height}+{s_width}+{s_height}")  #AFTER THE MONITOR DISPLAY HEIGHT AND WIDTH THE HEIGHT AND WIDTH OF THE CREATED WINDOW SHOULD COME TO THE CENTER
window.config(bg="red")
window.title("Sewa Hangman")

#creating the figure of hangman#
canvas=Canvas(window, width= 700, height=300)
canvas.pack(pady=30)
canvas.create_line(150, 260, 250, 260, width=3) #base line of the stand
canvas.create_line(200, 260, 200, 40, width=3) #line of the stand
canvas.create_line(200, 90, 250, 40, width=3) #supporter of the stand
canvas.create_line(200, 48, 300, 40, width=3) #top line of the stand
canvas.create_line(300, 40, 300, 70, width=3) #rope line of the stand
canvas.create_oval(280, 70, 320, 100, width=3) #head of the man
c5 = canvas.create_line(300, 100, 300,180, width=3) # stomach of the man
c4 = canvas.create_line(300, 105, 270,155, width=3) # left hand of the man
c3 = canvas.create_line(300, 105, 330,155, width=3) # right of the man
c2 = canvas.create_line(300, 180, 270,230, width=3) # left leg of the man
c1 = canvas.create_line(300, 180, 330,230, width=3) # right leg of the man

#---------------------------LAYOUT-------------------------
label = Label(window, font =("arial"))
label.pack()

text=Entry(window, font=("arial, 10"), justify= CENTER, relief=GROOVE, bd=2)
text.pack(pady=20)

button = Button(window, text="SUBMIT", font=("arial, 10"), bg="blue")
button.pack()


window.mainloop()