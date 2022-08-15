nome = input('Digite seu nome completo:')

print(f'Seu nome em maiusculo é: {nome.upper()}')

print(f'Seu nome em minúsculo é: {nome.lower()}')

print(f' A quantidade de letras no seu nome é: {len(nome) - nome.count(" ")}')

print(f"Seu primeiro nome tem {nome.find(' ')} letras.")

separado = nome.split()

print(f'Seu nome tem {len(separado[0])} letras')
