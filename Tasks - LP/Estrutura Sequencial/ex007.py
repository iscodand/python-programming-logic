"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área 
para o usuário.
"""

lado = float(input('Insira o valor do lado do quadrado em metros: '))

area = lado * lado

print('O valor da área do quadrado é de', area,
      'metros. E esse valor dobrado é de', area * 2, 'metros.')
