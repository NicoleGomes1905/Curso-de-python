sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
validacao = sexo

while sexo not in 'MmFf':
    print('Valor inválido, tente novamente')
    sexo = str(input('Digite seu sexo: [M/F]:')).strip().upper()[0]
print('Valor válido, cadastrado com sucesso')
