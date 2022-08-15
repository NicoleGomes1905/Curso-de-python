n1 = int(input('Digite um número: '))

n2 = [str(n1*i) for i in range(1,9)]

print (f'O numero escolhido é : {n1}, a tabuada é { ", ". join(n2)}')