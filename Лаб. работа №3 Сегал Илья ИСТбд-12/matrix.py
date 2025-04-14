from math import prod

def read_matrix_from_file(filename):
    with open(filename, "r") as file:
        return [list(map(int, line.split())) for line in file]

def print_matrix(matrix, name): 
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{x:4}" for x in row))

def transpose(matrix): 
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def define_regions(N):
    area1, area2, area3 = [], [], []
    for i in range(N):
        for j in range(N):
            if i < j and i + j < N - 1:
                area1.append((i, j))  # область 1 (верх)
            elif i > j and i + j < N - 1:
                area2.append((i, j))  # область 2 (левая)
            elif i > j and i + j > N - 1:
                area3.append((i, j))  # область 3 (нижняя)
    return area1, area2, area3

def build_modified_F(A, K):
    N = len(A)
    area1, area2, area3 = define_regions(N)
    F = [row[:] for row in A]

    even_count = sum(1 for i, j in area2 if j % 2 == 1 and A[i][j] % 2 == 0)

    perim_3 = []
    for i, j in area3:
        if j == 0 or i == N - 1 or i + j == N:
            perim_3.append(A[i][j])
    perimeter_product = prod(perim_3) if perim_3 else 0

    if even_count > perimeter_product:
        for idx in range(min(len(area1), len(area3))):
            i1, j1 = area1[idx]
            i3, j3 = area3[idx]
            F[i1][j1], F[i3][j3] = F[i3][j3], F[i1][j1]
    else:
        for idx in range(min(len(area1), len(area2))):
            i1, j1 = area1[idx]
            i2, j2 = area2[idx]
            F[i1][j1], F[i2][j2] = F[i2][j2], F[i1][j1]

    return F, even_count, perimeter_product

def calculate_expression(A, F, K):
    N = len(A)
    A_T = transpose(A)
    F_T = transpose(F)
    F_plus_A = [[F[i][j] + A[i][j] for j in range(N)] for i in range(N)]
    KAT = [[K * A_T[i][j] for j in range(N)] for i in range(N)]
    result_mult = [[sum(KAT[i][k] * F_plus_A[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    KF_T = [[K * F_T[i][j] for j in range(N)] for i in range(N)]
    result = [[result_mult[i][j] - KF_T[i][j] for j in range(N)] for i in range(N)]
    return result

# === ПРИМЕНЕНИЕ ===

K = int(input("Введите K: "))

# Пример матрицы A (можно заменить чтением из файла)
A = [
 [-1, 8,  1, 1, 1, 1, -1],
 [ 9, -1, 1, 1, 1, -1, 4],
 [ 2, 2, -1, 1, -1, 4, 4],
 [ 2, 2, 2, -1, 4, 4, 4],
 [ 2, 2, -1, 3, -1, 4, 4],
 [ 2, -1, 3, 3, 3, -1, 4],
 [-1, 3, 3, 3, 3, 3, -1],
]

print_matrix(A, "Исходная матрица A")

F, even_count, perimeter_product = build_modified_F(A, K)

print(f"\nЧётных чисел в нечётных столбцах области 2: {even_count}")
print(f"Произведение по периметру области 3: {perimeter_product}")

print_matrix(F, "Изменённая матрица F")

result = calculate_expression(A, F, K)

print_matrix(result, "Результат выражения")
