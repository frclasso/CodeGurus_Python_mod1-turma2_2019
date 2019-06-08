from tkinter import *

root = Tk()

def var_states():
    print("Python: {} \nPearl:{} \nDjango:{}".format(var1.get(), var2.get(),var3.get()))

var1 = IntVar(value=1)
c1 = Checkbutton(root, text='Python', variable=var1).grid(row=0, stick=W)


var2 = IntVar()
c2 = Checkbutton(root, text='Pearl', variable=var2).grid(row=1, stick=W)

var3 = IntVar()
c3 = Checkbutton(root, text='Django', variable=var3).grid(row=2, stick=W)


# botoes
b1 = Button(root, text="Exibir valores", command=var_states).grid(row=4, sticky=W, pady=4)
b2 = Button(root, text="Sair", command=root.quit).grid(row=5, sticky=W, pady=4)

root.mainloop()
