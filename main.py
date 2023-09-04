import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from resources.TextAndButton import TextAndButton


window = Tk()
style = ttk.Style()
style.map('C.TButton',
          foreground=[('pressed', 'red'), ('active', 'blue')],
          background=[('pressed', '!disabled', 'black'), ('active', 'white')]
          )

window.title("Chem Measurement Wizard")
window.geometry("1000x1000+10+20")


def execute():
    alert = tkinter.messagebox.showinfo(title='!!!TEST!!!', message='!!!THIS IS A TEST!!!')

def print_input():
    input = inputtxt.get(1.0, "end-1c")
    lbl.config(text='Provided Input: '+input)

inputtxt = tkinter.Text(window,
                        height=5,
                        width=20)
inputtxt.pack()

colored_btn = ttk.Button(text='press', style='C.TButton', command=lambda: execute())
print_btn = ttk.Button(text='Print', command=print_input).pack()

lbl = tkinter.Label(window, text='')
lbl.pack()

test_text = tkinter.Text(window,
                         height=5,
                         width=20)

# test = TextAndButton(window, test_text, colored_btn)

# run the app
window.mainloop()
