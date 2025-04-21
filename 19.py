# def f(x, p):
#     if x <= 87 and p == 3:
#         return True
#     elif x > 87 and p == 3:
#         return False
#     elif x <= 87:
#         return False
#     else:
#         if p % 2 == 0:
#             return f(x - 2, p + 1) or f(x // 2, p + 1)
#         else:
#             return f(x - 2, p + 1) and f(x // 2, p + 1)
#
# for S in range(89, 200):
#     if f(S, 1):
#         print(S)
# Ответ: 176


# def f(x, p):
#     if x <= 87 and p == 4:
#         return True
#     elif x > 87 and p == 4:
#         return False
#     elif x <= 87:
#         return False
#     else:
#         if p % 2 == 0:
#             return f(x - 2, p + 1) and f(x // 2, p + 1)
#         else:
#             return f(x - 2, p + 1) or f(x // 2, p + 1)
#
# for S in range(89, 500):
#     if f(S, 1):
#         print(S)
# Ответ: 178 179

def f(x, p):
    if x <= 87 and (p == 3  or p == 5):
        return True
    elif x > 87 and p == 5:
        return False
    elif x <= 87:
        return False
    else:
        if p % 2 == 0:
            return f(x - 2, p + 1) or f(x // 2, p + 1)
        else:
            return f(x - 2, p + 1) and f(x // 2, p + 1)

for S in range(89, 500):
    if f(S, 1):
        print(S)
# 180

