from datetime import date
ano = int(input('Informe um ano desejado (caso utilize o 0 irá ser fornecido o ano atual:'))
if ano == 0:
    ano = date.today().year
    print(f'O ano atual é {ano}')
if ano % 4 == 0 or ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')