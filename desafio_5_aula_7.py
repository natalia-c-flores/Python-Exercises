#criar um programa que mostre o antescessor e o sucessor de um dado número
n = int(input('Digite um número\n'))
a = n - 1
s = n + 1
print('Antecessor = {} e Sucessor = {}'.format(a,s))

#Nesse caso ainda poderia ser feito simplesmente:
# n = int(input('Digite um número\n'))
# print('Antecessor = {} e Sucessor = {}'.format(n-1,n+1))
# Dessa forma não são criadas novas variáveis e isso economiza memória do computador
# Caso esses valores serem de interesse para utilização posteriormente ao longo do código é mais interessante realmente salvar eles em variáveis
