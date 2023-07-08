# Import tkinter modul
import tkinter as tk

# DIO ZA FUNKCIJE
def click():
    label.config(text='Nova poruka iz funkcije "click"',
                 font = ('Helvetica', 18),
                 fg = 'red')

root = tk.Tk()

root.title('Algebra - Python Developer')
root.geometry('600x400')

label = tk.Label(root, 
                 text = "PORUKA", 
                 font = ('Segoe UI', 16))

label.pack(padx = 30, pady = 40)

button_click = tk.Button(root, text = 'Klikni me!', command = click).pack(padx=10, pady=10)

image_in_label = tk.PhotoImage(file='python-logo.png').subsample(7)
label_picture = tk.Label(root,
                         text = 'Tekst unutar Labela',
                         font = ('Segoe UI', 20),
                         compound = tk.CENTER,
                         image = image_in_label)

label_picture.pack(padx=5, pady = 5)
root.mainloop()
