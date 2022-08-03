#criar um programa que leia as duas notas de um aluno e calcule a média entre elas
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('A média é: {:.1f}'.format(m))