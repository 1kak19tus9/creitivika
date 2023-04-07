table = {'deaht':'94085'}
while True:
    a = input('Comand: exit/registration/login:')
    if a == 'registration':
        b = input('Enter login:')
        c = input('enter password:')
        d = input('Return password:')
        if b in table.keys() or  or d != c:
            print('Return please')
        else:
            nu = {b:c}
            table.update(nu)
    elif a == 'login':
        e = input('Enter login:')
        f = input('enter password:')
        if e in table.keys() and f in table.values():
            print('Welcome:)')
        else:
            print('please return')
    elif a == 'exit':
        break

