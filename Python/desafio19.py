''' primeira maneira
import random
nom = ['Gg', 'Aa', 'Ww', 'Qq']
r = random.choice(nom)
print(r)
'''
from random import choice 
n1 = str(input('Primero aluno: '))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceito aluno: '))
n4 = str(input('Quarto aluno: '))

list = [n1, n2, n3, n4]
escolha = choice(list)

print('O aluno escolhido foi {}'.format(escolha))