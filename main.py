import tkinter
import tkinter as tk
from tkinter import ttk

from snipper import Snipper
from translator import Translator
from p2t import P2T

s = Snipper()
t = Translator()
p2t = P2T(s, t)

root = tkinter.Tk()
root.title("p2e")


def start() -> None:
    p2t.start()
    stop_button["state"] = "normal"
    print("start")


def stop() -> None:
    print("stop")
    p2t.stop()
    stop_button["state"] = "disable"


def click_close():
    stop()
    root.destroy()


# # create window
frame = ttk.Frame(root)
frame.pack()


start_button = tk.Button(frame, text="Start", state="normal", command=start)
start_button.pack()

stop_button = tk.Button(frame, text="Stop", state="disable", command=stop)
stop_button.pack()

root.protocol("WM_DELETE_WINDOW", click_close)

root.mainloop()
