"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

user = str(input('Insira seu nome de usuário (até 4 letras ou números) ----> '))
senha = str(input('Insira sua senha (até 4 letras ou números) ----> '))


while user == senha:
    senha = str(input(
        '\nSeu nome não pode ser igual a sua senha.\nInsira uma nova senha ----> '))

print('\nAcesso permitido.\n')
