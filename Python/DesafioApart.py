import sqlite3, time

senhaMax = "123"

print('Welcome !! \n\r')

passw = input('Get in your senhaMax: ')
if passw != senhaMax:
    print('Senha inválida! Adeus...')
    exit()

conn = sqlite3.connect('password2.db')

cursor = conn.cursor()

class Cliente:
    def __init__(self, user, wordpass):
        self.user = user
        self.wordpass = wordpass

    user = str(input('What is your username ? \n'))
    wordpas = str(input('And your password ? \n'))

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id_user auto_increment PRIMARY KEY,
    name VARCHAR NOT NULL,
    pass VARCHAR NOT NULL
);

CREATE TABLE extract(
    id_extract primary key auto_incremente,
    extract references users,
    
)


CREATE TABLE IF NOT EXISTS accont(
    balance FLOAT NOT NULL,
    transfer CHAR NOT NULL,
   withdraw FLOAT NOT NULL,
    deposit FLOAT NOT NULL,
    extract FLOAT NOT NULL 
);
''')

wordpas = senhaMax

def menu():
    print('*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('-* t :   transfer               *-')
    print('-* w :   Withdraw/Sacar         *-')
    print('-* d :   Deposit                *-')
    print('-* e :   Extract                *-')
    print('-* q :   Quit                   *-')
    print('*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*') 

while True:
    menu()
    op = input('What do you want to do ?')
    if op not in ['t', 'w', 'd', 'e', 'q']:
        print('Invalid option!')
        continue

    if op == 'q':
        break
'''

    if op == 'e':


    if op == 'd':


    if op == 'w':



    if op == 't':
'''
#Class
#Sintaxe
#Marca, Memória ram,placa de video

'''

class Computador:

#Propriedades    
    def __init__(self, marca, memoria_ram, placa_de_video):
       self.marca = marca
       self.memoria_ram = memoria_ram
       self.placa_de_video = placa_de_video

#Métodos
    def Ligar(self):
        print('estou ligando')

    def Desligar(self):
        print('estou desligando')

    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus','16g','Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()

#ligar, Desligar, Exibir configurações
'''