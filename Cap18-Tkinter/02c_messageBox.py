from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Minha janela com definicao de geometria')

# tamanho da janela
# width x height + Left + Top
root.geometry("440x200+100+100")


def callBack():
    messagebox.showinfo(title='Hello', message='Ola Floripa Code Gurus')


B = Button(root, text='Hello', command=callBack)
B.place(x=50, y=50) # posicionamento


root.mainloop()