#criar um programa que leia o preço de um produto e recalcule seu novo preço com 5% de desconto
preço = float(input('Qual o preço do produto? '))
por_cento = preço / 100
novo_preço = preço - (5*por_cento)
print('O preço com 5% de desconto é {:.2f}' .format(novo_preço))

#pode ser feito de outra forma também
# x --- 100%
# y ---- 5%
# y = x * 5 / 100
# A lógica é que 5 / 100 lê-se "cinco por cento"
# Se multiplica o valor total por essa fração para saber o quanto é 5 por cento desse valor total
# Dessa forma se faz o código:
# preço = float(input('Preço do produto: R$'))
#novo_preço = preço - (preço * 5 / 100)
#print('preço com 5% de desconto é R${:.2f}.' .format(novo_preço))