
def matriz_zeros(linhas, colunas):
    matriz = []
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))
    for l in range(linhas):
        for c in range(colunas):
            matriz[l][c] = 0
            

    return matriz

matriz1 = matriz_zeros(3, 3)
matriz_vazia = [

]
print(matriz1)