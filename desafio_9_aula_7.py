#criar um programa que receba um número e mostre a sua tabuada.
n = int(input('Digite um número: '))
t1 = n*1
t2 = n*2
t3 = n*3
t4 = n*4
t5 = n*5
t6 = n*6
t7 = n*7
t8 = n*8
t9 = n*9
t10 = n*10
print('\n')
print(13*'-')
print(' 1 x  {} = {}\n' .format(n,t1))
print(' 2 x  {} = {}\n' .format(n,t2))
print(' 3 x  {} = {}\n' .format(n,t3))
print(' 4 x  {} = {}\n' .format(n,t4))
print(' 5 x  {} = {}\n' .format(n,t5))
print(' 6 x  {} = {}\n' .format(n,t6))
print(' 7 x  {} = {}\n' .format(n,t7))
print(' 8 x  {} = {}\n' .format(n,t8))
print(' 9 x  {} = {}\n'.format(n,t9))
print(' 10 x {} = {}' .format(n,t10))
print(13*'-')

#jeito alternativo mais fácil:
#n = int(input('Digite um número para ver sua tabuada: '))
#print(' {} x {:2} = {}\n' .format(1, n, 1*n))
#print(' {} x {:2} = {}\n' .format(2, n, 2*n))
#print(' {} x {:2} = {}\n' .format(3, n, 3*n))
#print(' {} x {:2} = {}\n' .format(4, n, 4*n))
#print(' {} x {:2} = {}\n' .format(5, n, 5*n))
#print(' {} x {:2} = {}\n' .format(6, n, 6*n))
#print(' {} x {:2} = {}\n' .format(7, n, 7*n))
#print(' {} x {:2} = {}\n' .format(8, n, 8*n))
#print(' {} x {:2} = {}\n'.format(9, n, 9*n))
#print(' {} x {:2} = {}' .format(10, n, 10*n))
