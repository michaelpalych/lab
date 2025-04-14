import tkinter as tk
from tkinter import scrolledtext
import math

#итерационная реализация функции F(n)
def F_iterative(n):
    results = {1: -1, 2: -1}
    for i in range(3, n + 1):
        if i % 2 == 0:
            results[i] = (-1) ** i * ((results[i - 2] / math.factorial(2 * i)) - (i - 1))
        else:
            results[i] = math.factorial(i - 1)
    return results[n]

#обработчик кнопки
def calculate():
    try:
        n = int(entry.get())
        if n < 1:
            raise ValueError("n должно быть натуральным числом")
        result = F_iterative(n)
        output_text.insert(tk.END, f"F({n}) = {result}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Ошибка: {str(e)}\n")

#создание основного окна
window = tk.Tk()
window.title("Вычисление рекуррентной функции F(n)")
window.geometry("500x400")

#метка и поле ввода
label = tk.Label(window, text="Введите n (натуральное число):")
label.pack(pady=5)

entry = tk.Entry(window, width=20)
entry.pack(pady=5)

#кнопка запуска
button = tk.Button(window, text="Вычислить F(n)", command=calculate)
button.pack(pady=10)

#поле вывода с прокруткой
output_text = scrolledtext.ScrolledText(window, width=60, height=15)
output_text.pack(padx=10, pady=10)

#запуск приложения
window.mainloop()
