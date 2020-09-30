n1 = int(input('Digite o primeiro: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

if n1 < n2 and n1 <n3:
    print(f'O menor número foi {n1}')

elif n2 < n1 and n2 < n3:
    print(f'O menor número foi {n2}')

else:
    print(f'O menor número foi {n3}')

if n1 > n2 and n1 > n3:
    print(f'O maior número foi {n1}')

elif n2 > n1 and n2 > n3:
    print(f'O maior número foi {n2}')

else:
    print(f'O maior número foi {n3}')