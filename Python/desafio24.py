import time

city = str(input('What is the name of your city ? \n'))
s = (city[:5].upper() == 'SANTO')


print('Aguarde..')
time.sleep(1)


if s == True:
    print('\n Your city have Santo on the name')

else:
    print('\n What a pity...')