frase = str(input('Digite uma frase qualquer: ')).lower().strip()
a = (frase.count('a'))
p = (frase.find('a') + 1)
u = (frase.rfind('a') + 1)

print(f'A letra A aparece {a} vezes')
print(f'O primeiro A aparece na posição {p}')
print(f'O último A aparece na posição {u}')