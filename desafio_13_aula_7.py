# criar um programa que leia o salário de um empregado e o recalcule com um aumento de 15%
salário = float(input('Qual o salário atual do empregado? : R$'))
por_cento = salário/100
novo_salário = salário + (15*por_cento)
print('O novo salário será R${:.2f}'.format(novo_salário))
