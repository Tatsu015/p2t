import time
import tkinter
import tkinter as tk
from tkinter import ttk

from snipper import Snipper
from translator import Translator
from p2t import P2T
from p2t_thread import P2TThread

root = tkinter.Tk()
root.title("p2e")

s = Snipper()
t = Translator()
p = P2T(s, t)
p2t = P2TThread(p)


def start() -> None:
    p2t.start()
    start_button["state"] = "disable"
    stop_button["state"] = "normal"
    print("start")


def stop() -> None:
    print("stop")
    p2t.pause()
    start_button["state"] = "normal"
    stop_button["state"] = "disable"


def exit():
    print("exit")
    p2t.exit()
    print("close window")
    root.destroy()


# # create window
frame = ttk.Frame(root)
frame.pack()


start_button = tk.Button(frame, text="Start", state="normal", command=start)
start_button.pack()

stop_button = tk.Button(frame, text="Stop", state="disable", command=stop)
stop_button.pack()

root.protocol("WM_DELETE_WINDOW", exit)
root.attributes("-topmost", True)


root.mainloop()
