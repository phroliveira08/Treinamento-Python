T = int(input())

for t in range(T):
    linha = input().split(' ')
    linhaMax = max([int(e) for e in linha])
    linhaMin = min([int(e) for e in linha])
    print(str(linhaMin) + ' ' + str(linhaMax), end="\n")
    if linhaMin == linhaMax:
        print('S', end="" if t == T - 1 else "\n")
    else:
        print('N', end="" if t == T - 1 else "\n")