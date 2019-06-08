from tkinter import *

root = Tk()

frame = Frame(root)  # posicionado em top
frame.pack()


bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redButton = Button(frame, text='Red', fg='red')
redButton.pack(side=LEFT)

greenButton = Button(frame, text='Green', fg='green')
greenButton.pack(side=LEFT)

blackButton = Button(frame, text='Black', fg='black')
blackButton.pack(side=LEFT)

blueButton = Button(bottomframe, text='Blue',fg='blue')
blueButton.pack()

root.mainloop()