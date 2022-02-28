"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""

morango = int(
    input('Insira a quantidade (em KG) de morangos desejados ----> '))
maca = int(input('Insira a quantidade de maçãs (em KG) desejadas ----------> '))

if morango < 5:
    valor_morango = (2.5 * morango)
else:
    valor_morango = (2.20 * morango)

if maca < 5:
    valor_maca = (1.8 * maca)
else:
    valor_maca = (1.5 * maca)

peso_total = morango + maca
valor_total = valor_morango + valor_maca

if peso_total > 8 or valor_total > 25:
    desconto = (valor_total * 0.10)
else:
    desconto = 0

print(
    f'Você irá pagar R$ {valor_total - desconto} pela quantidade total de {peso_total} Kg de morangos e maçãs.')
