# importanto tudo do tkinter
from tkinter import *


# configurações de tamanhos
BTN_WIDTH_STAND = 10
BTN_WIDTH_LARGER = 22
PAD_Y = 45


# criando a tela principal
root = Tk()
root.title('Calculadora simples')


# entrada de texto
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)


# funções
def button_click(number: int) -> None:
    """Função dos botões dos números."""
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear() -> None:
    """Função do botão para limpar a seleção."""
    e.delete(0, END)

def button_equal() -> None:
    """Função para mostrar o resultado na caixa de texto"""
    result = eval(e.get())
    e.delete(0, END)
    e.insert(0, result)


# definindo os botões
btn2 = Button(root, text='1', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(1))
btn1 = Button(root, text='2', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(2))
btn3 = Button(root, text='3', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(3))
btn4 = Button(root, text='4', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(4))
btn5 = Button(root, text='5', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(5))
btn6 = Button(root, text='6', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(6))
btn7 = Button(root, text='7', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(7))
btn8 = Button(root, text='8', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(8))
btn9 = Button(root, text='9', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(9))
btn0 = Button(root, text='0', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click(0))
btn_clear = Button(root, text='Clear', width=BTN_WIDTH_LARGER, pady=PAD_Y, command=button_clear)
btn_add = Button(root, text='+', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click('+'))
btn_equals = Button(root, text='=', width=BTN_WIDTH_LARGER, pady=PAD_Y, command=button_equal)
btn_subtract = Button(root, text='-', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click('-'))
btn_multiply = Button(root, text='*', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click('*'))
btn_divide = Button(root, text='/', width=BTN_WIDTH_STAND, pady=PAD_Y, command=lambda: button_click('/'))


# colocando botões na tela
btn1.grid(row=3, column=1)
btn2.grid(row=3, column=0)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)

btn_add.grid(row=5, column=0)
btn_equals.grid(row=5, column=1, columnspan=2)

# loop principal
root.mainloop()
