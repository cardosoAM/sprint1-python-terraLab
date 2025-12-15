def foo(valor):
    print(f"Função foo executada com valor: {valor}")

def foo2(valor):
    print(f"Função foo2 executada com valor: {valor}")

X = 1  

if X == 1:
    foo(10)
elif X == 2:
    foo2(X)
elif X == 3:
    foo(5)
else:
    print('Erro')