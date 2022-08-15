viagem = float(input('Digite a quantidade de KM da viagem:'))

if 200 >= viagem:
    print(f'Uma viagem de {viagem}KM irá ter uma passagem de custo R${(viagem*50/100)}0')
else:
    print(f'Uma viagem de {viagem}KM irá ter uma passagem de custo R${(viagem*45/100)}0')
