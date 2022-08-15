salario = float(input('Digite qual é o seu salário: '))

if salario > 1250:
    aumento = salario * 10/100
    caumento = salario + aumento
    print(f'Você receberá um aumento de R${aumento}0, irá começar a ganhar R${caumento}0')
else:
    aumento = salario * 15 / 100
    caumento = salario + aumento
    print(f'Você receberá um aumento de R${aumento}0, irá começar a ganhar R${caumento}0')
