from tkinter import *

root = Tk()
root.title('Titulo')

gandhi_msg = "Whatever you do will be insignificant, but it is very"\
    " important that you do it.\n(Mahatma Gandhi)."


msg = Message(root, text=gandhi_msg)
msg.config(bg='light green',fg='blue',font=('Times', 24, 'italic'))
# bg => background, fg=>foreground
msg.pack()


root.mainloop()