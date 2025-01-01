with open("employees.txt") as f:
    print(f.read(5))
    print(f.tell())
    f.seek(0)
    print(f.read())