nome = input('Qual é o seu nome completo? \n\r')
div = nome.rsplit()

print(f'Primeiro nome: {div[0]}')
print(f'Último nome: {div[-1]}')