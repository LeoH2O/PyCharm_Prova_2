# Matriz 5x5

matriz = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
]

for l in range(5):
    for c in range(5):
        if l == c:
            matriz[l][c] = 1
        else:
            matriz[l][c] = 0

for l in range(5):
    print(f'{matriz[l]}')
