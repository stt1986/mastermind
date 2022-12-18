#MasterMind with timer!

import random
import tkinter as tk
import threading
import time

colorChoices={0:"",1:"red",2:"yellow",3:"orange",4:"green",5:"cyan",6:"purple"}

class Game:
    def __init__(self, computerChoice=[], guessCount=0, score=0, round=1, timer=60, status=False, scoreFormatted="0"):
        self.computerChoice=computerChoice
        self.guessCount=guessCount
        self.score=score
        self.round=round
        self.timer=timer
        self.status=status
        self.scoreFormatted=scoreFormatted

class Guess:
    def __init__(self, choiceOne, choiceTwo, choiceThree, choiceFour, correctChoices=0):
        #choiceOne-Four integers, guessList colors
        self.choiceOne=choiceOne
        self.choiceTwo=choiceTwo
        self.choiceThree=choiceThree
        self.choiceFour=choiceFour
        self.correctChoices=correctChoices
        self.currentGuessList=["","","",""]

def createList():
    for i in range(4):
        choice=random.randint(1,6)
        currentGame.computerChoice.append(colorChoices[choice])

def randomColor():
    #this is messy
        choice=random.randint(1,6)
        color=colorChoices[choice]
        guessRowCurrent1.configure(bg=color)
        currentGuess.choiceOne=choice
        currentGuess.currentGuessList[0]=color
        choice=random.randint(1,6)
        color=colorChoices[choice]
        guessRowCurrent2.configure(bg=color)
        currentGuess.choiceTwo=choice
        currentGuess.currentGuessList[1]=color
        choice=random.randint(1,6)
        color=colorChoices[choice]
        guessRowCurrent3.configure(bg=color)
        currentGuess.choiceThree=choice
        currentGuess.currentGuessList[2]=color
        choice=random.randint(1,6)
        color=colorChoices[choice]
        guessRowCurrent4.configure(bg=color)
        currentGuess.choiceFour=choice
        currentGuess.currentGuessList[3]=color

def getColor(number):
    color=colorChoices.get(number)
    return color

def changeColor(position):
    if position=="1":
        if currentGuess.choiceOne==6:
            currentGuess.choiceOne=0
        currentGuess.choiceOne+=1
        color=getColor(currentGuess.choiceOne)
        guessRowCurrent1.config(bg=(color))
        currentGuess.currentGuessList[0]=color
    elif position=="2":
        if currentGuess.choiceTwo==6:
            currentGuess.choiceTwo=0
        currentGuess.choiceTwo+=1
        color=getColor(currentGuess.choiceTwo)
        guessRowCurrent2.config(bg=(color))
        currentGuess.currentGuessList[1]=color
 
    elif position=="3":
        if currentGuess.choiceThree==6:
            currentGuess.choiceThree=0
        currentGuess.choiceThree+=1
        color=getColor(currentGuess.choiceThree)
        guessRowCurrent3.config(bg=(color))
        currentGuess.currentGuessList[2]=color
    elif position=="4":
        if currentGuess.choiceFour==6:
            currentGuess.choiceFour=0
        currentGuess.choiceFour+=1
        color=getColor(currentGuess.choiceFour)
        guessRowCurrent4.config(bg=(color))
        currentGuess.currentGuessList[3]=color

def changeColorR(position):
    if position=="1":
        if currentGuess.choiceOne==1:
            currentGuess.choiceOne=6
        currentGuess.choiceOne-=1
        color=getColor(currentGuess.choiceOne)
        guessRowCurrent1.config(bg=(color))
        currentGuess.currentGuessList[0]=color
    elif position=="2":
        if currentGuess.choiceTwo==1:
            currentGuess.choiceTwo=6
        currentGuess.choiceTwo-=1
        color=getColor(currentGuess.choiceTwo)
        guessRowCurrent2.config(bg=(color))
        currentGuess.currentGuessList[1]=color
 
    elif position=="3":
        if currentGuess.choiceThree==1:
            currentGuess.choiceThree=6
        currentGuess.choiceThree-=1
        color=getColor(currentGuess.choiceThree)
        guessRowCurrent3.config(bg=(color))
        currentGuess.currentGuessList[2]=color
    elif position=="4":
        if currentGuess.choiceFour==1:
            currentGuess.choiceFour=6
        currentGuess.choiceFour-=1
        color=getColor(currentGuess.choiceFour)
        guessRowCurrent4.config(bg=(color))
        currentGuess.currentGuessList[3]=color

def submitGuess():
    global gameTimerThread
    currentGame.status=True
    notifyLabel.configure(text="")

    if checkGuess():
        notifyLabel.configure(text="Round Clear! +10 Seconds")
        gameWin()
    else:
        currentGame.guessCount+=1
        drawGuesses()
        moveGuesses()
        

def checkGuess():
    if currentGuess.currentGuessList==currentGame.computerChoice: return True
    else: return False

def gameWin():
    currentGame.round+=1
    currentGame.timer+=10
    currentGame.computerChoice=[]
    scoreModifier=checkGuessCount()
    currentGame.score+=scoreModifier
    currentGame.scoreFormatted=str(currentGame.score)
    currentGame.scoreFormatted=currentGame.scoreFormatted.zfill(8)
    scoreLabel.configure(text=("Score:" + currentGame.scoreFormatted))
    currentGame.guessCount=0
    clearRows()
    createList()
    roundLabel.configure(text=("Round: "+ str(currentGame.round)))
    
def checkGuessCount():
    if currentGame.guessCount==1:
        return 1000
    if currentGame.guessCount==2:
        return 750
    if currentGame.guessCount==3:
        return 500
    if currentGame.guessCount==4:
        return 250
    if currentGame.guessCount==5:
        return 100
    if currentGame.guessCount>=6:
        return 50
    


def drawGuesses():
    guessRow6_1.configure(bg=guessRow4_1.cget("bg"), text=guessRow4_1.cget("text"))
    guessRow6_2.configure(bg=guessRow4_2.cget("bg"), text=guessRow4_2.cget("text"))
    guessRow6_3.configure(bg=guessRow4_3.cget("bg"), text=guessRow4_3.cget("text"))
    guessRow6_4.configure(bg=guessRow4_4.cget("bg"), text=guessRow4_4.cget("text"))

    guessRow5_1.configure(bg=guessRow4_1.cget("bg"), text=guessRow4_1.cget("text"))
    guessRow5_2.configure(bg=guessRow4_2.cget("bg"), text=guessRow4_2.cget("text"))
    guessRow5_3.configure(bg=guessRow4_3.cget("bg"), text=guessRow4_3.cget("text"))
    guessRow5_4.configure(bg=guessRow4_4.cget("bg"), text=guessRow4_4.cget("text"))

    guessRow4_1.configure(bg=guessRow3_1.cget("bg"), text=guessRow3_1.cget("text"))
    guessRow4_2.configure(bg=guessRow3_2.cget("bg"), text=guessRow3_2.cget("text"))
    guessRow4_3.configure(bg=guessRow3_3.cget("bg"), text=guessRow3_3.cget("text"))
    guessRow4_4.configure(bg=guessRow3_4.cget("bg"), text=guessRow3_4.cget("text"))


    guessRow3_1.configure(bg=guessRow2_1.cget("bg"), text=guessRow2_1.cget("text"))
    guessRow3_2.configure(bg=guessRow2_2.cget("bg"), text=guessRow2_2.cget("text"))
    guessRow3_3.configure(bg=guessRow2_3.cget("bg"), text=guessRow2_3.cget("text"))
    guessRow3_4.configure(bg=guessRow2_4.cget("bg"), text=guessRow2_4.cget("text"))

    guessRow2_1.configure(bg=guessRow1_1.cget("bg"), text=guessRow1_1.cget("text"))
    guessRow2_2.configure(bg=guessRow1_2.cget("bg"), text=guessRow1_2.cget("text"))
    guessRow2_3.configure(bg=guessRow1_3.cget("bg"), text=guessRow1_3.cget("text"))
    guessRow2_4.configure(bg=guessRow1_4.cget("bg"), text=guessRow1_4.cget("text"))


def moveGuesses():
        if currentGuess.currentGuessList[0]==currentGame.computerChoice[0]:
            guessRow1_1.configure(text="        ", bg=currentGuess.currentGuessList[0])
        else:
            guessRow1_1.configure(text="   ×   ", bg=currentGuess.currentGuessList[0])

        if currentGuess.currentGuessList[1]==currentGame.computerChoice[1]:
            guessRow1_2.configure(text="        ", bg=currentGuess.currentGuessList[1])
        else:
            guessRow1_2.configure(text="   ×   ", bg=currentGuess.currentGuessList[1])

        if currentGuess.currentGuessList[2]==currentGame.computerChoice[2]:
            guessRow1_3.configure(text="        ", bg=currentGuess.currentGuessList[2])
        else:
            guessRow1_3.configure(text="   ×   ", bg=currentGuess.currentGuessList[2])
        
        if currentGuess.currentGuessList[3]==currentGame.computerChoice[3]:
            guessRow1_4.configure(text="        ", bg=currentGuess.currentGuessList[3])
        else:
            guessRow1_4.configure(text="   ×   ", bg=currentGuess.currentGuessList[3])

def timerSecond():
    seconds=60
    while True:
        if currentGame.status==True:
            if currentGame.timer>0:
                if currentGame.timer<10:
                    timerLabel.configure(fg="red")
                currentGame.timer-=1
                timerLabel.configure(text=currentGame.timer)
                time.sleep(1)
            if currentGame.timer==0:
                endGame()
                pass

def clearRows():
    guessRow1_1.configure(bg="black", text="        ")
    guessRow1_2.configure(bg="black", text="        ")
    guessRow1_3.configure(bg="black", text="        ")
    guessRow1_4.configure(bg="black", text="        ")

    guessRow2_1.configure(bg="black", text="        ")
    guessRow2_2.configure(bg="black", text="        ")
    guessRow2_3.configure(bg="black", text="        ")
    guessRow2_4.configure(bg="black", text="        ")

    guessRow3_1.configure(bg="black", text="        ")
    guessRow3_2.configure(bg="black", text="        ")
    guessRow3_3.configure(bg="black", text="        ")
    guessRow3_4.configure(bg="black", text="        ")

    guessRow4_1.configure(bg="black", text="        ")
    guessRow4_2.configure(bg="black", text="        ")
    guessRow4_3.configure(bg="black", text="        ")
    guessRow4_4.configure(bg="black", text="        ")

    guessRow5_1.configure(bg="black", text="        ")
    guessRow5_2.configure(bg="black", text="        ")
    guessRow5_3.configure(bg="black", text="        ")
    guessRow5_4.configure(bg="black", text="        ")

    guessRow6_1.configure(bg="black", text="        ")
    guessRow6_2.configure(bg="black", text="        ")
    guessRow6_3.configure(bg="black", text="        ")
    guessRow6_4.configure(bg="black", text="        ")

def endGame():
    guessSubmit.configure(state="disabled")
    notifyLabel.configure(text="Game Over!")


currentGuess=Guess(0,0,0,0)
currentGame=Game()
gameTimerThread=threading.Thread(target=timerSecond)
gameTimerThread.start()

createList()
root=tk.Tk()
root.title("Mastermind")
root.geometry("325x300")
root.configure(bg="black")
root.resizable(False,False)

screenFrame=tk.LabelFrame(bd=0, bg="black")
timerFrame=tk.LabelFrame(screenFrame, bd=0,bg="black")
guessFrame=tk.LabelFrame(screenFrame, bg="black")
currentGuessFrame=tk.LabelFrame(screenFrame, bg="black")
bottomFrame=tk.LabelFrame(screenFrame, bd=0,bg="black")

timerLabel=tk.Label(timerFrame, text="60", font="TkDefaultFont 24",bg="black",fg="white")
roundLabel=tk.Label(timerFrame, text="Round: 1",bg="black",fg="white")
scoreLabel=tk.Label(timerFrame, text="Score: 00000000", bg="black", fg="white")


guessRow1_1=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow1_2=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow1_3=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow1_4=tk.Label(guessFrame, text="        ",bg="black", width=5)

guessRow2_1=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow2_2=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow2_3=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow2_4=tk.Label(guessFrame, text="        ",bg="black", width=5)

guessRow3_1=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow3_2=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow3_3=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow3_4=tk.Label(guessFrame, text="        ",bg="black", width=5)

guessRow4_1=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow4_2=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow4_3=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow4_4=tk.Label(guessFrame, text="        ",bg="black", width=5)

guessRow5_1=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow5_2=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow5_3=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow5_4=tk.Label(guessFrame, text="        ",bg="black", width=5)

guessRow6_1=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow6_2=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow6_3=tk.Label(guessFrame, text="        ",bg="black", width=5)
guessRow6_4=tk.Label(guessFrame, text="        ",bg="black", width=5)

guessRowCurrent1=tk.Label(currentGuessFrame, text="        ")
guessRowCurrent2=tk.Label(currentGuessFrame, text="        ")
guessRowCurrent3=tk.Label(currentGuessFrame, text="        ")
guessRowCurrent4=tk.Label(currentGuessFrame, text="        ")
guessRowCurrent5=tk.Label(root, text="        ")

notifyLabel=tk.Label(bottomFrame, text="",bg="black",fg="white")
guessSubmit=tk.Button(bottomFrame, text="Guess", command=submitGuess)

guessRowCurrent1.bind("<Button-1>", lambda event: changeColor("1"))
guessRowCurrent2.bind("<Button-1>", lambda event: changeColor("2"))
guessRowCurrent3.bind("<Button-1>", lambda event: changeColor("3"))
guessRowCurrent4.bind("<Button-1>", lambda event: changeColor("4"))
guessRowCurrent1.bind("<Button-3>", lambda event: changeColorR("1"))
guessRowCurrent2.bind("<Button-3>", lambda event: changeColorR("2"))
guessRowCurrent3.bind("<Button-3>", lambda event: changeColorR("3"))
guessRowCurrent4.bind("<Button-3>", lambda event: changeColorR("4"))

screenFrame.place(relx=0.5, rely=0.5, anchor="center")
timerFrame.grid(row=0)
timerLabel.grid(row=0)
roundLabel.grid(row=1)
scoreLabel.grid(row=2)


guessFrame.grid(row=2)
guessRow6_1.grid(row=0,column=0)
guessRow6_2.grid(row=0,column=1)
guessRow6_3.grid(row=0,column=2)
guessRow6_4.grid(row=0,column=3)

guessRow5_1.grid(row=1,column=0)
guessRow5_2.grid(row=1,column=1)
guessRow5_3.grid(row=1,column=2)
guessRow5_4.grid(row=1,column=3)

guessRow4_1.grid(row=2,column=0)
guessRow4_2.grid(row=2,column=1)
guessRow4_3.grid(row=2,column=2)
guessRow4_4.grid(row=2,column=3)

guessRow3_1.grid(row=3,column=0)
guessRow3_2.grid(row=3,column=1)
guessRow3_3.grid(row=3,column=2)
guessRow3_4.grid(row=3,column=3)

guessRow2_1.grid(row=4,column=0)
guessRow2_2.grid(row=4,column=1)
guessRow2_3.grid(row=4,column=2)
guessRow2_4.grid(row=4,column=3)

guessRow1_1.grid(row=5,column=0)
guessRow1_2.grid(row=5,column=1)
guessRow1_3.grid(row=5,column=2)
guessRow1_4.grid(row=5,column=3)

currentGuessFrame.grid(row=10)
guessRowCurrent1.grid(row=0,column=0)
guessRowCurrent2.grid(row=0,column=1)
guessRowCurrent3.grid(row=0,column=2)
guessRowCurrent4.grid(row=0,column=3)

bottomFrame.grid(row=11)
notifyLabel.grid(row=1)
guessSubmit.grid(row=0)

randomColor()

root.mainloop()