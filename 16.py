from sys import setrecursionlimit

setrecursionlimit(2000)


def F(n):
    if n <= 5:
        return 1
    return n + F(n - 2)


print(F(2126) - F(2122))
# Ответ: 4250


F = [0] * 2130
for n in range(2130):
    if n <= 5:
        F[n] = 1
    else:
        F[n] = n + F[n - 2]

print(F[2126] - F[2122])
# Ответ: 4250
