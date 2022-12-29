import tkinter as tk
from tkinter import ttk
import webbrowser

app = tk.Tk()
app.title("Поисковая система")

serch_label = ttk.Label(app, text='Поиск')
serch_label.grid(row=0, column=0)

text_field = ttk.Entry(app, width=25)
text_field.grid(row=0, column=1)

app.mainloop()
