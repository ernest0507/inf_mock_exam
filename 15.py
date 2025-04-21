def f(x, y, A):
    return (5 < y) or (x > 32) or ((x + 2 * y) < A)


for A in range(500):
    flag = True
    for x in range(700):
        for y in range(700):
            if not f(x, y, A):
                flag = False

    if flag:
        print(A)
# Ответ: 43
