# def f(N):
#     num = bin(N)[2:]
#     if num.count('1') % 2 == 0:
#         num = '10' + num[2:] + '0'
#     else:
#         num = '11' + num[2:] + '1'
#     return int(num, 2)
#
#
# for N in range(1, 500):
#     R = f(N)
#     if R > 480:
#         print(N)
# Ответ: 176