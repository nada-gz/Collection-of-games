import random
from tkinter import *
from words import words

print("-----------Welcome to Hangman------------")
root = Tk()
root.title('Hangman Game')

greet = Label(root, font=('arial', 60, 'bold'), text="Welcome!").grid(row=0, columnspan=3)
won = 0
entered = ''
curr = random.choice(words)
print(curr)
guessed = ''
moves = len(curr) + 1
str = ''


def play():
    global guessed
    global curr
    global won
    global entered
    global moves
    global str
    entered = f"{en.get()}"
    if entered in guessed:
        btn = Entry(root, textvariable=en, width=5, font=('arial', 20, 'bold'))
        btn.grid(row=2, column=2)
        submitbtn = Button(root, text="Submit", command=play, bg="DodgerBlue2", fg="white",
                           font=('arial', 20, 'bold')).grid(row=4, columnspan=3)
        return

    guessed += entered
    entered = entered[0]
    print(entered)
    won = 1
    str = ''
    for ch in curr:
        if ch in guessed:
            str += ch
            print(ch, end='')
        else:
            won = 0
            str += '_'
            print("_", end='')
    print('')
    entered_string = Label(root, font=('arial', 20, 'bold'), text=str).grid(row=6, columnspan=3)
    moves -= 1
    print(moves)
    if won == 1:
        win = Label(root, font=('arial', 20, 'bold'), text="You Won!!!")
        win.grid(row=8, columnspan=3)
    elif won == 0 and moves <= 0:
        lost = Label(root, font=('arial', 20, 'bold'), text="You Lost!!!")
        lost.grid(row=8, columnspan=3)
    else:
        btn = Entry(root, textvariable=en, width=5, font=('arial', 20, 'bold'))
        btn.grid(row=2, column=2)
        submitbtn = Button(root, text="Submit", command=play, bg="DodgerBlue2", fg="white", font=('arial', 20, 'bold'))
        submitbtn.grid(row=4, columnspan=3)


msg = Label(root, font=('arial', 20, 'bold'), text="Enter a character")
msg.grid(row=2, column=1)
en = StringVar()
btn = Entry(root, textvariable=en, width=5, font=('arial', 20, 'bold'))
btn.grid(row=2, column=2)
submitbtn = Button(root, text="Submit", command=play, bg="DodgerBlue2", fg="white", font=('arial', 20, 'bold'))
submitbtn.grid(row=4, columnspan=3)
root.resizable(width=False, height=False)
mainloop()





