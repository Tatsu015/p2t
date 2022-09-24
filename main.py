from csv import Sniffer
import tkinter
import tkinter as tk
from tkinter import ttk
import pyautogui
from PIL import Image, ImageTk


from snipper import Snipper
from translator import Translator
from p2t import P2T

s = Snipper()
t = Translator()
p2t = P2T(s, t)

root = tkinter.Tk()
root.title("p2e")


# def take_fullscreen_shot():
#     # take screen shot
#     rate = 2.5
#     tmp_img = pyautogui.screenshot()
#     img = tmp_img.resize(
#         size=(int(tmp_img.width / rate), int(tmp_img.height / rate)),
#         resample=Image.Resampling.BILINEAR,
#     )
#     # TODO I'm not sure, but screen shot cannot take without save...
#     img.save("test.png")
#     img_tk = ImageTk.PhotoImage(img)

#     w = tk.Toplevel()
#     w.attributes("-fullscreen", True)
#     g_canvas1 = tkinter.Canvas(w, bg="black", highlightthickness=0)
#     g_canvas1.pack(fill=tk.BOTH, expand=True)
#     g_canvas1.create_image(0, 0, image=img_tk, anchor=tkinter.NW)
#     g_canvas1.pack()


def start()->None:
    p2t.start()
    stop_button["state"] = "normal"
    print("start")


def stop()->None:
    print("stop")
    p2t.stop()
    stop_button["state"] = "disable"


# # create window
frame = ttk.Frame(root)
frame.pack()



start_button = tk.Button(frame, text="Start", state="normal", command=start)
start_button.pack()

stop_button = tk.Button(frame, text="Stop", state="disable", command=stop)
stop_button.pack()

def click_close():
    stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", click_close)

root.mainloop()
