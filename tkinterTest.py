from tkinter import *
import random 

top = Tk()
playlist = []
myRolls = []

def printList():
    print(playlist)

def exportPlaylist():
    with open('playlist.txt', 'w') as f:
        for song in playlist:
            f.write("%s\n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    Lmain = Label(top, text = "Block 5 GUIs")
    Lmain.grid(column = 0, row = 1)
    
    B1Main = Button(text = "week 1", bg = "#946f92", command = week1)
    B1Main.grid(column = 0, row = 2)

    B2Main = Button(text = "week 2", bg = "#946f92", command = week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "week 3", bg = "#946f92")
    B3Main.grid(column = 0, row = 4)

    top["background"]="#6f946f"

def week1():
    clearWindow()
    
    def addSong():
        playlist.append(E1.get())
        E1.delete(0, END)
        
    #this is a label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row= 1)

    #this is a text entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #this is a button widget
    B1 = Button(text= " + ", bg = "#946f92", command = addSong)
    B1.grid(column = 1, row = 2)

    #print
    B2 = Button(text = "Print List", bg = "#946f92", command = printList)
    B2.grid(column=0, row = 3)

    #export
    B3 = Button(text= "Export List", bg = "#946f92", command = exportPlaylist)
    B3.grid(column=1, row = 3)

    Bclear = Button(text= "Main Menu", bg = "#946f92", command = mainMenu)
    Bclear.grid(column = 1, row = 4)

def week2():
    def rollDice():
        #access the entry data
        rollTimes = E2W2.get()
        dieType = E1W2.get()
           
        #clear the window
        clearWindow()
           
        #perform the dice roll calculations
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
               
        #display the results with two labels and a button that goes to main menu
        L1RD = Label (top, text= "Here's your rolls!")
        L1RD.grid(column= 0, row=1)
           
        L2RD = Label (top, text = myRolls)
        L2RD.grid(column= 0, row=2)
           
        B1RD = Button (text= "Main Menu", bg = "#946f92", command = mainMenu)
        B1RD.grid(column= 0, row= 3)

        
    clearWindow()

    L1W2 = Label(top, text = "Dice Roller App")
    L1W2.grid(column = 2, row = 1)
    
    L2W2 = Label(top, text = "# of sides")
    L2W2.grid(column = 1, row = 2)
    
    L3W2 = Label(top, text = "# of rolls")
    L3W2.grid(column = 3, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 1, row = 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 3, row = 3)

    B1W2 = Button(text = "Roll 'em", bg = "#6e0868", fg = "white", command = rollDice)
    B1W2.grid(column = 2, row = 4)




if __name__== "__main__":
    mainMenu()
    top.mainloop()
