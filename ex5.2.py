
t = int(input('Digite o tempo total em segundos:\n'))

segundos = t % 60
t //= 60
minutos = t % 60
t //= 60
horas = t

print('O tempo digitado equivale a:\n', horas, ':', minutos, ':', segundos, sep='')