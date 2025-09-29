def transpose(matrix):

    if len(matrix) == 0:
        return []

    rows = len(matrix)  # сколько строк
    cols = len(matrix[0])  # сколько столбцов (в первой строке)

    # создаём новую матрицу: cols строк, rows столбцов
    new_matrix = []
    i = 0
    while i < cols:
        new_row = []
        j = 0
        while j < rows:
            new_row.append(matrix[j][i])
            j = j + 1
        new_matrix.append(new_row)
        i = i + 1

    return new_matrix

print("Транспонирование матрицы")

# ввод матрицы
print("Введите матрицу построчно. Каждую строку через пробел. Пропуск строки = конец ввода")

matrix = []
while True:
    line = input()
    if line == "":
        break
    row = []
    parts = line.split()
    for part in parts:
        row.append(int(part))
    matrix.append(row)

if len(matrix) == 0:
    print("Матрица пуста.")
else:
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    transposed = transpose(matrix)

    print("\nТранспонированная матрица:")
    for row in transposed:
        print(row)