import os.path
import tkinter.messagebox
from tkinter import *
from tkinter import ttk, filedialog
from components.processor import Processor


# args:
#   video | type: FILE
#   mag | type: number
def process():
    print("processing video")


class Window:

    def __init__(self):
        self.window = Tk()
        self.window.title("Chem Measurement Wizard")
        self.window.geometry("600x400")
        self.launch()

    def launch(self):
        center_frame = ttk.Frame(self.window)
        center_frame.pack(side="top", pady=10)
        # div1
        frame_1 = Frame(center_frame)
        frame_1.pack(anchor='w')
        fp = tkinter.Label(frame_1, text='Select File:')
        fp.pack(side="left")
        browse_button = ttk.Button(frame_1, text='Browse', command=lambda: self.open_file(fp)).pack(side=LEFT,
                                                                                                    pady=10)

        # div2
        frame_2 = Frame(center_frame)
        frame_2.pack(pady=10, anchor='w')

        validation = self.window.register(self.on_validate)
        label = ttk.Label(frame_2, text="Scale (in pixels):")
        label.pack(side="left")
        scale = ttk.Entry(frame_2, validate="key",
                          validatecommand=(validation, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        scale.pack(side="left")

        # div3
        frame_3 = Frame(center_frame)
        frame_3.pack(pady=10, anchor='w')

        label = ttk.Label(frame_3, text="Minimum Distance:")
        label.pack(side="left")
        min_dist = ttk.Entry(frame_3, validate="key",
                             validatecommand=(validation, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        min_dist.insert(0, "1")
        min_dist.pack(side="left")

        # div4
        frame_4 = Frame(center_frame)
        frame_4.pack(pady=10, anchor='w')

        label = ttk.Label(frame_4, text="Edge Detection:")
        label.pack(side="left")
        param_1 = ttk.Entry(frame_4, validate="key",
                            validatecommand=(validation, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        param_1.insert(0, "100")
        param_1.pack(side="left")

        # div5
        frame_5 = Frame(center_frame)
        frame_5.pack(pady=10, anchor='w')

        label = ttk.Label(frame_5, text="Circle Threshold:")
        label.pack(side="left")
        param_2 = ttk.Entry(frame_5, validate="key",
                            validatecommand=(validation, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        param_2.insert(0, "30")
        param_2.pack(side="left")

        # div6
        frame_6 = Frame(center_frame)
        frame_6.pack(pady=10, anchor='w')

        label = ttk.Label(frame_6, text="Minimum Radius:")
        label.pack(side="left")
        min_rad = ttk.Entry(frame_6, validate="key",
                            validatecommand=(validation, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        min_rad.insert(0, "30")
        min_rad.pack(side="left")

        # div7
        frame_7 = Frame(center_frame)
        frame_7.pack(pady=10, anchor='w')

        label = ttk.Label(frame_7, text="Maximum Radius:")
        label.pack(side="left")
        max_rad = ttk.Entry(frame_7, validate="key",
                            validatecommand=(validation, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        max_rad.insert(0, "0")
        max_rad.pack(side="left")

        # this is where the run button will live
        bottom_frame = Frame(center_frame)
        bottom_frame.pack()
        run = ttk.Button(bottom_frame, text='Run',
                         command=lambda: self.inputs(fp, scale, min_dist, param_1, param_2, min_rad, max_rad)) \
            .pack(pady=20)

        # run the app
        self.window.mainloop()

    @staticmethod
    def open_file(fp):
        file = filedialog.askopenfile(mode='r', filetypes=[('MP4 Video', '*.mp4'), ('AVI Video', '*.avi')])
        if file:
            fp.config(text=os.path.abspath(file.name))
            print("file read")
            file.close()

    @staticmethod
    def on_validate(d, i, P, s, S, v, V, W):
        # d: action (1 for insert, 0 for delete, -1 for others)
        # i: index
        # P: value being inserted or deleted
        # s: current value of the entry
        # S: text string being inserted or deleted
        # v: validation result (1 for valid, 0 for invalid)
        # V: type of validation (1 for focus in, -1 for focus out)
        # W: widget name

        # Allow only numeric values, an empty string, or backspace/delete
        return (d == '1' and P.isdigit()) or P == "" or d == '0'

    def inputs(self, fp, scale, min_d, p1, p2, min_r, max_r):
        if not fp.cget("text") or not scale.get():
            print('nononono')
            return

        result = {
            "file": fp.cget("text"),
            "scale": int(scale.get()),
            "min_dist": float(min_d.get()),
            "p1": float(p1.get()),
            "p2": float(p2.get()),
            "min_rad": int(min_r.get()),
            "max_rad": int(max_r.get())
        }
        self.run(result)

    @staticmethod
    def run(values):
        core = Processor(
            values["file"],
            values["scale"],
            values["min_dist"],
            values["p1"],
            values["p2"],
            values["min_rad"],
            values["max_rad"],
        )

        core.run()
