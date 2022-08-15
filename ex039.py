from datetime import date

nascimento = int(input('Informe o ano do seu nascimento:'))
atual = date.today().year
idade = atual - nascimento


if idade == 18:
    print(f'Está na hora de você se alistar, pois você já tem {idade} anos!')
elif idade < 18:
    anos = 18 - idade
    alistamento = atual + anos
    print(f'Sem pressa, você ainda possui {idade} anos! Ainda falta {anos} anos para você se alistar, seu ano de alistamento é {alistamento}!')
else:
    faltante = idade - 18
    alistamento = atual - faltante
    print(f'Você já tem {idade} anos? Já passou do momento do seu alistamento há {faltante} anos, sendo o ano de alistamento {alistamento}.')