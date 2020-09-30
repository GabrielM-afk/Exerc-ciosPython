d = int(input('Por quantos dias ele foi alugado? \n\r'))
k = float(input('Quantos Quilômetros foram percorridos? \n\r'))

r = (k * 0.15) + (d * 60)

print('O total a pagar é R$ {:.2f}'.format(r))