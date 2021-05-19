x = int(input())
s1 = input()
y = int(input())
s2 = input()
z = int(input())

if s1 == '*':
    y = x * y
    if s2 == '+':
        y = y + z
        print(int(y), end="")
    elif s2 == '-':
        y = y - z
        print(int(y), end="")
elif s1 == '/':
    if y == 0:
        print("erro", end="")
    else:
        y = x / y
        if s2 == '+':
            y = y + z
            print(int(y), end="")
        elif s2 == '-':
            y = y - z
            print(int(y), end="")
elif s2 == '*':
    y = y * z
    if s1 == '+':
        y = x + y
        print(int(y), end="")
    elif s1 == '-':
        y = x - y
        print(int(y), end="")
elif s2 == '/':
    if z == 0:
        print("erro", end="")
    else:
        y = y / z
        if s1 == '+':
            y = x + y
            print(int(y), end="")
        elif s1 == '-':
            y = x - y
            print(int(y), end="")
elif s1 == '+':
    y = x + y
    if s2 == '*':
        y = y * z
    elif s2 == '/':
        if z == 0:
            print("erro", end="")
        else:
            y = y / z
            print(int(y), end="")
    elif s2 == '+':
            y = y + z
            print(int(y), end="")
    elif s2 == '-':
            y = y - z
            print(int(y), end="")
elif s1 == '-':
    y = x - y
    if s2 == '*':
        y = y * z
        print(int(y), end="")
    elif s2 == '/':
        if z == 0:
            print("erro", end="")
        else:
            y = y / z
            print(int(y), end="")
    elif s2 == '+':
            y = y + z
            print(int(y), end="")
    elif s2 == '-':
            y = y - z
            print(int(y), end="")
