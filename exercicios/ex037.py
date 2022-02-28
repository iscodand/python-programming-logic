"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

num = int(input('Insira um número inteiro menor que 1000 ----> '))

if num >= 1000 or num < 0:
    print('Valor inválido.')
    quit()

centenas = num // 100
dezenas = (num % 100) // 10
unidades = (num % 10)
separador1 = ""
separador2 = ""

if (centenas >= 1) and (dezenas >= 1) and (unidades >= 1):
    separador1 = " , "
    separador2 = " e "
elif (centenas >= 1 and unidades >= 1) or (dezenas >= 1 and unidades >= 1):
    separador1 = ""
    separador2 = " e "
elif (centenas >= 1 and dezenas >= 1):
    separador1 = " e "
    separador2 = ""

if centenas == 1:
    centenas = "1 centena"
elif centenas > 1:
    centenas = f"{centenas} centenas"
else:
    centenas = ""

if dezenas == 1:
    dezenas = "1 dezena"
elif dezenas > 1:
    dezenas = f"{dezenas} dezenas"
else:
    dezenas = ""

if unidades == 1:
    unidades = "1 unidade"
elif unidades > 1:
    unidades = f"{unidades} unidades"
else:
    unidades = ""

print(
    f'O número {num} possui: {centenas}{separador1}{dezenas}{separador2}{unidades}')
