import random
from Tkinter import *
num=random.randint(1,20)
root=None
entryBox=None
myText=None
count=0
def buttonPushed():
    global entryBox
    global count
    count+=1
    if count>6:
        myText.set("You lose!")
        entryBox.delete(0,END)
        entryBox.destroy()
        return
    txt=int(entryBox.get())
    entryBox.delete(0,END)
    if txt<num:
        myText.set("Your number is too low!")
    elif txt>num:
        myText.set("Your number is too high!")
    else:
        myText.set("You've guessed it correctly!")
        entryBox.destroy()
def createTextBox(root):
    global entryBox
    entryBox=Entry(root)
    entryBox.pack()                    
        
        
def addTextLabel(root):
    global myText
    myText=StringVar()
    myText.set("Hello User! I have chosen a number between 1 to 20.")
    myLabel=Label(root,textvariable=myText)
    myLabel.pack()
def main():
    global root
    root=Tk()
    root.title("Guess the Number!")
    root.geometry("400x300")
    myButton=Button(root,text="Take Guess!",command=buttonPushed)
    myButton.pack()
    createTextBox(root)
    addTextLabel(root)
    b=Button(root,text="Exit",command=root.destroy)
    b.pack()
    root.mainloop()
if __name__=='__main__':
    main()                        
        
    
