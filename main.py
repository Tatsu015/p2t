import tkinter
import tkinter as tk
from tkinter import ttk
import pyautogui
from PIL import ImageTk

root = tkinter.Tk()
root.title('p2e')

def trans():
    print('trans!')

def take_fullscreen_shot():
    # take screen shot
    img = pyautogui.screenshot()
    # TODO I'm not sure, but screen shot cannot take without save... 
    img.save('test.png')
    img_tk = ImageTk.PhotoImage(img)

    w = tk.Toplevel()
    g_canvas1 = tkinter.Canvas(w,
                                bg="black",
                                width=500,
                                height=500)

    g_canvas1.create_image(0, 0, image=img_tk, anchor=tkinter.NW)
    g_canvas1.pack()

# create window
frame = ttk.Frame(root)
frame.pack()

text = tk.StringVar(frame)
text.set('Trans')

button = tk.Button(frame, text='Tr', command=take_fullscreen_shot)
button.pack()

root.mainloop()
