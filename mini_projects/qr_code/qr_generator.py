import tkinter as tk
# from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode


class App(ctk.CTk):
    def __init__(self):
        # window setup
        ctk.set_appearance_mode('light')
        super().__init__(fg_color='white')

        # customization
        self.title('')
        # self.iconbitmap('empty.ico')
        self.geometry('400x400')

        # Entry field
        EntryField(self)

        # running the app
        self.mainloop()


class EntryField(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.place(relx=0.5, rely=0.5, relwidth=0.5,
                   relheight=0.5, anchor='center')


App()
