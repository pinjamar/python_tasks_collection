import tkinter as tk

root = tk.Tk()

odustani = tk.BooleanVar()

print(odustani.get())

odustani.set(tk.TRUE)

print(odustani.get())

root.mainloop()

