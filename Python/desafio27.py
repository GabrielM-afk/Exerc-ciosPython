import time
nome = input('Qual é o seu nome completo? \n\r').strip()
div = nome.rsplit()


time.sleep(1)
print('Boa ')
print(f'Primeiro nome: {div[0]}')
print(f'Último nome: {div[-1]}')