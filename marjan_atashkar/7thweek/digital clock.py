import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = tk.Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')

lbl.pack(anchor = 'center')
time()

root.mainloop()
