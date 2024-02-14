from tkinter import *
from PIL import ImageTk, Image
import random 

root = Tk()

#root.iconbitmap("rockwin.ico")
root.title("Rock Paper Scissors")
root.resizable(width=False,height=False)




click = True


rockPhoto=PhotoImage(file="rock.png")
paperPhoto=PhotoImage(file="paper.png")
scissorsPhoto=PhotoImage(file="scissors.png")

rockwinPhoto=PhotoImage(file="rockwin.png")
paperwinPhoto=PhotoImage(file="paperwin.png") 
scissorswinPhoto=PhotoImage(file="scissorswin.png")

rocklosePhoto=PhotoImage(file="rocklose.png")
paperlosePhoto=PhotoImage(file="paperlose.png")
scissorslosePhoto=PhotoImage(file="scissorslose.png")

winPhoto=PhotoImage(file="win.png")
losePhoto=PhotoImage(file="lose.png")
tiePhoto=PhotoImage(file="tie.png")



def play():
    global rockButton,paperButton,scissorsButton

    rockButton = Button(root,image=rockPhoto,
                        command = lambda:youPick("rock"))

    paperButton = Button(root,image=paperPhoto,
                        command = lambda:youPick("paper"))

    scissorsButton = Button(root,image=scissorsPhoto,
                        command = lambda:youPick("scissors"))

    rockButton.grid(row=0,column=0)
    paperButton.grid(row=0,column=1)
    scissorsButton.grid(row=0,column=2)


def computerPick():
    choice = random.choice(["rock","paper","scissors"])
    return choice


def youPick(yourChoice):
    global click

    compPick = computerPick()

    if click == True:
        if yourChoice == "rock" and compPick == "rock":
            rockButton.configure(image = rockwinPhoto)
            paperButton.configure(image=rocklosePhoto)
            scissorsButton.configure(image = tiePhoto)
            click = False
        elif yourChoice == "rock" and compPick == "paper":
            rockButton.configure(image = rocklosePhoto)
            paperButton.configure(image=paperwinPhoto)
            scissorsButton.configure(image = losePhoto)
            click = False
        elif yourChoice == "rock" and compPick == "scissors":
            rockButton.configure(image = rockwinPhoto)
            paperButton.configure(image=scissorslosePhoto)
            scissorsButton.configure(image = winPhoto)
            click = False
        elif yourChoice == "paper" and compPick == "paper":
            rockButton.configure(image = paperwinPhoto)
            paperButton.configure(image = paperlosePhoto)
            scissorsButton.configure(image = tiePhoto)
            click = False
        elif yourChoice == "paper" and compPick == "scissors":
            rockButton.configure(image = paperlosePhoto)
            paperButton.configure(image = scissorswinPhoto)
            scissorsButton.configure(image = losePhoto)
            click = False
        elif yourChoice == "paper" and compPick == "rock":
            rockButton.configure(image = paperwinPhoto)
            paperButton.configure(image = rocklosePhoto)
            scissorsButton.configure(image = winPhoto)
            click = False
        elif yourChoice == "scissors" and compPick == "scissors":
            rockButton.configure(image = paperwinPhoto)
            paperButton.configure(image = paperlosePhoto)
            scissorsButton.configure(image = tiePhoto)
            click = False
        elif yourChoice == "scissors" and compPick == "rock":
            rockButton.configure(image = scissorslosePhoto)
            paperButton.configure(image = rockwinPhoto)
            scissorsButton.configure(image = losePhoto)
            click = False
        elif yourChoice == "scissors" and compPick == "paper":
            rockButton.configure(image = scissorswinPhoto)
            paperButton.configure(image = paperlosePhoto)
            scissorsButton.configure(image = winPhoto)
            click = False
        else:
            if yourChoice == "rock" or yourChoice == "paper" or yourChoice == "scissors":
                rockButton.configure(image = rockPhoto)
                paperButton.configure(image = paperPhoto)
                scissorsButton.configure(image = scissorsPhoto)
                click = True

play()
root.mainloop()





