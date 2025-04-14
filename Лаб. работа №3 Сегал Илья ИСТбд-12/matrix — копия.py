from math import prod

def read_matrix(filename): return [list(map(int, line.split())) for line in open(filename)]
def print_matrix(m, name): print(f"\n{name}:"); [print(" ".join(f"{x:4}" for x in row)) for row in m]
def transpose(m): return [list(row) for row in zip(*m)]

def get_diagonal_regions(n):
    a1, a2, a3, a4 = [], [], [], []
    for i in range(n):
        for j in range(n):
            if i < j and i + j < n - 1: a1.append((i, j))
            elif i < j and i + j > n - 1: a2.append((i, j))
            elif i > j and i + j > n - 1: a3.append((i, j))
            elif i > j and i + j < n - 1: a4.append((i, j))
    return a1, a2, a3, a4

def build_F(A):
    n = len(A)
    F = [row[:] for row in A]
    a1, a2, a3, _ = get_diagonal_regions(n)
    even_count = sum(1 for i, j in a2 if j % 2 == 1 and A[i][j] % 2 == 0)
    perimeter = [A[i][j] for i, j in a3 if i == n - 1 or j in {0, n - 1} or i + j == n]
    perim_prod = prod(perimeter) if perimeter else 0
    swap = zip(a1, a3) if even_count > perim_prod else zip(a1, a2)
    for (i1, j1), (i2, j2) in swap:
        F[i1][j1], F[i2][j2] = F[i2][j2], F[i1][j1]
    return F, even_count, perim_prod

def compute_result(A, F, K):
    n = len(A)
    A_T, F_T = transpose(A), transpose(F)
    FA = [[F[i][j] + A[i][j] for j in range(n)] for i in range(n)]
    KAT = [[K * A_T[i][j] for j in range(n)] for i in range(n)]
    mult = [[sum(KAT[i][k] * FA[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return [[mult[i][j] - K * F_T[i][j] for j in range(n)] for i in range(n)]

K = int(input("Введите K: "))
A = read_matrix("matrix.txt")
F, even, perim = build_F(A)
R = compute_result(A, F, K)

print_matrix(A, "Исходная матрица A")
print(f"\nЧётных в нечётных столбцах области 2: {even}")
print(f"Произведение по периметру области 3: {perim}")
print_matrix(F, "Матрица F после замены")
print_matrix(R, "Результат выражения ((K*A^T)*(F+A) - K*F^T)")
