import random
print('Vou pensar em um número de 1 a 5, tente adivinhar...')
n = 1, 2, 3, 4, 5
n1 = int(input('Escolha um número de 1 a 5:'))
n2 = random.choice(n)

if n1 == n2:
    print(f'Parabéns, você acertou! O número escolhido foi: {n2}')
else:
    print(f'Perdeu para o computador! O número escolhido foi: {n2}')