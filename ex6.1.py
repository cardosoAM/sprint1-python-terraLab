
n = int(input('Ate qual numero da sequencia de fibonacci deseja ver?\n'))
f = 0
prev_1 = 1
prev_2 = 0
print('Indice 1 f = 1')
for i in range(2, n + 1):
    f = prev_1 + prev_2
    prev_2 = prev_1
    prev_1 = f
    print('Indice', i, 'f =', f)