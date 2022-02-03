import tkinter as tk
import os
import sys


def run():
    global run_win, run_win_canvas, a, time
    run_win = tk.Tk()
    run_win.title('Attendance Overlay')
    run_win.geometry('400x180')

    run_win_canvas = tk.Canvas(run_win, bg = '#DDE392', height=180, width=400)
    run_win_canvas.pack()

    a = '1'
    time = tk.Label(run_win_canvas, text=a)
    run_win_canvas.create_window(200, 40, window = time)

    def update():
        global a
        b = int(a)
        b += 1
        a = str(b)
        time.config(text=a)
        time.update_idletasks()

    run_win.after(2000, update)
    run_win.mainloop()

run()