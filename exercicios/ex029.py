"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

salario = float(input('Insira seu salário: '))

if salario <= 280:
    aumento = 0.20
elif salario <= 700:
    aumento = 0.15
elif salario <= 1500:
    aumento = 0.10
else:
    aumento = 0.05

print('Seu salário era de ----> R$', salario)
print('O percentual de aumento foi de ---->', aumento * 100, '%')
print('O valor do aumento foi de ----> R$', (salario * aumento))
print('O valor do seu novo salário é de ----> R$', (salario * aumento) + salario)
