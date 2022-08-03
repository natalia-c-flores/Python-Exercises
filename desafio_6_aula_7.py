#criar um programa que leia um número e calcule seu dobro, triplo e raiz quadrada
n = int(input('digite um número\n'))
d = 2 * n
t = 3 * n
r = n**(1/2)
print('O dobro desse número é {}\n O triplo é {}\n A raíz quadrada é {:.2f}' .format(d,t,r))

# Também pode ser feito sem as demais variáveis.
# n = int(input('digite um número\n'))
# print('O dobro desse número é {}\n O triplo é {}\n A raíz quadrada é {:.2f}' .format(n*2, n*3, (n**(1/2))))
# Caso os valores sejam importantes para o uso no resto do programa é interessante salvá-los em variáveis.
