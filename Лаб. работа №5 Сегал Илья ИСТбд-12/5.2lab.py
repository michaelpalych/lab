import itertools, time, random

P, B, U, Pl = 100, 100, 100, 100
colors = ['красный', 'синий', 'зелёный', 'чёрный', 'белый']
jackets, blouses, skirts, dresses = [[random.choice(colors) for _ in range(x)] for x in [P, B, U, Pl]]
restricted = {('красный', 'зелёный'), ('чёрный', 'чёрный')}

start = time.perf_counter()
outfits = ([(f'Пиджак {p+1} ({jackets[p]})', f'Блузка {b+1} ({blouses[b]})', f'Юбка {u+1} ({skirts[u]})') 
           for p in range(P) for b in range(B) for u in range(U) if (jackets[p], skirts[u]) not in restricted] +
          [(f'Платье {pl+1} ({dresses[pl]})',) for pl in range(Pl)])
time_taken = time.perf_counter() - start

print(f'Нарядов: {len(outfits)}, время: {time_taken:.6f} сек.')
print(f'Оптимальный наряд: {min(outfits, key=len)}')
