salario = float(input('informe seu salário: R$'))
if salario > 2500.00:
	total = salario + (salario * 10/100) 
	print(f'Seu salário teve um aumento de 10%, o valor líquido dele é de: {total:.2f}R$')
elif salario <= 2500.00:
	total = salario + (salario * 15/100)
	print(f'Seu salário teve um aumento de 15%, o valor líquido dele é de {total:.2f}R$')