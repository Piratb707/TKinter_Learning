import tkinter as tk
from tkinter import ttk
import webbrowser

# Создание приложения
app = tk.Tk()
app.title("Поисковая система")

# Создание текстовой надписи
serch_label = ttk.Label(app, text='Поиск')
serch_label.grid(row=0, column=0)

# Создание поля для ввода информации
text_field = ttk.Entry(app, width=25)
text_field.grid(row=0, column=1)

# Функция поиска информации в интернете
def search():
    if text_field.get().strip() != "":
        webbrowser.open('https://www.google.com/search?q=' + text_field.get())

def searchBtn():
    search()

def enterBtn(event):
    search()

# Кнопка поиска
btn_search = ttk.Button(app, text='Найти', width=10, command=searchBtn)
btn_search.grid(row=0, column=2)

# Отслеживание события нажатия на клавишу Enter
text_field.bind('<Return>', enterBtn)

# Отображение по верх всех окон
app.wm_attributes('-topmost', True)



# Функция, позволяющая не закрывать приложение
app.mainloop()
