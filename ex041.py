from datetime import date
ano = int(input('Digite seu ano de nascimento:'))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('Sua classificação é: MIRIM')
elif 9 < idade <= 14:
    print('Sua classificação é: INFANTIL')
elif 14 < idade <= 19:
    print('Sua classificação é: JUNIOR')
elif 19 < idade <= 25:
    print('Sua classificação é: SÊNIOR')
elif idade > 25:
    print('Sua classificação é: MASTER')