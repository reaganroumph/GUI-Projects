from tkinter import *

top = Tk()
playlist = []


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
    
    B1Main = Button(text = "week 1", bg = "green", command = week1)
    B1Main.grid(column = 0, row = 2)

    B2Main = Button(text = "week 2", bg = "green", command = week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "week 3", bg = "green")
    B3Main.grid(column = 0, row = 4)

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
    B1 = Button(text= " + ", bg = "#35783d", command = addSong)
    B1.grid(column = 1, row = 2)

    #print
    B2 = Button(text = "Print List", bg = "#35783d", command = printList)
    B2.grid(column=0, row = 3)

    #export
    B3 = Button(text= "Export List", bg = "#35783d", command = exportPlaylist)
    B3.grid(column=1, row = 3)

    Bclear = Button(text= "Main Menu", bg = "#35783d", command = mainMenu)
    Bclear.grid(column = 1, row = 4)

def week2():
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

    B1W2 = Button(text = "Roll 'em", bg = "red")
    B1W2.grid(column = 2, row = 4)




if __name__== "__main__":
    mainMenu()
    top.mainloop()
