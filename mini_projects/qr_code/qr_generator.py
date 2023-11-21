import tkinter as tk
from tkinter import filedialog
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
        self.geometry('400x400')

        # Entry field
        self.entry_string = ctk.StringVar(value='test')
        # self.entry_string.trace('w', self.create_qr)
        EntryField(self, self.entry_string)

        # QR code
        raw_image = Image.open(
            'mini_projects\qr_code\Placeholder.png').resize((400, 400))
        tk_image = ImageTk.PhotoImage(raw_image)
        self.qr_image = QrImage(self)
        self.qr_image.update_image(tk_image)

        # running the app
        self.mainloop()


class EntryField(ctk.CTkFrame):
    def __init__(self, parent, entry_string):
        super().__init__(master=parent, corner_radius=20, fg_color='#021FB3')
        self.place(relx=0.5, rely=1, relwidth=1,
                   relheight=0.4, anchor='center')
        # grid layout
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')
        # widgets
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.columnconfigure(0, weight=1, uniform='b')
        self.frame.columnconfigure(1, weight=4, uniform='b')
        self.frame.columnconfigure(2, weight=2, uniform='b')
        self.frame.columnconfigure(3, weight=1, uniform='b')
        self.frame.grid(row=0, column=0)

        entry = ctk.CTkEntry(self.frame, textvariable=entry_string, fg_color='#2E54E8',
                             border_width=0, text_color='white')
        entry.grid(row=0, column=1, sticky='nsew')

        button = ctk.CTkButton(self.frame, text="Save",
                               fg_color='#2E54E8', hover_color='#4266f1')
        button.grid(row=0, column=2, sticky='nsew', padx=10)


class QrImage(tk.Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, background='white',
                         bd=0, highlightthickness=0, relief='ridge')
        self.place(relx=0.5, rely=0.3, width=400, height=400, anchor='center')

    def update_image(self, image_tk):
        self.create_image(0, 0, image=image_tk, anchor='nw')


App()
