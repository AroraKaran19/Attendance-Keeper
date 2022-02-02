#Attendance Keeper
#Karan Arora

import tkinter as tk
import sys
import os

os_name = os.name

def window():
    win = tk.Tk()
    win.title("Attendance Keeper")
    win.geometry("500x500+200+200")
    win.resizable(width=False, height=False)

    win_canvas = tk.Canvas(win, bg='cyan', height=500, width=500)
    win_canvas.pack()

    heading = tk.Label(win_canvas, text='Attendance Keeper', bg='cyan',
                        font=('helvetica', 20, 'underline bold'))
    win_canvas.create_window(250, 20, window=heading)

    win.mainloop()

if __name__ == '__main__':
    window()