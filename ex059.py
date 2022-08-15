import random
num = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))

print("""Digite sua opção:
[1] somar
[2] multiplicar 
[3] maior
[4] novos números
[5] sair do programa""")

decisao = int(input("Escolha uma opção de 1 a 5: "))

while decisao != 5:

    if decisao == 1:
        soma = num + num2
        print(f'A soma dos números {num} e {num2} é: {soma}')
        decisao = int(input('Digite outra opção: '))
    elif decisao == 2:
        multiplicacao = num * num2
        print(f'A multiplicação entre os números {num} e {num2} é: {multiplicacao}')
        decisao = int(input('Digite outra opção: '))
    elif decisao == 3:
        if num > num2:
            print(f'O número {num} é maior que {num2}')
            decisao = int(input('Digite outra opção: '))
        elif num2 > num:
            print(f'O número {num2} é maior que {num}')
            decisao = int(input('Digite outra opção: '))
        else:
            print('Os números são iguais')
            decisao = int(input('Digite outra opção: '))
    elif decisao == 4:
        novo_num = random.randint(1,10000)
        print(f'Que tal utilizar as opções {novo_num} e {novo_num}?')
        decisao = int(input('Digite outra opção: '))
    else:
        print('Valor inválido, favor inserir valor novamente')
print('Fim da seleção')
