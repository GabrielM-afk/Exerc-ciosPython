import time

nome = str(input('Qual é o seu nome completo ? \n')).strip()

pn = nome.split()

print('\n       Analisando seu nome...      \n')

time.sleep(1)

print('O seu nome maiúsculo é {}'.format(nome.upper()))
print('O seu nome minúsculo é {}'.format(nome.lower()))
print('O seu nome tem {} carecteres'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e tem {} letras'.format(pn[0] ,nome.find(' ')))