# compreensão de listas
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]  # copiando
print(l2)

exemplo2 = [v * 2 for v in l1]  # multiplicando cada elemento por 2
print(exemplo2)

exemplo3 = [(v, v2) for v in l1 for v2 in range(3)]
# iterando e criando tuplas num range 3
print(exemplo3)
print('-' * 50)

l11 = ['Vinicius', 'Larissa', 'Cintia']
ex4 = [v.replace('i', 'e') for v in l11]  # fazendo um replace numa lista
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
print('proximo é um dict?')
ex5 = [(x, y) for y, x in tupla]  # convertendo uma tupla em um dict
print(ex5)
ex5 = dict(ex5)
print(ex5)
l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]  # usando ifs
print(ex6)
#  ex7 = [v if v % 3 == 0 and v % 8 == 0 else 'Não é' for v in l3]  # if else
#  print(ex7)
print('-' * 50)

lista = [
    ('key', 'valor'),
    ('key1', 'valor1')
]

d1 = {x: y for x, y in lista}  # transformando em dicionário.
print(d1)

d2 = {x: y for x, y in enumerate(range(5))}
# usando o range para fazer um dicionário
print(d2)

d3 = {x for x in range(5)}  # type é set
print(d3)

d4 = {f'chave_{x}': x**2 for x in range(1, 5+1)}  # type é set
print(d4)
