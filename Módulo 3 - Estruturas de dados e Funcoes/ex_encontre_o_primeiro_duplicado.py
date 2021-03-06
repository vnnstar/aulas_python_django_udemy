"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def encontra(lista):
    for listas in lista:
        lista_duplicado, lista_posicao, cont_valor = [], [], 0
        if len(listas) == len(set(listas)):
            print('-' * 40, f'\nNão existe valor duplicado > -1')
        else:
            for x in range(len(listas)):
                valor = listas[x]
                for i, j in enumerate(listas):
                    if valor == j and i != cont_valor and j not in lista_duplicado:
                        lista_posicao.append(i)
                        lista_duplicado.append(valor)
                cont_valor += 1
            print('-' * 40, f'\nPosição: {lista_posicao},\nDuplica: {lista_duplicado}')
            print(f'O primeiro valor duplicado foi {lista_duplicado[lista_posicao.index(min(lista_posicao))]}')


encontra(lista_de_listas_de_inteiros)
encontra([[1, 2, 3, 3, 2, 1]])

'''
for listas in lista_de_listas_de_inteiros:
    lista_duplicado, lista_posicao = [], []
    cont_valor = 0
    if len(listas) == len(list(set(listas))):
        print(-1)
        print('-' * 40)
    else:
        for x in range(10):
            valor = listas[x]
            for i, j in enumerate(listas):
                if listas[x] == j and i != cont_valor and j not in lista_duplicado:
                    lista_posicao.append(i)
                    lista_duplicado.append(listas[x])
            cont_valor += 1
        print(f'Posição: {lista_posicao},\nDuplica: {lista_duplicado}')
        print(f'O primeiro valor duplicado foi {lista_duplicado[lista_posicao.index(min(lista_posicao))]}')
        print('-' * 40)'''
