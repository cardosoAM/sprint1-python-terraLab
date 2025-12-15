
conta = dict()
nomes = ['Joao', 'Arthur', 'Ary', 'Isabela', 'Israel', 'Vitor', 'Joao']
for nome in nomes:
    if nome in conta:
        conta[nome] += 1
    else:
        conta[nome] = 1
print(conta)