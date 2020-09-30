from random import shuffle 
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceito aluno: '))
n4 = str(input('Quarto aluno: '))

list = [n1, n2, n3, n4]

shuffle(list)

print('A ordem sorteada foi')
print(list)
