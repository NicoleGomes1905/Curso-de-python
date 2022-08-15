valor = float(input('Digite o valor da casa desejada:'))
salario = float(input('Digite o valor do seu salário:'))
anos = int(input('Digite em quantos anos você quer pagar a casa:'))


mensal = valor / (anos * 12)
parcela = salario * 30/100

print(f'Para uma casa de R${valor},00 em {anos} será necessário uma prestação de {mensal}')

if mensal >= parcela:
    print('Infelizmente não será possível aprovar seu empréstimo. pois o valor excede o limite')
else:
    print('Parabéns, o limite foi aprovado!')
