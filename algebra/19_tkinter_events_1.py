import tkinter as tk

unesena_slova = ''

def handle_keypress(event):
    print(event.char)
    global unesena_slova
    unesena_slova += str(event.char)
    label_tekst_var.set(unesena_slova)

root = tk.Tk()
root.title('Algebra - Python Developer')
root.geometry('600x400')

label_tekst_var = tk.StringVar()
label_tekst_var.set('Ovo je mjesto gdje će se prikazivati unesena slova')

label_naslov = tk.Label(root,
                        text= 'Key Event',
                        font = ('Segoe UI', 18))

label_naslov.grid(column=0, row=0)

label_ispis = tk.Label(root, 
                       textvariable=label_tekst_var, font = ('Segoe UI', 24), fg = 'red')

label_ispis.grid(column=0, row = 1)

root.bind("<Key>", handle_keypress)

root.mainloop()