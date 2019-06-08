from tkinter import *

root = Tk()
root.title('Mensagem Tk')

campo = Message(root, text='Ola pessoal bom dia', relief=RAISED)
campo.pack()

root.mainloop()