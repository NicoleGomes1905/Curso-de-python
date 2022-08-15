import math
oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digite o comprimento do cateto adjacente:'))
hipotenusa = (oposto ** 2) + (adjacente ** 2)
print(f'A soma dos catetos {oposto} e {adjacente} é {hipotenusa}, sendo assim, a hipotenusa é {math.sqrt(hipotenusa)}')

co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print(f'A soma dos catetos {co} e {ca} é {hi}, sendo assim, a hipotenusa é {hi}')