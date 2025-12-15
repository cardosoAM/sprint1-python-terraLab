
n = int(input('Digite o valor que deseja receber:\n'))

nota_100 = n // 100
n = n % 100
nota_50 = n // 50
n = n % 50
nota_10 = n // 10
n = n % 10
nota_1 = n // 1
n = n % 1

print('Notas de 100,00 reais:', nota_100)
print('Notas de 50,00 reais:', nota_50)
print('Notas de 10,00 reais:', nota_10)
print('Notas de 1,00 real:', nota_1)