#Attendance Keeper
#Karan Arora

import tkinter as tk
import sys
import os

os_name = os.name

def window():
    win = tk.Tk()
    win.title("Attendance Keeper")
    win.geometry("300x300+200+200")
    win.resizable(width=False, height=False)

    win_canvas = tk.Canvas(win, bg='#011C27', height=300, width=300)
    win_canvas.pack()

    heading = tk.Label(win_canvas, text='Attendance Keeper', bg='#011C27', fg='orange',  font=('helvetica', 20, 'underline bold'))
    win_canvas.create_window(150, 30, window = heading)

    start_button = tk.Button(win_canvas, text='Start', bg='lightgreen', padx=20, font=('', 14))
    win_canvas.create_window(150, 120, window = start_button)

    exit_button = tk.Button(win_canvas, text='Exit', bg='red', padx=20, font=('', 14))
    win_canvas.create_window(150, 200, window = exit_button)

    win.mainloop()

if __name__ == '__main__':
    window()