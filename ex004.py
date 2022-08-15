teste = input('Digite algo do seu desejo:')

print('Qual é a varíavel?', type(teste))

print('É númerico?', teste.isnumeric())

print('Tem espaço?', teste.isspace())

print('É letra?', teste.isalpha())

print('É alfanúmerico?', teste.isalnum())

print('Está em letras maiúsculas?', teste.isupper())

print('E minúsculas?', teste.islower())

print('Está capitalizada?', teste.istitle())