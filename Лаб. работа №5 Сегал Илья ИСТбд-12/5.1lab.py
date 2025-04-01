import itertools, time

P, B, U, Pl = 300, 500, 200, 600  

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    return result, time.perf_counter() - start

# Алгоритмический способ
outfits_loop, loop_time = measure_time(lambda P, B, U, Pl: 
    [(f'Пиджак {p+1}', f'Блузка {b+1}', f'Юбка {u+1}') for p in range(P) for b in range(B) for u in range(U)] +
    [(f'Платье {pl+1}',) for pl in range(Pl)], P, B, U, Pl)

# С использованием itertools
outfits_itertools, itertools_time = measure_time(lambda P, B, U, Pl: 
    list(itertools.product(range(1, P+1), range(1, B+1), range(1, U+1))) +
    [(pl,) for pl in range(1, Pl+1)], P, B, U, Pl)

print(f'Алгоритмический метод: {len(outfits_loop)} нарядов, время: {loop_time:.6f} сек.')
print(f'Метод itertools: {len(outfits_itertools)} нарядов, время: {itertools_time:.6f} сек.')
