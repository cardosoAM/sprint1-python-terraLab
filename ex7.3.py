
msg = input('Digite a mensagem:\n')

nova_msg = str()

for i in msg:
    if i.isupper():
        estou_em_nome = True
        nova_msg += '*'
        continue
    if estou_em_nome:
        if i.isalpha():
            nova_msg += '*'
            continue
        else:
            nova_msg += i
            estou_em_nome = False
    else:
        nova_msg += i

print(nova_msg)