"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

name = str(input('Insira seu nome ----> '))
while len(name) <= 3:
    print('\nSeu nome precisa ter mais de 3 caracteres.')
    name = str(input('Insira seu nome ----> '))

age = int(input('Insira sua idade ----> '))
while age <= 0 or age >= 150:
    print('\nSua idade precisa estar entre 0 e 150 anos.')
    age = int(input('Insira sua idade ----> '))

sal = float(input('Insira seu salário ----> R$ '))
while sal <= 0:
    print('\nSeu salário não pode ser R$ 0')
    sal = float(input('Insira seu salário ----> R$ '))

sex = input('Insira seu sexo: [M]asculino [F]eminino ----> ').upper()
while sex != "M" and sex != "F":
    print('\nInsira uma opção válida.')
    sex = input('Insira seu sexo: [M]asculino [F]eminino ----> ').upper()

civil = input(
    'Insira seu estado civil: [C]asado [S]olteiro [V]iúvo [D]ivorciado ----> ').upper()
while civil != "C" and civil != "S" and civil != "V" and civil != "D":
    print('\nInsira uma opção válida.')
    civil = input(
        'Insira seu estado civil: [C]asado [S]olteiro [V]iúvo [D]ivorciado ----> ')

print('\nFim do programa.\n')
