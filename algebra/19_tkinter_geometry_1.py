import tkinter as tk

root = tk.Tk()

# Do sad smo vidjeli pack() Geometry Manager, a sada ćemo se upoznati i s place()

root.title('Algebra - Python Developer')
root.geometry('600x400')

btn_image = tk.PhotoImage(file='python.gif')

button_image = tk.Button(root, 
                         text = 'Gumbic sa slikicom',
                         image = btn_image,
                         compound = tk.CENTER)

button_image.place(x = 300, y = 75)

root.mainloop()