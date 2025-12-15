
print('-' * 10)
print('Bem vindo a Calculadora 2.0')
print('-' * 10)

print('Escolha uma operacao: 1 - soma;2 - subtracao; 3 - multiplicacao; 4 - divisao.')

Op = int(input('Operacao: '))

a = float(input('digite o valor de a\na = '))
b = float(input('digite o valor de b\nb = '))

if Op == 1:
    print('a + b =', a + b)
elif Op == 2:
    print('a - b =', a - b)
elif Op == 3:
    print('a * b =', a * b)
elif Op == 4:
    print('a / b =', a / b)
else:
    print('Operacao invalida')