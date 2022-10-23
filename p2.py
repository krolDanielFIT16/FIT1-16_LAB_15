import tkinter as tk

win = tk.Tk()

fr = tk.Frame(master=win, borderwidth=1)

inp = tk.Entry(master=fr, width=25)
lb = tk.Label(text="Enter list, delimiter is \",\"", master=fr)
inp.grid(row=0, column=1)
lb.grid(row=0, column=0)


def btn_handler():
    lst = inp.get().replace(" ", "").split(",")
    lst = list(map(int, lst))
    lst.sort(reverse=True)
    lst = list(map(str, lst))
    inp.delete(0, tk.END)
    inp.insert(0, ",".join(lst))


btn = tk.Button(text="Sort", command=btn_handler)


fr.pack()
btn.pack()
win.mainloop()
