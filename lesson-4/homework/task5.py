x = input('Enter password: ')
if len(x) < 8:
    print('Password is too short.')
else:
    uppercase_found = False
    for i in range(len(x)):
        if x[i].isupper():
            uppercase_found = True
            break
    if not uppercase_found:
        print('Password must contain an uppercase letter.')
    else:
        print('Password is strong.')