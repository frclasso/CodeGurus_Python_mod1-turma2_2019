from tkinter import *

root = Tk()

Lb1 = Listbox(root)
Lb1.insert(1, 'Python')
Lb1.insert(2, 'Pearl')
Lb1.insert(3, 'Django')
Lb1.insert(4, 'Kivy')
Lb1.insert(5, 'C')
Lb1.insert(6, 'Julia')
Lb1.insert(7, 'R')

Lb1.pack()

root.mainloop()