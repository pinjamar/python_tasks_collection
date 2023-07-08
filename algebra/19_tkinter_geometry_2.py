import tkinter as tk

root = tk.Tk()
root.title('Algebra - Python developer')

# Sad ćemo pogledati grid() GEOMETRY MANAGER
# grid je najlakše predočiti kao tablic s n redaka i stupaca (red i stupac počinju od 0)

for i in range(3):
    root.columnconfigure(i, weight = 1, minsize = 75)
    root.rowconfigure(i, weight = 1, minsize = 75)
    for j in range(3):

# prva iteracija i = 0, prva iteracija j = 0
# prva iteracije vanjska i = 0, prva iteracija unutarnja j = 1
        frame = tk.Frame(
            root,
            relief = tk.SUNKEN,
            borderwidth = 6
        )

        frame.grid(row = i, column = j, padx = 15, pady = 15)

        label = tk.Label(frame, text = f'Red {i}\nKolona {j}')

        # Svaki frame je pozicioniran pomoću grid(), ALI unutar svakog frame widgeta možemo 
        # upravljati pomoću pack()
        label.pack()

root.mainloop()