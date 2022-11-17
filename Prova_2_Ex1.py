def lista_zeros(tamanho):
    lista = []
    tamanho = int(input("Tamanho da lista: "))
    for l in range(tamanho):
        lista.append(0)
    return lista
lista1 = lista_zeros(5)
lista_vazia = []
for i in lista1:
    preencher = int(input("Digite valores: "))
    lista_vazia.append(preencher)

print(f'Lista: {lista_vazia}')

lista_vazia.sort()
print(f'Lista ordenada: {lista_vazia}')

soma = sum(lista_vazia)
print(f'Soma de todos os valores: {soma}')

maior = max(lista_vazia)
print(f'Maior número da lista: {maior}')

