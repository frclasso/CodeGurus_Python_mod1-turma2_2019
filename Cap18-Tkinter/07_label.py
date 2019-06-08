from tkinter import *
root = Tk()

l1 = Label(root, text='Insira seu nome:').grid(row=0)

e1 = Entry(root).grid(row=0, column=1)

l2 = Label(root, text='Insira seu sobrenome:').grid(row=1)

e2 = Entry(root).grid(row=1, column=1)

root.mainloop()