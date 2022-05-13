"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = (input('Insira [M] se você for homem e [F] se você for mulher: '))

if sexo == "M" or sexo == "m":
    print('O sexo definido foi o Masculino.')
elif sexo == "F" or sexo == "f" :
    print('O sexo definido foi o Feminino.')
else :
    print('O sexo escolhido é inválido.')