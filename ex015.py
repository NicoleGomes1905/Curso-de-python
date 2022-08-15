dia = int(input('Informe por quantos dias você gostaria de alugar o carro:'))
km = int(input('Informe quantos km será rodado:'))
d1 = dia * 60
d2 = km * 0.15
dinheiro = d1 + d2
print(f'Conforme sua solicitação, o aluguel será de R${dinheiro}, sendo R${d1} pela quantidade de dias e R${D2} pelos km rodados.')