carro = int(input('Digite qual é a velocidade do carro:'))
multa = (carro - 80) * 7

if carro > 80:
    print(f'Peço desculpas, porém você será multado em R${multa},00')
else:
    print('Isso mesmo, continue na lei')
