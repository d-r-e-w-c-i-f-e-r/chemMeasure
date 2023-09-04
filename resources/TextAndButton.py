import tkinter
from tkinter import *
from tkinter import ttk

class TextAndButton(tkinter.Frame):
    def __init__(self, parent, text, button):
        super().__init__(parent)
        self.pack(fill=tkinter.X)

        lbl = tkinter.Label(self, text=text, width=14, anchor='w')
        lbl.pack(side=tkinter.LEFT, padx=5, pady=5)
        button.pack(side=tkinter.LEFT)

