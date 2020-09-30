km = float(input('Qual vai ser a distância da viagem ? \n\r'))

p = km * 0.50 if km <= 200 else km * 0.45

print(f'O total a pagar será de {p}')