#!usr/bin/env python3

from tkinter import *

root = Tk()
root.title("Calculo de IMC")

root.geometry('310x200')

text = StringVar()
alt = DoubleVar()
pes = DoubleVar()

label1 = Label(root, text="Digite seu nome:").grid(row=0, column=0, sticky=W, padx=5)
entry1 = Entry(root, textvariable=text, width=20)
entry1.grid(row=0, column=1)

label2 = Label(root, text='Altura: ').grid(row=1, column=0, sticky=W, padx=5)
entry2 = Entry(root, textvariable=alt, width=20)
entry2.grid(row=1, column=1)

label3 = Label(root, text='Peso: ').grid(row=2, column=0, sticky=W, padx=5)
entry3 = Entry(root, textvariable=pes, width=20)
entry3.grid(row=2, column=1)


def resultado():
    nome = entry1.get()
    altura = float(entry2.get())
    peso = float(entry3.get())
    imc = peso / altura ** 2
    imc = '{:.2f}'.format(imc)
    saida['text'] = f'Nome: {nome}, IMC: {imc}'


B1 = Button(root, text="Calcula IMC", command=resultado).grid(row=4, pady=20)

saida = Label(root, text='Resultado de sua avaliação', fg='blue',bg='white', font="Verdana 10 bold")
saida.grid(rowspan=5, columnspan=2, sticky=W, padx=6)

root.mainloop()