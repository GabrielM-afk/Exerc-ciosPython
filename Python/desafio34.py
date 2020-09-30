s = float(input('Qual é o seu salário: '))

if s <= 1250:
    a = s + (s * 15) / 100

else:
    a = s + (s * 10) / 100

print('O seu salário ficará R$ {:.2f} com o aumento'.format(a))