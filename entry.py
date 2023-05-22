from tkinter import *

root = Tk()

labelName = Label(root, text='Nome:')
labelName.pack()

e = Entry(root)
e.pack()

def myClick():
    myLabel = Label(root, text=f'Olá, {e.get()}!')
    myLabel.pack() 
    e.delete(0,99999)

myButton = Button(root, text='Clique aqui!', command=myClick)
myButton.pack()

root.mainloop()
