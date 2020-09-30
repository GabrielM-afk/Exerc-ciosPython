import random, time
n = random.randint(0, 5)

print('-=-' * 10)
print('Estou pensando em um número...')
print('-=-' * 10)
time.sleep(1)
nu = int(input('Tente adivinhar que número eu pensei: '))

print('procesando...')
time.sleep(1)

if nu == n:
    print('Parabéns, tanta de novo..')
else:
    print('Não foi dessa vez, Eu venci')

time.sleep(1.5)
print(f'Eu pensei no {n}')