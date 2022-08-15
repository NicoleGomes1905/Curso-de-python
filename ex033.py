n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n2 < n1 > n3:
    print(f'O número maior é {n1}')
if n1 < n2 > n3:
    print(f'O maior número é {n2}')
if n2 < n3 > n1:
    print(f'O maior número é {n3}')
if n2 > n1 < n3:
    print(f'O menor número é {n1}')
if n1 > n2 < n3:
    print(f'O menor número é {n2}')
if n2 > n3 < n1:
    print(f'O menor número é {n3}')