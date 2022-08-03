#criar um programa que leia quanto dinheiro em reais uma pessoa tem na carteira e diga quantos dólares podem ser comprados. Considerar US$ 1,00 = R$ 3,27
r = float(input('Valor em R$ na carteira: R$ '))

d = r / 3.27

print('Você pode comprar US$ {:.2f}.\n' .format(d))
