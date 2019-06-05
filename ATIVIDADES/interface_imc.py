from tkinter import *

root = Tk()
root.title("Calculdadora de IMC")

root.geometry("300x100")

label_nome = Label(root, text='Nome:').grid(row=0)
label_altura = Label(root, text='Atura:').grid(row=1)
label_peso = Label(root, text='Peso:').grid(row=2)


e_nome = Entry(root).grid(row=0, column=1)
e_altura = Entry(root).grid(row=1, column=1)
e_peso = Entry(root).grid(row=2, column=1)

sair = Button(root, text='Sair', command=root.quit).grid(row=3)


root.mainloop()
