from tkinter import *

# tela principal
root = Tk()

def myClick():
    myLabel = Label(root, text='Olha, c clicou no botão!')
    myLabel.pack() 

myButton = Button(root, text='Clique aqui!', command=myClick, bg='#000000', fg='#ffffff')
myButton.pack()

root.mainloop()
