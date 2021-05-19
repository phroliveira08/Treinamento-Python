entrada = input().split(" ")
X = int(entrada[0])
Y = int(entrada[1])

if 0 < X <= 50 and 0 < Y <= 50:
    print("R1", end="")
elif 0 < X <= 50 and -50 <= Y < 0:
    print("R4", end="")
elif -50 <= X < 0 and 0 < Y <= 50:
    print("R2", end="")
elif -50 <= X < 0 and -50 <= Y < 0:
    print("R3", end="")
elif X == 0 and Y == 0:
    print("NO ALVO!", end="")