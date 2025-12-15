
conta = dict()
nomes = list()

a = ' '
while a != '':
    a = input('Inserir mais um nome?\n')
    nomes += [a.capitalize()]

nomes.remove('')
for nome in nomes:
    if nome in conta:
        conta[nome] += 1
    else:
        conta[nome] = 1
print(conta)