import tkinter as tk
import sqlite3
import tkinter.messagebox

root = tk.Tk()

root.geometry("650x800")
root.resizable(0, 0)

answer = tkinter.messagebox.askquestion(title="Ulazak u Admin sustav",
                                        message='Zelite li pokrenuti sustav administracije?')

print(answer)
