"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220."""

valor_hora = float(input('Insira o valor que você recebe por hora ----> R$ '))
horas_trabalho = float(
    input('Insira a quantidade de horas mensais trabalhadas ----------> '))
salario = (valor_hora * horas_trabalho)

if salario <= 900:
    desconto = 0
elif salario <= 1500:
    desconto = 0.05
elif salario <= 2500:
    desconto = 0.10
else:
    desconto = 0.20

print('Salário Bruto -----------> R$', salario)

ir = (salario * desconto)
print('(-) Imposto de Renda ----> R$', ir)

inss = (salario * 0.10)
print('(-) INSS ----------------> R$', inss)

fgts = (salario * 0.11)
print('FGTS --------------------> R$', fgts)

desconto_total = (ir) + (inss)
print('Desconto total ----------> R$', desconto_total)

salario_liquido = (salario) - (desconto_total)
print('Salário Líquido ---------> R$', salario_liquido)
