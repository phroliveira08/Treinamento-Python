valor = int(input())

n100 = valor // 100
n100resto = valor % 100
n50 = n100resto // 50
n50resto = n100resto % 50
n20 = n50resto // 20
n20resto = n50resto % 20
n10 = n20resto // 10
n10resto = n20resto % 10
n5 = n10resto // 5
n5resto = n10resto % 5
n2 = n5resto // 2
n2resto = n5resto % 2
n1 = n2resto // 1
n1resto = n2resto % 1

print(str(n100) + " nota(s) de R$ 100")
print(str(n50) + " nota(s) de R$ 50")
print(str(n20) + " nota(s) de R$ 20")
print(str(n10) + " nota(s) de R$ 10")
print(str(n5) + " nota(s) de R$ 5")
print(str(n2) + " nota(s) de R$ 2")
print(str(n1) + " nota(s) de R$ 1", end='')
