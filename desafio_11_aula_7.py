#criar um progrma que receba a altura e a largura de uma parede e calcule sua área e o quanto de tinta será necessária para pintá-la, levando em consideração que 1L de tinta pinta 2m^2
heigth = float(input('Qaual a altura em m da parede? '))
length = float(input('Qual a largura em metros? '))
area = heigth*length
paint = area / 2
print('A área total da parede é de {:.1f}m^2, então são precisos {:.1f}L de tinta.'.format(area,paint))
