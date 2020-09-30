'''             Priemria Maneira
co = float(input('Comprimento do cateto oposto: \n\r'))
ca = float(input('Comprimento do cateto adjacente: \n\r'))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: \n\r'))
ca = float(input('Comprimento do cateto adjacente: \n\r'))

h = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(h))