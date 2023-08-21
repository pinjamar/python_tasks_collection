import tkinter as tk
from time import strftime
from MagicMirror import *

def my_time():
  time_string = strftime('%H:%M:%S') # time format 
  hours_label.config(text=time_string)
  hours_label.after(1000,my_time) # time delay of 1000 milliseconds

root = tk.Tk()
root.title('Magic Mirror Aplikacija')
# root.geometry('600x900')
root.configure(bg='#8EE5EE')

daily_qt_frame = tk.Label(root,text=daily_quote(),bg='#8EE5EE', font=('Arial BOLD',12), fg='#EE7600')
daily_qt_frame.pack(pady=20)

my_font=('times',52,'bold')
hours_label =  tk.Label(root,font = my_font,bg='#8EE5EE', fg='#EE7600')
hours_label.pack(side='bottom', pady=10)
my_time()

daily_temp_st = tk.Label(root, text = temperature_st(), font=('Ariel', 35),bg='#8EE5EE',fg='#EEC900')
daily_temp_st.pack(side='bottom')

daily_date = tk.Label(root,text=date(),bg='#8EE5EE',font=('Arial BOLD',12), fg='#EE7600')
daily_date.pack(side='bottom')
root.mainloop()