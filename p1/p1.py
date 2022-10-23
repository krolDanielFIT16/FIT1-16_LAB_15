import tkinter as tk
import p1_module

win = tk.Tk()
child = []
Lmn = tk.Label(text="Min")
Emx = tk.Entry(fg="black", bg="white", width=30)
Lmx = tk.Label(text="Max")
Emn = tk.Entry(fg="black", bg="white", width=30)


def btn_handler():
    for i in child:
        i.destroy()
    nwin = tk.Toplevel()
    child.append(nwin)
    canvas = tk.Canvas(nwin, width=300, height=200, background="blue")
    canvas.pack()
    p1_module.drawFunc(canvas, int(Emn.get()), int(Emx.get()), width=300, height=200)


btn = tk.Button(text="Calculate", command=btn_handler)

Lmn.grid(row=0, column=0)
Emn.grid(row=0, column=1)
Lmx.grid(row=1, column=0)
Emx.grid(row=1, column=1)
btn.grid(row=3, column=1)
win.mainloop()
