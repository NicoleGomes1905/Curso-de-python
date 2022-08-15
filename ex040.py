nota = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota + nota2) / 2

if media < 5:
    print(f'Sua média é {media}! Sinto muito, você está reprovado.')
elif media >= 5 and media <= 6.9:
    print(f'Sua média é {media}! Sinto muito, você está de recuperação.')
else:
    print(f'Sua média é {media}! Parabéns! Você foi aprovado.')