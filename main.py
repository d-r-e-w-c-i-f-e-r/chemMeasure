import os.path
import tkinter.messagebox
from tkinter import *
from tkinter import ttk, filedialog


window = Tk()
window.title("Chem Measurement Wizard")
window.geometry("600x200")


def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('MP4 Video', '*.mp4')])
    if file:
        fp.config(text=os.path.abspath(file.name))
        print("file read")
        file.close()


# args:
#   video | type: FILE
#   mag | type: number
def process():
    print("processing video")


top_frame = Frame(window)
top_frame.pack()
fp = tkinter.Label(top_frame, text='')
fp.pack(side=LEFT)
browse_button = ttk.Button(top_frame, text='Browse', command=open_file).pack(side=LEFT, pady=20)

mid_frame = Frame(window)
mid_frame.pack()
# this is where the magnification selection will live
mag = 1
mag_lbl = tkinter.Label(mid_frame, text='Magnification: ').pack(side=LEFT)
mag_scale = tkinter.Scale(mid_frame, variable=mag, from_=1, to=100, showvalue=0, orient=HORIZONTAL)
x = tkinter.Label(mid_frame, text='x').pack(side=RIGHT, padx=0)
mag_val = tkinter.Label(mid_frame, textvariable=mag).pack(side=RIGHT)
mag_scale.pack()


bottom_frame = Frame(window)
bottom_frame.pack()
# this is where the run button will live
run = ttk.Button(bottom_frame, text='Run', command=process).pack(pady=20)

# run the app
window.mainloop()
