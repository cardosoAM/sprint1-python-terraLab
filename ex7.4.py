
X_str = input('Informe o vetor X:\n')
X_str_list = X_str.split()
X = [int(i) for i in X_str_list]
Y_str = input('Informe o vetor Y:\n')
Y_str_list = Y_str.split()
Y = [int(i) for i in Y_str_list]

produto_escalar = 0
for i in range(3):
    produto_escalar += X[i] * Y[i]

produto_vetorial = list()
produto_vetorial.append(X[1] * Y[2] - X[2] * Y[1])
produto_vetorial.append(X[0] * Y[2] - X[2] * Y[0])
produto_vetorial.append(X[0] * Y[1] - X[1] * Y[0])

print('Produto escalar =', produto_escalar)
print('Produto vetorial =', produto_vetorial)