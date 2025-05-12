import timeit
import matplotlib.pyplot as plt
from math import factorial

def recursive_f(n):
    if n in (1, 2):
        return -1
    return (-1)**n * (recursive_f(n - 2) / (factorial(2 * n)) - (n - 1)) if n % 2 == 0 else factorial(n - 1)

def iterative_f(n):
    if n in (1, 2):
        return -1
    f_prev = -1
    for i in range(3, n + 1):
        f_prev = (-1)**i * (f_prev / (factorial(2 * i)) - (i - 1)) if i % 2 == 0 else factorial(i - 1)
    return f_prev

results = {'n': list(range(1,21))} #макс рабочая глубина 70
results['Recursive'] = [recursive_f(n) for n in results['n']]
results['Iterative'] = [iterative_f(n) for n in results['n']]
results['Rec_Time'] = [timeit.timeit(lambda: recursive_f(n), number=1000) for n in results['n']]
results['Iter_Time'] = [timeit.timeit(lambda: iterative_f(n), number=1000) for n in results['n']]

plt.figure(figsize=(10, 5))
plt.plot(results['n'], results['Rec_Time'], label='Recursive Time', color='orange')
plt.plot(results['n'], results['Iter_Time'], label='Iterative Time', color='green')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.title('Сравнение времени выполнения: Рекурсивный vs Итеративный')
plt.show()
