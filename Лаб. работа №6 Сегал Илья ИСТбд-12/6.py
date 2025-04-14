import time
import math
import matplotlib.pyplot as plt
import pandas as pd

# рекурсивная реализация функции
def F_recursive(n):
    if n == 1 or n == 2:
        return -1
    if n % 2 == 0:
        return (-1) ** n * ((F_recursive(n - 2) / math.factorial(2 * n)) - (n - 1))
    else:
        return math.factorial(n - 1)

# итерационная реализация функции
def F_iterative(n):
    results = {1: -1, 2: -1}
    for i in range(3, n + 1):
        if i % 2 == 0:
            results[i] = (-1) ** i * ((results[i - 2] / math.factorial(2 * i)) - (i - 1))
        else:
            results[i] = math.factorial(i - 1)
    return results[n]

# максимальное значение n для тестирования
max_n = 45

# список для хранения результатов
results = []

# вычисления и измерения времени
for n in range(1, max_n + 1):
    # рекурсивный способ
    start = time.perf_counter()
    try:
        f_rec = F_recursive(n)
        time_rec = (time.perf_counter() - start) * 1000  # мс
    except RecursionError:
        f_rec = None
        time_rec = None

    # итерационный способ
    start = time.perf_counter()
    f_it = F_iterative(n)
    time_it = (time.perf_counter() - start) * 1000  # мс

    # сохраним результаты
    results.append({
        'n': n,
        'F_recursive': f_rec,
        'F_iterative': f_it,
        'time_recursive_ms': time_rec,
        'time_iterative_ms': time_it
    })

# создание таблицы
df = pd.DataFrame(results)
print(df.to_string(index=False))

# построение графика времени
plt.plot(df['n'], df['time_recursive_ms'], label='Рекурсивно', marker='o')
plt.plot(df['n'], df['time_iterative_ms'], label='Итеративно', marker='s')
plt.xlabel('n')
plt.ylabel('Время выполнения (мс)')
plt.title('Сравнение времени: рекурсия vs итерация')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
