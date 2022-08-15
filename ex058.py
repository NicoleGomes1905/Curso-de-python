import random
c = 0
num = int(input('Digite um número de 1 até 10:'))
computador = random.randint(1, 10)

while num != computador:
    print(f'Valor incorreto, o número escolhido foi {computador}')
    num = int(input('Digite um número de 1 até 10:'))
    computador = random.randint (1, 10)
print(f'Parabéns, você acertou! O número escolhido foi: {computador}')
