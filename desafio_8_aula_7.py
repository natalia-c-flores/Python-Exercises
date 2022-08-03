#criar um programa que receba um valor em metros e mostre esse valor em cm e mm.
m = float(input('Digite um valor em metros: '))
cm = m*100
mm = m*1000
print('Valor em cm: {:.0f}\nValor em mm: {:.0f}\n' .format(cm,mm))
