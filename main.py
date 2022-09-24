import tkinter
import tkinter as tk
from snipper import Snipper
from translator import Translator
from p2t import P2T
from p2t_thread import P2TThread

# define globals
s = Snipper()
t = Translator()
p = P2T(s, t)
p2t = P2TThread(p)

root = tkinter.Tk()
root.title("p2e")
root.attributes("-topmost", True)

# define callback functions
def on_start() -> None:
    p2t.exec()
    start_button["state"] = "disabled"
    stop_button["state"] = "normal"


def on_stop() -> None:
    p2t.pause()
    start_button["state"] = "normal"
    stop_button["state"] = "disabled"


def on_exit():
    print("exit")
    p2t.exit()
    print("close window")
    root.destroy()


# define callback settings
start_button = tk.Button(root, text="Start", state="normal", command=on_start)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(root, text="Stop", state="disabled", command=on_stop)
stop_button.pack(side=tk.RIGHT)

root.protocol("WM_DELETE_WINDOW", on_exit)

# start application
root.mainloop()
