km = float(input('Qual é a sua velocidade atual ? \n\r'))

if km > 80:
    m = (km - 80) * 7
    print('\nSua mullta é de R$ {:.2f}'.format(m))
else:
    print('\nContinue com sua viagem, dirija com segurança..')