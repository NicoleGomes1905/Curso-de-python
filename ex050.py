soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
        print(soma)

print(f'Ao total foram somados {cont} números. A soma de todos os produtos foi: {soma}')