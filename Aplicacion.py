from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicación')
        ttk.Button(raiz, text='Salir',
                    command=raiz.destroy).pack(side=BOTTOM)
        raiz.mainloop()