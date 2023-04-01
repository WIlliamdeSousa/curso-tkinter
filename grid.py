from tkinter import *

# tela principal
root = Tk()

# criando labels
my_label1 = Label(root, text='hello, world')
my_label2 = Label(root, text='my name is William')

# mostrando na tela
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=1)

root.mainloop()
