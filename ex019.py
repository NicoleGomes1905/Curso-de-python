import random
aluno1 = (input('Digite o número do primeiro aluno:'))
aluno2 = (input('Digite o número do segundo aluno:'))
aluno3 = (input('Digite o número do terceiro aluno:'))
aluno4 = (input('Digite o número do quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]

print(f'Os alunos selecionados foram {aluno1}, {aluno2}, {aluno3} e {aluno4}. Porém, o escolhido foi o {random.choice(lista)}')